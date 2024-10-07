from abc import ABC, abstractmethod
from .abc_provider import IaProvider
from typing import Dict, Any


class ProviderFactoryABC(ABC):

    @abstractmethod
    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        raise NotImplementedError("Implement get_provider method.")
