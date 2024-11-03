import logging
from abc import ABC, abstractmethod
from .providers.abc_provider import ASRProvider
from typing import Dict

logger: logging.Logger = logging.getLogger(__file__)


class BenchmarkABC(ABC):
    @property
    @abstractmethod
    def providers(self) -> Dict[str, ASRProvider]:
        raise NotImplementedError("Implement providers property.")

    @abstractmethod
    def run(self) -> str:
        raise NotImplementedError("Implement run method.")

    @abstractmethod
    def run_with_provider(self, provider_name: str) -> str:
        raise NotImplementedError("Implement run with provider method.")

    def add_provider(self, name: str, provider: ASRProvider) -> None:
        if not isinstance(provider, ASRProvider):
            raise ValueError(f"Provider {name} is not instance of IaProvider")

        self.providers[name] = provider

    def remove_provider(self, name: str) -> None:
        if name not in self.providers:
            raise KeyError(f"Provider {name} does not exists.")

        self.providers.pop(name)
