import re
from datetime import timedelta


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"[\s_]+", "-", text.strip().lower()))


def format_duration(seconds: float) -> str:
    return str(timedelta(seconds=int(seconds)))
