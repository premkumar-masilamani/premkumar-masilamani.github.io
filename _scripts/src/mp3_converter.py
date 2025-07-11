import os
import re
import json
import subprocess
from datetime import datetime, timedelta
from typing import Dict
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

DEFAULT_FOLDER = "/Users/premkumar/Downloads/Podcast"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"[\s_]+", "-", text.strip().lower()))


def format_duration(seconds: float) -> str:
    return str(timedelta(seconds=int(seconds)))


def get_default_tags() -> Dict[str, str]:
    """Return default ID3 tags. Override in UI or test."""
    return {
        "artist": "பிரேம்குமார் மாசிலாமணி",
        "album": "நிகழே அதுவாய்",
        "date": datetime.now().strftime("%d-%b-%Y"),
    }


def get_user_tags(defaults: Dict[str, str]) -> Dict[str, str]:
    """Interactive prompt to override default tags."""
    tags = {}
    for tag, default in defaults.items():
        user_input = input(f"{tag.capitalize()} [{default}]: ").strip()
        tags[tag] = user_input if user_input else default
    return tags


def convert_with_ffmpeg(
    input_file: str, output_file: str, bitrate: str = "192k"
) -> bool:
    """Convert M4A to MP3 using FFmpeg with two-pass loudness normalization."""
    print("🔊 Analyzing loudness...")
    analysis_command = [
        "ffmpeg",
        "-i",
        input_file,
        "-af",
        "loudnorm=I=-16:LRA=11:TP=-1.5:print_format=json",
        "-f",
        "null",
        "-",
    ]
    # First pass just prints stats to stderr, no actual file is created.
    # It may have a non-zero exit code, which is fine.
    result = subprocess.run(analysis_command, capture_output=True, text=True)

    stderr_lines = result.stderr.strip()
    json_start = stderr_lines.rfind("{")
    json_end = stderr_lines.rfind("}") + 1

    if json_start == -1 or json_end == 0:
        print("❌ Could not find JSON stats in FFmpeg output.")
        print(result.stderr)
        return False

    json_str = stderr_lines[json_start:json_end]
    try:
        loudness_stats = json.loads(json_str)
    except json.JSONDecodeError:
        print("❌ Could not parse FFmpeg loudness stats.")
        print(json_str)
        return False

    print("🔊 Normalizing and converting...")
    normalization_command = [
        "ffmpeg",
        "-y",
        "-i",
        input_file,
        "-af",
        f"loudnorm=I=-16:LRA=11:TP=-1.5:"
        f"measured_I={loudness_stats['input_i']}:"
        f"measured_LRA={loudness_stats['input_lra']}:"
        f"measured_TP={loudness_stats['input_tp']}:"
        f"measured_thresh={loudness_stats['input_thresh']}:"
        f"offset={loudness_stats['target_offset']}",
        "-codec:a",
        "libmp3lame",
        "-b:a",
        bitrate,
        output_file,
    ]

    result = subprocess.run(normalization_command, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ FFmpeg Conversion Error:\n", result.stderr)
        return False

    print("✅ Conversion and normalization successful.")
    return True


def apply_id3_tags(file_path: str, tags: Dict[str, str]) -> None:
    """Apply ID3 tags to an MP3 file."""
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


def summarize_output(output_file: str) -> Dict[str, str]:
    """Return metadata summary for YAML frontmatter."""
    mp3_meta = MP3(output_file)
    return {
        "file_name": os.path.basename(output_file),
        "file_size": os.path.getsize(output_file),
        "duration": format_duration(mp3_meta.info.length),
    }


def process_file(
    input_path: str, output_path: str, tags: Dict[str, str]
) -> Dict[str, str]:
    """Full pipeline for one file."""
    if not convert_with_ffmpeg(input_path, output_path):
        raise RuntimeError("Conversion failed.")
    apply_id3_tags(output_path, tags)
    return summarize_output(output_path)


def main():
    folder = (
        input(f"Enter path to folder with .m4a files [{DEFAULT_FOLDER}]: ").strip()
        or DEFAULT_FOLDER
    )

    if not os.path.isdir(folder):
        print("❌ Invalid directory.")
        return

    m4a_files = [f for f in os.listdir(folder) if f.lower().endswith(".m4a")]
    if not m4a_files:
        print("❌ No .m4a files found.")
        return

    for m4a_file in m4a_files:
        print(f"\n🎧 Processing: {m4a_file}")
        episode_number = input("Episode number: ").strip()
        episode_title = input("Episode title: ").strip()
        safe_title = slugify(episode_title)
        filename = f"episode-{episode_number}-{safe_title}.mp3"

        full_input = os.path.join(folder, m4a_file)
        full_output = os.path.join(folder, filename)

        defaults = get_default_tags()
        tags = get_user_tags(defaults)
        tags["title"] = episode_title or tags.get("title", "Untitled")

        try:
            summary = process_file(full_input, full_output, tags)
        except RuntimeError as e:
            print(str(e))
            continue

        print("\nYAML Frontmatter for the podcast website:")
        print("-----------------------------------------")
        print(f"audio-file: {summary['file_name']}")
        print(f"audio-length: {summary['file_size']}")
        print(f"duration: {summary['duration']}")


if __name__ == "__main__":
    main()