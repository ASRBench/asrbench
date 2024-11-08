import logging
from .abc_factory import TranscriberFactoryABC
from .abc_transcriber import Transcriber
from .registry import TranscriberRegistry
from typing import Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DefaultTranscriberFactory(TranscriberFactoryABC):
    def __init__(self) -> None:
        self.__registry: TranscriberRegistry = TranscriberRegistry()

    def get_transcriber(self, name: str, cfg: Dict[str, Any]) -> Transcriber:
        """Return IaProvider with provider config"""
        if "asr" not in cfg:
            raise KeyError(f"Missing asr in {name} config.")

        transcriber = self.__registry.get_transcriber(cfg["asr"])
        return transcriber.from_config(name, cfg)

    def from_config(
            self,
            providers_cfg: Dict[str, Dict[str, Any]],
    ) -> Dict[str, Transcriber]:
        """Set up transcribers dict from provider section in config file"""
        providers: Dict[str, Transcriber] = {}

        for name, provider_cfg in providers_cfg.items():
            providers[name] = self.get_transcriber(name, provider_cfg)

        logging.debug(f"transcribers for benchmark: {providers.__str__()}")
        return providers
