import logging
from .abc_factory import TranscriberFactoryABC
from .abc_transcriber import Transcriber
from .faster_whisper_ import FasterWhisper
from .hf_provider import HFAudio2Text
from .vosk_ import Vosk
from .wav2vec_ import Wav2Vec
from .whisper_ import Whisper
from typing import Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DefaultTranscriberFactory(TranscriberFactoryABC):

    def get_transcriber(self, name: str, cfg: Dict[str, Any]) -> Transcriber:
        """Return IaProvider with provider config"""
        if "asr" not in cfg:
            raise KeyError(f"Missing asr in {name} config.")
        provider: str = cfg["asr"]

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

    def from_config(
            self,
            providers_cfg: Dict[str, Dict[str, Any]],
    ) -> Dict[str, Transcriber]:
        """Set up providers dict from provider section in config file"""
        providers: Dict[str, Transcriber] = {}

        for name, provider_cfg in providers_cfg.items():
            providers[name] = self.get_transcriber(name, provider_cfg)

        logging.debug(f"providers for benchmark: {providers.__str__()}")
        return providers
