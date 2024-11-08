import logging
import pkgutil
import importlib
from .abc_transcriber import Transcriber
from pathlib import Path
from typing import Dict, Type, List, Callable

logger: logging.Logger = logging.Logger(__file__)


def register_transcriber(id_: str) -> Callable[
    [Type[Transcriber]], Type[Transcriber]
]:
    def decorator(cls: Type[Transcriber]) -> Type[Transcriber]:
        TranscriberRegistry.register(id_, cls)
        return cls

    return decorator


def load_registers(pkg_path: Path, pkg: str = __package__) -> None:
    for _, name, _ in pkgutil.iter_modules([pkg_path]):
        importlib.import_module(f"{pkg}.{name}")


class TranscriberRegistry:
    __transcribers: Dict[str, Type[Transcriber]] = {}

    def __init__(self) -> None:
        load_registers(Path(__file__).parent)

    @classmethod
    def register(cls, id_: str, class_: Type[Transcriber]) -> None:
        logger.debug(f"Register transcriber {id_}.")
        cls.__transcribers[id_] = class_

    @classmethod
    def get_transcriber(cls, id_: str) -> Type[Transcriber]:
        if id_ not in cls.__transcribers:
            raise KeyError(f"Transcriber {id_} not registered.")

        logger.debug(f"Get transcriber {id_}.")
        return cls.__transcribers[id_]

    @classmethod
    def list_transcribers(cls) -> List[str]:
        return [class_ for class_ in cls.__transcribers.keys()]
