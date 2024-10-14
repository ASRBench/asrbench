from pathlib import Path
from .transcribe import TranscribePair
from typing import List, Dict


def _get_param(data: Dict[str, str], param: str, name: str) -> str:
    if param not in data or data[param] is None:
        raise KeyError(f"Dataset {name} param {param} is missing.")
    return data[param]


class Dataset:
    def __init__(
            self,
            name: str,
            audio_dir: str,
            ref_dir: str,
    ):
        self.__name: str = name
        self.__audio_dir: Path = Path(audio_dir)
        self.__ref_dir: Path = Path(ref_dir)
        self.__pairs: List[TranscribePair] = []
        self.get_data()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def pairs(self) -> List[TranscribePair]:
        return self.__pairs

    def get_data(self) -> None:
        if not self.__audio_dir.is_dir():
            raise ValueError("Provided dir is not a directory or not exists.")

        for audio_file in self.__audio_dir.glob("*.wav"):
            ref_file: Path = self.__ref_dir.joinpath(
                audio_file.with_suffix(".txt").name,
            )

            if not ref_file.exists():
                raise FileNotFoundError(
                    f"Reference file for {audio_file.name} not exists.",
                )

            reference: str = ref_file.open().read()

            self.pairs.append(
                TranscribePair(
                    audio_path=audio_file.__str__(),
                    reference=reference,
                )
            )

    @classmethod
    def from_config(cls, name: str, config: Dict[str, str]):
        return Dataset(
            name=name,
            audio_dir=_get_param(config, "audio_dir", name),
            ref_dir=_get_param(config, "reference_dir", name)
        )

    def __repr__(self) -> str:
        return f"<Dataset dir={self.__audio_dir} with {len(self.pairs)} pairs.>"
