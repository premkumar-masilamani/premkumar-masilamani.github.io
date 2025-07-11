import os
import subprocess
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from utils import format_duration


def convert_with_ffmpeg(
    input_file: str, output_file: str, bitrate: str = "192k"
) -> bool:
    result = subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_file,
            "-codec:a",
            "libmp3lame",
            "-b:a",
            bitrate,
            output_file,
        ],
        capture_output=True,
        text=True,
    )

    return result.returncode == 0


def apply_id3_tags(file_path: str, tags: dict):
    try:
        audio_file = EasyID3(file_path)
    except Exception:
        from mutagen.id3 import ID3

        audio_file = ID3()
        audio_file.save(file_path)
        audio_file = EasyID3(file_path)

    for tag, value in tags.items():
        audio_file[tag] = value
    audio_file.save()


def summarize_output(output_file: str) -> dict:
    mp3_meta = MP3(output_file)
    return {
        "file_name": os.path.basename(output_file),
        "file_size": os.path.getsize(output_file),
        "duration": format_duration(mp3_meta.info.length),
    }
