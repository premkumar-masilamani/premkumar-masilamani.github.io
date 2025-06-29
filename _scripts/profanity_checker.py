import os
import re
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Context-aware profanity list: (word, acceptable contexts, problematic contexts)
PROFANITY_LIST = [
    # Common profanity
    ("fuck", [], []),
    ("fucking", [], []),
    ("fucked", ["I am fucked"], []),
    ("ass", ["kick ass", "smart ass"], []),
    ("shit", ["get shit done", "shit together"], []),
    ("damn", ["damn good", "damn sure"], []),
    ("crap", ["feel like crap"], []),
    ("bitch", ["son of a bitch", "99% is a bitch"], []),
    # Inappropriate terms with context
    ("dumb", ["dumb terminal", "dumb luck", "dumb phone", "dumb brain"], []),
    ("idiot", ["what an idiot"], []),
    ("stupid", ["stupid question"], []),
    # Scientific terms
    ("homo", ["homo sapiens", "homo erectus"], []),
    # Sensitive topics
    ("rape", ["rape survivor", "against rape", "violent gang rape"], []),
    ("prostitute", ["prostitute themselves"], []),
    ("illegal", ["illegal activity", "illegal immigration"], []),
]


def find_directory():
    """Find the english directory relative to script location"""
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    # Try common locations
    paths = [
        Path("../english/blog"),  # From current directory
        script_dir / "../english/blog",  # Relative to script
        script_dir.parent / "english/blog",  # Sibling to scripts dir
    ]

    for path in paths:
        try:
            if path.exists() and path.is_dir():
                return path
        except:
            pass

    return None


def is_acceptable_context(text, word, acceptable_contexts):
    """Check if word appears in an acceptable context"""
    # If no acceptable contexts defined, assume it's always problematic
    if not acceptable_contexts:
        return False

    # Check if any acceptable context exists in the text
    text_lower = text.lower()
    return any(context.lower() in text_lower for context in acceptable_contexts)


def check_file(file_path):
    """Check a file for profanity with context awareness"""
    issues = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            for word, acceptable_contexts, problematic_contexts in PROFANITY_LIST:
                # Use regex to find whole words only
                for match in re.finditer(r"\b" + re.escape(word) + r"\b", line.lower()):
                    # Skip if word appears in acceptable context
                    if is_acceptable_context(line, word, acceptable_contexts):
                        continue

                    # Otherwise flag it
                    start, end = match.span()
                    prefix = line[max(0, start - 20) : start].strip()
                    suffix = line[end : min(len(line), end + 20)].strip()
                    highlight = f"{prefix} >>>{line[start:end]}<<< {suffix}"

                    issues.append(
                        {
                            "file": file_path,
                            "line": line_num,
                            "term": word,
                            "context": highlight,
                        }
                    )
    except Exception as e:
        print(f"Error checking {file_path}: {e}")

    return issues


def main():
    # Find the directory to scan
    directory = find_directory()
    if not directory:
        print("Error: Could not find the english directory.")
        print("Run this script from the project root or specify a directory.")
        sys.exit(1)

    # Find markdown and HTML files
    files_to_check = []
    for ext in [".md", ".html", ".htm"]:
        files_to_check.extend(list(directory.glob(f"**/*{ext}")))

    print(f"Scanning {len(files_to_check)} files in {directory}")

    # Process files in parallel
    all_issues = []
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = {
            executor.submit(check_file, str(file)): file for file in files_to_check
        }

        # Process results as they complete
        processed = 0
        for future in futures:
            try:
                results = future.result()
                all_issues.extend(results)

                # Update progress
                processed += 1
                if processed % 10 == 0 or processed == len(files_to_check):
                    print(
                        f"\rProcessed {processed}/{len(files_to_check)} files...",
                        end="",
                    )
            except Exception as e:
                print(f"\nError: {e}")

    print("\n")

    # Display results
    if not all_issues:
        print("No profanity or inappropriate content found!")
        return

    print(f"Found {len(all_issues)} instances of potentially problematic content:\n")

    # Group by file for better readability
    files_with_issues = {}
    for issue in all_issues:
        if issue["file"] not in files_with_issues:
            files_with_issues[issue["file"]] = []
        files_with_issues[issue["file"]].append(issue)

    # Print results
    for file_path, issues in files_with_issues.items():
        rel_path = os.path.relpath(file_path, str(directory))
        print(f"File: {rel_path}")
        print("-" * 80)

        for issue in issues:
            print(f"Line {issue['line']}: Found '{issue['term']}'")
            print(f"Context: {issue['context']}")
            print()

        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
