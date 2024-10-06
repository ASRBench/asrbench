import logging
from .abc_factory import ProviderFactoryABC
from .abc_provider import IaProvider
from .faster_whisper_ import FasterWhisper
from .hf_provider import HFText2AudioProvider
from .vosk_ import Vosk
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper
from typing import Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class ProviderFactory(ProviderFactoryABC):

    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        if "provider" not in cfg:
            raise KeyError(f"Missing provider in {name} config.")
        provider: str = cfg["provider"]

        match provider:
            case "faster_whisper":
                logger.debug("Get faster_whisper provider.")
                return FasterWhisper(self._get_faster_whisper_cfg(name, cfg))
            case "whisper":
                logger.debug("Get whisper provider.")
                return Whisper(self._get_whisper_cfg(name, cfg))
            case "wav2vec":
                logger.debug("Get wav2vec provider.")
                return Wav2Vec(self._get_wav2vec_cfg(name, cfg))
            case "vosk":
                logger.debug("Get vosk provider.")
                return Vosk(self._get_vosk_cfg(name, cfg))
            case "hf":
                logger.debug("Get HF provider.")
                return HFText2AudioProvider(self._get_hf_config(name, cfg))
            case _:
                logger.error(
                    f"Error on get provider, {provider} does not exists.",
                )
                raise ValueError(f"Provider {provider} does not exists.")

    def get_providers(
            self,
            providers_cfg: Dict[str, Dict[str, Any]],
    ) -> Dict[str, IaProvider]:
        providers: Dict[str, IaProvider] = {}

        for name, provider_cfg in providers_cfg.items():
            providers[name] = self.get_provider(name, provider_cfg)

        logging.debug(f"providers for benchmark: {providers.__str__()}")
        return providers
