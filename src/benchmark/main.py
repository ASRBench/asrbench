from pathlib import Path
from dtos.faster_whisper_data import FasterWhisperCfg
from enums import FasterWhisperSizeModels
from f_whisper import fw_run

AUDIO_DIR: str = "src/benchmark/resources/audios"
REFENCE_DIR: str = "src/benchmark/resources/references"

audio_path: Path = Path(AUDIO_DIR).joinpath("senna-e-galvao.wav")
reference_path: Path = Path(REFENCE_DIR).joinpath("senna-e-galvao.txt")

fw_cfg = FasterWhisperCfg(
    ModelSize=FasterWhisperSizeModels.Medium,
    Device="cpu",
    Compute_Type="int8",
    Beam_Size=5,
    Audio_Path=audio_path.__str__(),
    Reference=reference_path.open().read()
)

fw_run(fw_cfg)
