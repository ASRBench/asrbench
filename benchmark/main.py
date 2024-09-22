from pathlib import Path
from providers.faster_whisper_ import FasterWhisper, FasterWhisperCfg
from dtos.common import TranscribeResult
from enums import FasterWhisperSizeModels
from benchmarks import Benchmark
import logging

current_dir: str = Path(__file__).parent.__str__()

logging.basicConfig(
    level=logging.WARNING,
    format=(
        "[%(asctime)s] %(levelname)s:   %(message)s -  %(name)s:%(lineno)d"
    ),
    filemode="a",
    filename=f"{current_dir}/benchmark.log",
)

logger = logging.getLogger(__file__)

AUDIO_DIR: str = "benchmark/resources/audios"
REFERENCE_DIR: str = "benchmark/resources/references"

audio_path: Path = Path(AUDIO_DIR).joinpath("senna-e-galvao.wav")
reference_path: Path = Path(REFERENCE_DIR).joinpath("senna-e-galvao.txt")

fw_cfg = FasterWhisperCfg(
    model_size=FasterWhisperSizeModels.Medium,
    device="cpu",
    compute_type="int8",
    beam_size=5,
)

faster_whisper_provider = FasterWhisper(fw_cfg)

benchmark = Benchmark(audio_path, reference_path.open().read())
benchmark.add_provider("faster_whisper", faster_whisper_provider)
benchmark.run()
