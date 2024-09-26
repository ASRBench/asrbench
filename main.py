import torch

from benchmark.providers.wav2vec_ import Wav2Vec, Wav2VecCfg
from benchmark.benchmark_ import Benchmark
from pathlib import Path

ref_path = Path("resources/references/senna-e-galvao.txt")
reference = ref_path.open().read()

cfg = Wav2VecCfg(
    compute_type=torch.float32,
    device="cpu",
    checkpoint="facebook/wav2vec2-large-xlsr-53-portuguese"
)

benchmark = Benchmark("resources/audios/senna-e-galvao.wav", reference)
benchmark.add_provider(
    name="wav2vec",
    provider=Wav2Vec(cfg)
)
benchmark.run()
