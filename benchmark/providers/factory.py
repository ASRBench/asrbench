from .abc_factory import ProviderFactoryABC
from .abc_provider import IaProvider
from .faster_whisper_ import FasterWhisper
from .vosk_ import Vosk
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper


class ProviderFactory(ProviderFactoryABC):
    def __init__(self):
        ...

    def get_provider(self, name: str) -> IaProvider:
        match name:
            case "faster-whisper":
                # mount cfg
                return FasterWhisper()
            case "whisper":
                # mount cfg
                return Whisper()
            case "wav2vec":
                # mount cfg
                return Wav2Vec()
            case "vosk":
                # mount cfg
                return Vosk()
            case _:
                raise ValueError(f"Provider {name} does not exists.")
