import jiwer
import re
import unicodedata
from num2words import num2words
from .transcribe import Measures
from typing import List


def _normalize_number2word(texts: List[str]) -> List[str]:
    """Converts numerical digits in the text to their word equivalents.

    Parameters:
        texts : the input text list.

    Returns:
        the texts with numbers converted to words.
    """

    def replace_number(match: re.Match) -> str:
        number_as_word = num2words(
            int(match.group()),
        )

        return number_as_word

    return [re.sub(r'\b\d+\b', replace_number, txt) for txt in texts]


def _remove_accents(texts: List[str]) -> List[str]:
    return [
        ''.join(
            char for char in unicodedata.normalize('NFD', txt)
            if unicodedata.category(char) != 'Mn'
        ) for txt in texts
    ]


transform = jiwer.Compose(
    [
        jiwer.RemoveEmptyStrings(),
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation(),
        _normalize_number2word,
        _remove_accents,
        jiwer.ReduceToListOfListOfWords()
    ]
)

char_transform = jiwer.Compose(
    [
        jiwer.RemoveEmptyStrings(),
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation(),
        _normalize_number2word,
        _remove_accents,
        jiwer.ReduceToListOfListOfChars()
    ]
)

normalize_transform = jiwer.Compose(
    [
        jiwer.RemoveEmptyStrings(),
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation(),
        _remove_accents,
        _normalize_number2word,
    ]
)


def normalize_txt(txt: str) -> str:
    """Return the post-processed text from jiwer transform"""
    processed_txt = normalize_transform(txt)
    return "".join(processed_txt)


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
            reference_transform=char_transform,
            hypothesis=hypothesis,
            hypothesis_transform=char_transform
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
