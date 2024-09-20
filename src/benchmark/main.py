from pathlib import Path
from dtos.faster_whisper_data import FasterWhisperCfg
from enums import FasterWhisperSizeModels
from f_whisper import fw_run
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

AUDIO_DIR: str = "src/benchmark/resources/audios"
REFERENCE_DIR: str = "src/benchmark/resources/references"

audio_path: Path = Path(AUDIO_DIR).joinpath("senna-e-galvao.wav")
reference_path: Path = Path(REFERENCE_DIR).joinpath("senna-e-galvao.txt")

fw_cfg = FasterWhisperCfg(
    ModelSize=FasterWhisperSizeModels.Medium,
    Device="cpu",
    Compute_Type="int8",
    Beam_Size=5,
    Audio_Path=audio_path.__str__(),
    Reference=reference_path.open().read()
)

fw_run(fw_cfg)
