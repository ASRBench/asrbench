import time
import utils
from wer import get_wer
from dtos.common import TranscribeResult
from providers.abc_provider import IaProvider
from typing import Dict


# vosk, wav2vec, whisper e faster - whisper.

class DatasetBenchmark:
    ...


class Benchmark:
    """
    """

    def __init__(self, audio, reference: str):
        self.__audio: str = audio
        self.__reference: str = reference
        self.__providers: Dict[str, IaProvider] = {}

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    @providers.setter
    def providers(self, providers: Dict[str, IaProvider]) -> None:
        if providers is None:
            raise ValueError("Providers is empty.")

        if providers.values() is not IaProvider:
            raise ValueError("Providers is not IaProvider.")

        self.__providers = providers

    def add_provider(self, name: str, provider: IaProvider) -> None:
        self.providers[name] = provider

    def remove_provider(self, name: str) -> None:
        self.providers.pop(name)

    def run(self) -> None:
        ...

    def run_provider(self, provider_name: str) -> TranscribeResult:
        provider: IaProvider = self.providers.get(provider_name)
        if provider is None:
            raise KeyError(f"Provider {provider_name} not exists.")

        start: float = time.time()
        hypothesis: str = provider.transcribe(self.audio)
        runtime: float = round((time.time() - start) * (10 ** 3), 3)

        wer: float = get_wer(self.reference, hypothesis)
        duration: float = utils.get_audio_duration(self.audio)

        return TranscribeResult(
            ia=provider.__class__.__name__,
            params={},
            hypothesis=hypothesis,
            reference=self.reference,
            wer=wer,
            accuracy=round(((1 - wer) * 100), 2),
            runtime=round((runtime / 1000), 3),
            audio_duration=round((duration / 1000), 3),
            rtf=utils.get_rtf(runtime, duration)
        )
