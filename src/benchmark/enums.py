from enum import Enum


class FasterWhisperSizeModels(Enum, str):
    Tiny: str = "tiny"
    Small: str = "small"
    Base: str = "base"
    Medium: str = "medium"
    Large_V1: str = "large-v1"
    Large_V2: str = "large-v2"
    Large_V3: str = "large-v3"
