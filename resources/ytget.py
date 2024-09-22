import os
import re
from pathlib import Path
from pytubefix import YouTube
from pydub import AudioSegment


def ytget_audio(url, out_dir: str) -> None:
    yt = YouTube(url)

    video = yt.streams.get_audio_only()
    if video is not None:
        filename: str = video.download(output_path=out_dir)

        path: Path = Path(filename)
        final_path: Path = __rename(path)

        __audio2wav(final_path)


def __rename(path: Path) -> Path:
    return path.rename(
        path.with_name(
            __normalize_filename(path.name),
        ),
    )


def __normalize_filename(filename: str) -> str:
    filename = filename.lower().replace(" ", "-")
    return re.sub("-+", "-", filename).strip("-")


def __audio2wav(filepath: Path) -> None:
    audio = AudioSegment.from_file(filepath)
    audio.export(filepath.with_suffix(".wav"), format="wav")

    os.remove(filepath)


if __name__ == "__main__":
    ytget_audio(
        "https://www.youtube.com/watch?v=m5T7WnUIrpU",
        "audios",
    )
