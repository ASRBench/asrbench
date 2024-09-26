from abc import ABC, abstractmethod
from abc_provider import IaProvider


class ProviderFactoryABC(ABC):

    @abstractmethod
    def get_provider(self, name: str) -> IaProvider:
        raise NotImplementedError("Implement get_provider method.")
