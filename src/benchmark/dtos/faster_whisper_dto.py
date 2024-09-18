from dataclasses import dataclass


@dataclass
class FasterWhisperDTO:
    ModelSize: str
    Device: str
    Compute_Type: str
