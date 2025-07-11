from datetime import datetime


def get_id3_tags_interactive() -> dict:
    defaults = {
        "artist": "பிரேம்குமார் மாசிலாமணி",
        "album": "நிகழே அதுவாய்",
    }

    tags = {}
    for tag, default in defaults.items():
        user_input = input(f"{tag.capitalize()} [{default}]: ").strip()
        tags[tag] = user_input if user_input else default

    tags["date"] = datetime.now().strftime("%d-%b-%Y")
    return tags
