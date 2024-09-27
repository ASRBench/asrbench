from benchmark.dataset_benchmark import DatasetBenchmark
from benchmark.dataset import Dataset
from benchmark.providers.faster_whisper_ import FasterWhisper
from benchmark.providers.whisper_ import Whisper
from benchmark.providers import configs

dataset = Dataset(
    name="teste",
    directory="resources/teste",
    audio_ext=".wav",
    reference_ext=".txt"
)

fw_cfg = configs.FWhisperCfg(
    model_size="medium",
    device="cpu",
    compute_type="int8",
    beam_size=5
)

whisper_cfg = configs.WhisperCfg(
    model_size="medium",
    device="cpu",
    language="pt",
    fp16=False
)
print(f"dataset: {dataset}")
benchmark = DatasetBenchmark([dataset])
benchmark.add_provider("faster_whisper", FasterWhisper(fw_cfg))
benchmark.add_provider("whisper", Whisper(whisper_cfg))
benchmark.run()
