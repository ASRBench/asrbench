from .abc_factory import ProviderFactoryABC
from .abc_provider import IaProvider
from .faster_whisper_ import FasterWhisper
from .vosk_ import Vosk
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper
from typing import Dict, Any, List


class ProviderFactory(ProviderFactoryABC):

    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        match name:
            case "faster_whisper":
                return FasterWhisper(self._get_faster_wisper_cfg(cfg))
            case "whisper":
                return Whisper(self._get_whisper_cfg(cfg))
            case "wav2vec":
                return Wav2Vec(self._get_wav2vec_cfg(cfg))
            case "vosk":
                return Vosk()
            case _:
                raise ValueError(f"Provider {name} does not exists.")

    def get_providers(
            self,
            providers_cfg: Dict[str, Dict[str, Any]],
    ) -> Dict[str, IaProvider]:
        providers: Dict[str, IaProvider] = {}

        for name, provider_cfg in providers_cfg.items():
            providers[name] = self.get_provider(name, provider_cfg)

        return providers
