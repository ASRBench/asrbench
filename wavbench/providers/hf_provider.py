import torch
import librosa
from .abc_provider import IaProvider
from .configs import HFCfg
from transformers import AutoModelForCTC, AutoProcessor
from typing import Dict, Any, List


class HFAudio2Text(IaProvider):

    def __init__(self, cfg: HFCfg) -> None:
        self.__name: str = cfg.name
        self.__params: Dict[str, Any] = cfg.__dict__
        self.__model = AutoModelForCTC.from_pretrained(
            pretrained_model_name_or_path=cfg.model,
            torch_dtype=cfg.compute_type,
        )
        self.__processor = AutoProcessor.from_pretrained(
            pretrained_model_name_or_path=cfg.model
        )

    @property
    def name(self) -> str:
        return self.__name

    @classmethod
    def from_config(cls, name: str, data: Dict[str, Any]):
        return HFAudio2Text(HFCfg.load(data, name))

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    def transcribe(self, audio_path: str) -> str:
        audio, sample_rate = librosa.load(audio_path, sr=16000)
        inputs = self.__processor(
            audio=audio,
            sampling_rate=16000,
            padding=True,
            return_tensors="pt"
        ).input_values

        inputs = inputs.to(self.__model.device)

        with torch.no_grad():
            logits = self.__model(inputs).logits

        predicted_ids: torch.Tensor = torch.argmax(logits, dim=-1)

        transcription: List[str] = self.__processor.batch_decode(predicted_ids)
        return transcription[0]
