import time
import utils
from wer import get_wer
from dtos.faster_whisper_data import FasterWhisperCfg
from dtos.common import TranscribeResult
import models


# vosk, wav2vec, whisper e faster - whisper.


class Benchmark:
    """
    """

    def __init__(self, audio, reference: str):
        self.__audio = audio
        self.__reference = reference

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

    @audio.setter
    def audio(self, path: str) -> None:
        utils.check_path(path)
        self.__audio = path

    @reference.setter
    def reference(self, path: str) -> None:
        utils.check_path(path)
        self.__reference = path

    def run_faster_whisper(self, cfg: FasterWhisperCfg) -> TranscribeResult:
        model = models.FasterWhisper(cfg)
        start: float = time.time()
        hypothesis: str = model.transcribe(self.audio)
        end: float = time.time()
        wer: float = get_wer(self.reference, hypothesis)
        runtime: float = round((end-start)*(10**3), 3)
        duration: float = utils.get_audio_duration(self.audio)

        return TranscribeResult(
            ia="faster_whisper",
            hypothesis=hypothesis,
            reference=self.reference,
            compute_type=cfg.Compute_Type,
            beam_size=cfg.Beam_Size,
            model_size=cfg.ModelSize,
            wer=wer,
            accuracy=round(((1 - wer) * 100), 2),
            runtime=runtime,
            audio_duration=duration,
            rtf=utils.get_rtf(runtime, duration)
        )

    def run_vosk(self):
        ...

    def run_wav2vec(self):
        ...

    def run_whisper(self):
        ...
