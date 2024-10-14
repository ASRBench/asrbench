from dataclasses import dataclass
from typing import Dict


@dataclass
class Measures:
    wer: float
    cer: float
    mer: float
    wil: float
    wip: float


@dataclass
class TranscribeResult:
    audio: str
    ia: str
    provider_name: str
    params: Dict[str, str]
    reference: str
    hypothesis: str
    measures: Measures
    audio_duration: float
    runtime: float
    rtf: float
    accuracy: float

    def to_dict(self) -> Dict[str, any]:
        return {
            "audio": self.audio,
            "ia": self.ia,
            "provider_name": self.provider_name,
            "params": self.params,
            "reference": self.reference,
            "hypothesis": self.hypothesis,
            "wer": self.measures.wer,
            "cer": self.measures.cer,
            "mer": self.measures.mer,
            "wil": self.measures.wil,
            "wip": self.measures.wip,
            "audio_duration": self.audio_duration,
            "runtime": self.runtime,
            "rtf": self.rtf,
            "accuracy": self.accuracy,
        }


class TranscribePair:
    def __init__(self, audio_path: str, reference: str) -> None:
        self.__audio: str = audio_path
        self.__reference: str = reference

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

    def __repr__(self) -> str:
        return f"<TranscribeData audio={self.audio} reference={self.reference}>"
