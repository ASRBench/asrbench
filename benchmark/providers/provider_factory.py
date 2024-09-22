from faster_whisper_ import FasterWhisper
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper


class DefaultProviderFactory:
    def __init__(self):
        ...

    def make_faster_whisper(self) -> FasterWhisper:
        raise NotImplementedError("Implement make_faster_whisper method.")

    def make_wav2vec(self) -> Wav2Vec:
        raise NotImplementedError("Implement make_wav2vec method.")

    def make_whisper(self) -> Whisper:
        raise NotImplementedError("Implement make_whisper method.")
