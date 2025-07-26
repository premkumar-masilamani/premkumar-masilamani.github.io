import sys
from pathlib import Path
from collections import defaultdict


def get_all_files_recursively(folder: Path, extensions=None):
    """Return all files with given extensions in folder, recursively."""
    if extensions:
        return [
            f
            for f in folder.rglob("*")
            if f.is_file() and f.suffix.lower() in extensions
        ]
    return [f for f in folder.rglob("*") if f.is_file()]


def is_file_referenced(file_name, text):
    """Check if a file name appears in the text (simple substring match)."""
    return file_name in text


def scan_text_files(root_folder: Path, extensions):
    """Return a dictionary mapping each text file path to its content."""
    files = get_all_files_recursively(root_folder, extensions)
    return {file: file.read_text(encoding="utf-8", errors="ignore") for file in files}


def main(project_folder):
    root_path = Path(project_folder).expanduser().resolve()

    print(f"📁 Scanning recursively under: {root_path}\n")

    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".svg",
        ".bmp",
        ".tiff",
    }
    text_extensions = {".md", ".markdown", ".html", ".htm"}

    # Step 1: Collect all image files
    image_files = get_all_files_recursively(root_path, image_extensions)

    # Step 2: Collect Markdown and HTML files
    text_files = scan_text_files(root_path, text_extensions)

    used_in_posts = defaultdict(list)
    unused_images = []

    # Step 3: Check each image for usage in text files
    for image_path in image_files:
        image_name = image_path.name
        found = False
        for text_file, content in text_files.items():
            if is_file_referenced(image_name, content):
                used_in_posts[image_path].append(text_file)
                found = True
        if not found:
            unused_images.append(image_path)

    # Step 4: Output results
    print("=== ✅ Referenced Image Files ===")
    for file, refs in used_in_posts.items():
        print(f"{file.relative_to(root_path)} →")
        for ref in refs:
            print(f"    - {ref.relative_to(root_path)}")

    print("\n=== ⚠️ Unreferenced Image Files ===")
    for file in unused_images:
        print(f"{file.relative_to(root_path)} (not used)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_image_references.py <path_to_project_folder>")
        sys.exit(1)

    main(sys.argv[1])
