from abc import ABC, abstractmethod
from .abc_provider import IaProvider
from typing import Dict, Any


class ProviderFactoryABC(ABC):

    @abstractmethod
    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        """Get IaProvider with provider config"""
        raise NotImplementedError("Implement get_provider method.")

    @abstractmethod
    def from_config(
            self,
            config: Dict[str, Dict[str, Any]],
    ) -> Dict[str, IaProvider]:
        """Set up providers dict from provider section in config file"""
        raise NotImplementedError("Implement from_config method.")
