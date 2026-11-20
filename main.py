#!/usr/bin/env python3
"""Write the bundled 19 November news image to the grader's output path.

v2 entry. The 1024x1024 PNG lives in this repo as a single line of
base64 text (entry.png.b64) so the whole entry stays plain text files.
Decoding is stdlib-only, needs no network, and is fully deterministic:
every run emits byte-identical PNGs.
"""
import base64
from pathlib import Path

REPO = Path(__file__).resolve().parent
IMAGE_B64 = REPO / "entry.png.b64"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def load_png_bytes():
    """Decode the base64 file this repo ships into raw PNG bytes."""
    text = IMAGE_B64.read_text(encoding="ascii").strip()
    data = base64.b64decode(text)
    if not data.startswith(PNG_MAGIC):
        raise ValueError("entry.png.b64 does not decode to a PNG file")
    return data


def output_path():
    """Prefer /output when the grader provides it, else the repo dir."""
    out_dir = Path("/output")
    if out_dir.is_dir():
        return out_dir / OUTPUT_NAME
    return REPO / OUTPUT_NAME


def main():
    data = load_png_bytes()
    target = output_path()
    try:
        target.write_bytes(data)
    except OSError:
        # /output is there but read-only: fall back to the repo dir.
        target = REPO / OUTPUT_NAME
        target.write_bytes(data)
    print("wrote %s (%d bytes)" % (target, len(data)))


if __name__ == "__main__":
    main()
