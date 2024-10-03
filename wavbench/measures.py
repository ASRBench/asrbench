import jiwer
import unicodedata
from .dtos.common import Measures


def _remove_accents(text: str) -> str:
    return ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )


transform = jiwer.Compose(
    [
        jiwer.RemoveEmptyStrings(),
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation(),
        _remove_accents,
        jiwer.ReduceToListOfListOfWords(),
    ]
)


def get_measures(reference: str, hypothesis: str) -> Measures:
    """Returns all measures provided by jiwer (wer, cer, mer, wil, wip)"""
    return Measures(
        wer=get_wer(reference, hypothesis),
        cer=get_cer(reference, hypothesis),
        mer=get_mer(reference, hypothesis),
        wil=get_wil(reference, hypothesis),
        wip=get_wip(reference, hypothesis)
    )


def get_wer(reference: str, hypothesis: str) -> float:
    """Measure Word Error Rate [WER]"""
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
    """Measure Character Error Rate [CER]"""
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
    """Measure Match Error Rate [MER]"""
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
    """Measure Word Information Lost [WIL]"""
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
    """Measure Word Information Preserved [WIP]"""
    return round(
        jiwer.wip(
            reference=reference,
            reference_transform=transform,
            hypothesis=hypothesis,
            hypothesis_transform=transform
        ),
        2
    )
