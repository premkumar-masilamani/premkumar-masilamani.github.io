import os
from utils import slugify
from tags import get_id3_tags_interactive
from converter import (
    convert_with_ffmpeg,
    apply_id3_tags,
    summarize_output,
)

DEFAULT_FOLDER = "/Users/premkumar/Downloads/Podcast"


def main():
    folder = (
        input(f"Enter path to folder with .m4a files [{DEFAULT_FOLDER}]: ").strip()
        or DEFAULT_FOLDER
    )

    if not os.path.isdir(folder):
        print("Invalid directory.")
        return

    m4a_files = [f for f in os.listdir(folder) if f.lower().endswith(".m4a")]
    if not m4a_files:
        print("No .m4a files found.")
        return

    for m4a_file in m4a_files:
        print(f"\nProcessing: {m4a_file}")
        episode_number = input("Episode number: ").strip()
        episode_title = input("Episode title: ").strip()
        safe_title = slugify(episode_title)
        filename = f"episode-{episode_number}-{safe_title}.mp3"

        full_input = os.path.join(folder, m4a_file)
        full_output = os.path.join(folder, filename)

        tags = get_id3_tags_interactive()
        tags["title"] = episode_title or tags.get("title", "Untitled")

        print(f"\nConverting: {full_input} → {full_output}")
        if not convert_with_ffmpeg(full_input, full_output):
            print("Conversion failed.")
            continue

        apply_id3_tags(full_output, tags)

        summary = summarize_output(full_output)
        print("\nYAML Frontmatter for the podcast website:")
        print("-----------------------------------------")
        print(f"audio-file: {summary['file_name']}")
        print(f"audio-length: {summary['file_size']}")
        print(f"duration: {summary['duration']}")


if __name__ == "__main__":
    main()
