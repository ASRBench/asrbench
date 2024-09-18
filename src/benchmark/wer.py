from typing import List
import jiwer

transform = jiwer.Compose(
    [
        jiwer.RemoveEmptyStrings(),
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation(),
        jiwer.ReduceToListOfListOfWords(),
    ]
)


def get_wer(reference: str, hypothesis: List[str]) -> float:
    return round(
        jiwer.wer(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )
