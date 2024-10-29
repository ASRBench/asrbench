import sys
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update_progress(self, progress: float, message: str) -> None:
        raise NotImplementedError("Implement update_progress method.")

    @abstractmethod
    def notify(self, message: str) -> None:
        raise NotImplementedError("Implement notify method.")

    @abstractmethod
    def finish(self) -> None:
        raise NotImplementedError("Implement finish method.")


class ConsoleObserver(Observer):
    def update_progress(self, progress: float, message: str) -> None:
        self.__display_message(f"\r[{progress * 100:.2f}%] {message}")

    def notify(self, message: str) -> None:
        self.__display_message(f"{message}")

    def finish(self) -> None:
        self.__display_message("\t Finished.\n")

    @staticmethod
    def __display_message(message: str) -> None:
        sys.stdout.write(message)
        sys.stdout.flush()
