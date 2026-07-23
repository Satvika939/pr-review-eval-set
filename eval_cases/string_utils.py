import re


def slugify(text):
    """Convert text into a lowercase, hyphen-separated slug."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
