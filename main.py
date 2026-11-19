#!/usr/bin/env python3
"""News-image entry: write the front page to /output/entry.png.

The bundled image (entry.png, 1024x1024, 526851 bytes) sums up the
world news of Thursday 19 November 2026 as a newspaper front page:
the masthead names the day, the lead story is the first-ever
Trump-Xi-Putin trilateral in Shenzhen as APEC opens, and six cards
cover the Crimea bridge hit for a third day, US-Iran fire widening
to Kuwait and Bahrain, Cyclone Akvan nearing India's east coast,
GTA VI launching worldwide, Voyager 1 reaching one light-day from
Earth, and the EU's proposed 45bn euro loan for Ukraine.

Deterministic: the same bytes are copied on every run. No network,
standard library only.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = OUT / "entry.png"
    shutil.copyfile(src, dst)
    # Fail loudly on a short copy instead of shipping a broken image.
    assert dst.stat().st_size == src.stat().st_size, "entry.png copy mismatch"


if __name__ == "__main__":
    main()
