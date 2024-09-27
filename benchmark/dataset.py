from typing import List
from pathlib import Path
from typing import Dict


def _get_param(data: Dict[str, str], param: str, name: str) -> str:
    if param not in data or data[param] is None:
        raise KeyError(f"Dataset {name} param {param} is missing.")
    return data[param]


class TranscribePairData:
    def __init__(self, audio: str, reference: str) -> None:
        self.__audio: str = audio
        self.__reference: str = reference

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

    def __repr__(self) -> str:
        return f"<TranscribeData audio={self.audio} reference={self.reference}>"


class Dataset:
    def __init__(
            self,
            name: str,
            directory: str,
            audio_ext: str,
            reference_ext: str,
    ):
        self.__name: str = name
        self.__dir: Path = Path(directory)
        self.__audio_ext: str = audio_ext
        self.__reference_ext: str = reference_ext
        self.__pairs: List[TranscribePairData] = []
        self.get_data()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def pairs(self) -> List[TranscribePairData]:
        return self.__pairs

    def get_data(self) -> None:
        if not self.__dir.is_dir():
            raise ValueError("Provided dir is not a directory.")

        for audio_file in self.__dir.glob(f"*{self.__audio_ext}"):
            ref_file: Path = audio_file.with_suffix(f"{self.__reference_ext}")
            print(f"audio_file: {audio_file}")
            if not ref_file.exists():
                raise FileNotFoundError(
                    f"Reference file for {audio_file.name} not exists.",
                )

            reference: str = ref_file.open().read()
            print(f"reference: {reference}")

            self.pairs.append(
                TranscribePairData(
                    audio=audio_file.__str__(),
                    reference=reference,
                )
            )

    @classmethod
    def from_config(cls, name: str, config: Dict[str, str]):
        return Dataset(
            name=name,
            directory=_get_param(config, "dir", name),
            audio_ext=_get_param(config, "audio_ext", name),
            reference_ext=_get_param(config, "reference_ext", name)
        )

    def __repr__(self) -> str:
        return f"<Dataset dir={self.__dir} with {len(self.pairs)} pairs.>"
