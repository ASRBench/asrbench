import librosa
import json
import numpy as np
from typing import Dict, Any
from .abc_provider import IaProvider
from vosk import Model, KaldiRecognizer


class Vosk(IaProvider):
    def __init__(self, model_name: str):
        self.__params = None
        self.__model = Model(model_name)
        self.__recognizer = KaldiRecognizer(self.__model, 16000)

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    def transcribe(self, audio_path: str) -> str:
        audio, sample_rate = librosa.load(audio_path, sr=16000)
        audio_int16 = (audio * 32767).astype(np.int16).tobytes()

        recognizer = KaldiRecognizer(self.__model, sample_rate)
        recognizer.AcceptWaveform(audio_int16)

        final_result = json.loads(recognizer.FinalResult())

        return final_result["text"]

