# make.fun news image — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/mangyana1711/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![Reward](https://make.fun/badge/news-image-20261119/mangyana1711/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for the [make.fun](https://make.fun) daily news-image bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119): one
1024×1024 image summing up the world news of Thursday 19 November 2026 —
24 stories across 6 continents, drawn as a one-page newspaper front page.

## Run

```sh
python3 main.py
```

Writes `entry.png` to `/output/` (or the current directory if `/output`
does not exist). The image is stored as base64 in `entry.png.b64` and
decoded by `main.py`; the output is deterministic — every run produces
byte-identical PNGs.

## Contents

- `main.py` — stdlib-only decoder, no network access
- `entry.png.b64` — the 1024×1024 entry image, base64-encoded
