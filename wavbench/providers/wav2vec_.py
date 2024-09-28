import torch
import librosa
from .abc_provider import IaProvider
from .configs import Wav2VecCfg
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from typing import Dict, Any, List


class Wav2Vec(IaProvider):
    def __init__(self, cfg: Wav2VecCfg) -> None:
        self.__params = cfg.__dict__
        self.checkpoint = cfg.checkpoint
        self.__model: Wav2Vec2ForCTC = Wav2Vec2ForCTC.from_pretrained(
            pretrained_model_name_or_path=cfg.checkpoint,
            torch_dtype=cfg.compute_type,
        ).to(cfg.device)
        self.__processor: Wav2Vec2Processor = Wav2Vec2Processor.from_pretrained(
            cfg.checkpoint

        )

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
