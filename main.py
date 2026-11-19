#!/usr/bin/env python3
"""Decode the bundled news image and write it to the output path.

The image is stored in this repo as base64 text (entry.png.b64) because
the repo is pushed as text files only. This script is deterministic: the
same input always produces the same PNG bytes.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png.b64")
    with open(src, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read().strip())
    out_dir = "/output" if os.path.isdir("/output") else HERE
    out = os.path.join(out_dir, "entry.png")
    try:
        with open(out, "wb") as f:
            f.write(data)
    except OSError:
        # /output exists but is not writable: fall back to the repo dir.
        out = os.path.join(HERE, "entry.png")
        with open(out, "wb") as f:
            f.write(data)
    print("wrote %s (%d bytes)" % (out, len(data)))


if __name__ == "__main__":
    main()
