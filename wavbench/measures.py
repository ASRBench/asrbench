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


def get_wer(reference: str, hypothesis: str) -> float:
    return round(
        jiwer.wer(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )


def get_cer(reference: str, hypothesis: str) -> float:
    return round(
        jiwer.cer(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )


def get_mer(reference: str, hypothesis: str) -> float:
    return round(
        jiwer.mer(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )


def get_wil(reference: str, hypothesis: str) -> float:
    return round(
        jiwer.wil(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )


def get_wip(reference: str, hypothesis: str) -> float:
    return round(
        jiwer.wip(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )
