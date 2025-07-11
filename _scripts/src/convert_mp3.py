import token
import os
import re
import subprocess
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from datetime import timedelta


def slugify(text):
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"[\s_]+", "-", text.strip().lower()))


def get_id3_tags():
    print("\n--- ID3 Tag Setup ---")
    defaults = {
        "artist": "பிரேம்குமார் மாசிலாமணி",
        "album": "நிகழே அதுவாய்",
    }

    tags = {}
    for tag, default in defaults.items():
        user_input = input(f"{tag.capitalize()} [{default}]: ").strip()
        tags[tag] = user_input if user_input else default

    return tags


def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))


def convert_with_ffmpeg(input_file, output_file):
    result = subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_file,
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "192k",
            output_file,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("❌ ffmpeg conversion failed:")
        print(result.stderr)
        return False
    return True


def convert_m4a_to_mp3(input_file, output_file, tags):
    print(f"\n🔄 Converting: {input_file} → {output_file}")

    if not convert_with_ffmpeg(input_file, output_file):
        return

    # Apply ID3 tags
    try:
        audio_file = EasyID3(output_file)
    except Exception:
        from mutagen.id3 import ID3

        audio_file = ID3()
        audio_file.save(output_file)
        audio_file = EasyID3(output_file)

    for tag, value in tags.items():
        audio_file[tag] = value
    audio_file.save()

    mp3_meta = MP3(output_file)
    file_size = os.path.getsize(output_file)
    duration = format_duration(mp3_meta.info.length)

    print("YAML Frontmatter for the podcast website:")
    print("-----------------------------------------")
    print(f"audio-file: {os.path.basename(output_file)}")
    print(f"audio-length: {file_size}")
    print(f"duration: {duration}")


def main():
    default_folder = "/Users/premkumar/Downloads/Podcast"
    folder = input(f"Enter path to folder with .m4a files [{default_folder}]: ").strip()
    folder = folder if folder else default_folder

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

        tags = get_id3_tags()
        tags["title"] = episode_title or tags["title"]

        convert_m4a_to_mp3(full_input, full_output, tags)


if __name__ == "__main__":
    main()
