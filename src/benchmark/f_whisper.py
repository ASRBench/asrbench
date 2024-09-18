from faster_whisper import WhisperModel
from enums import FasterWhisperSizeModels
from wer import get_wer

model = WhisperModel(
    FasterWhisperSizeModels.Base,
    device="cpu",
    compute_type="int8",
)
audio_dir = "./audios/clips"
audio_name = "common_voice_pt_38490975.mp3"

segments, info = model.transcribe(
    "./audios/clips/common_voice_pt_38490975.mp3", beam_size=5
)

print(
    "Detected language '%s' with probability %f"
    % (info.language, info.language_probability)
)

transcript = [seg.text for seg in segments]
reference: str = "Foi um vareio"

print("Reference: ", reference)
print("Transcript: ", transcript)
print("Result: ", get_wer(reference=reference, hypothesis=transcript))
