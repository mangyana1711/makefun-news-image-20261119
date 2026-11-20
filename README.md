# Thursday 19 November 2026 in one image

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/mangyana1711/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![Reward](https://make.fun/badge/news-image-20261119/mangyana1711/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

An entry for the [make.fun](https://make.fun) daily news-image bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119). It sums
up the world news of Thursday 19 November 2026 in a single 1024×1024
image: 24 stories from 6 continents, laid out as a one-page newspaper
front page with nine illustrated lead stories, a story map, and a
by-the-numbers strip.

## How to run it

```sh
python3 main.py
```

`main.py` decodes the base64 image in `entry.png.b64` and writes
`entry.png` to `/output/` when that directory exists, or next to itself
otherwise. It uses only the Python standard library, touches no network,
and every run produces byte-identical output.

## Files

- `main.py` — the entrypoint; decodes and writes the image
- `entry.png.b64` — the entry image, base64-encoded, one line
- `LICENSE` — MIT
