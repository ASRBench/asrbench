from faster_whisper import WhisperModel
from dtos.faster_whisper_data import FasterWhisperCfg, FasterWhisperData
from wer import get_wer


def fw_run(cfg: FasterWhisperCfg) -> None:
    model = WhisperModel(
        model_size_or_path=cfg.ModelSize,
        device=cfg.Device,
        compute_type=cfg.Compute_Type
    )

    segments, info = model.transcribe(
        audio=cfg.Audio_Path,
        beam_size=cfg.Beam_Size,
    )

    hypothesis: str = " ".join([seg.text for seg in segments])

    data = FasterWhisperData(
        Wer=get_wer(cfg.Reference, hypothesis),
        Info=info,
        Cfg=cfg
    )

    __show_info(data)
    print(f">>> hypothesis: {hypothesis}")


def __show_info(data: FasterWhisperData) -> None:
    info = data.Info
    lang_probability: float = round(info.language_probability, 2)*100

    print(
        f"Lang: {info.language} \t\tLang Accuracy: {lang_probability}%",
    )
    print(f"IA: FasterWhisper \tModel Size: {data.Cfg.ModelSize.__str__()}")
    print(f"Device: {data.Cfg.Device}\t\tCompute Type: {data.Cfg.Compute_Type}")
    print(f"Wer: {data.Wer} \t\tAccuracy: {(1 - data.Wer) * 100}%")
