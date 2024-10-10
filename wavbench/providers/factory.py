import logging
from .abc_factory import ProviderFactoryABC
from .abc_provider import IaProvider
from .faster_whisper_ import FasterWhisper
from .hf_provider import HFAudio2Text
from .vosk_ import Vosk
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper
from typing import Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class ProviderFactory(ProviderFactoryABC):

    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        """Return IaProvider with provider config"""
        if "provider" not in cfg:
            raise KeyError(f"Missing provider in {name} config.")
        provider: str = cfg["provider"]

        match provider:
            case "faster_whisper":
                logger.debug("Get faster_whisper provider.")
                return FasterWhisper.from_config(name, cfg)
            case "whisper":
                logger.debug("Get whisper provider.")
                return Whisper.from_config(name, cfg)
            case "wav2vec":
                logger.debug("Get wav2vec provider.")
                return Wav2Vec.from_config(name, cfg)
            case "vosk":
                logger.debug("Get vosk provider.")
                return Vosk.from_config(name, cfg)
            case "hf":
                logger.debug("Get HF provider.")
                return HFAudio2Text.from_config(name, cfg)
            case _:
                logger.error(
                    f"Error on get provider, {provider} does not exists.",
                )
                raise ValueError(f"Provider {provider} does not exists.")

    def get_providers(
            self,
            providers_cfg: Dict[str, Dict[str, Any]],
    ) -> Dict[str, IaProvider]:
        """Set up providers dict from provider section in config file"""
        providers: Dict[str, IaProvider] = {}

        for name, provider_cfg in providers_cfg.items():
            providers[name] = self.get_provider(name, provider_cfg)

        logging.debug(f"providers for benchmark: {providers.__str__()}")
        return providers
