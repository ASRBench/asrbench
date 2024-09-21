from abc import ABC, abstractmethod
from faster_whisper import WhisperModel
from dtos.faster_whisper_data import FasterWhisperCfg


class ModelIa(ABC):

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")


class FasterWhisper(ModelIa):
    def __init__(self, cfg: FasterWhisperCfg):
        self.__model_size: str = cfg.ModelSize
        self.__beam_size: int = cfg.Beam_Size
        self.__device: str = cfg.Device
        self.__compute_type: str = cfg.Compute_Type

    @property
    def model_size(self) -> str:
        return self.__model_size

    @model_size.setter
    def model_size(self, model_size: str) -> None:
        self.__model_size = model_size

    @property
    def beam_size(self) -> int:
        return self.__beam_size

    @beam_size.setter
    def beam_size(self, beam_size: int) -> None:
        self.__beam_size = beam_size

    @property
    def device(self) -> str:
        return self.__device

    @device.setter
    def device(self, device: str) -> None:
        self.__device = device

    @property
    def compute_type(self) -> str:
        return self.__compute_type

    @compute_type.setter
    def compute_type(self, compute_type: str) -> None:
        self.__compute_type = compute_type

    def transcribe(self, audio_path: str) -> str:
        model = WhisperModel(
            model_size_or_path=self.model_size,
            device=self.device,
            compute_type=self.compute_type
        )

        segments, info = model.transcribe(
            audio=audio_path,
            beam_size=self.beam_size,
        )

        return " ".join([seg.text for seg in segments])
