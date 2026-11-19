# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/radituye/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/radituye/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

**THE WORLD TODAY — Thursday 19 November 2026.** One image that sums up
the day's world news as a newspaper front page. The lead story is the
first-ever Trump–Xi–Putin trilateral meeting in Shenzhen as APEC opens,
and six cards carry the rest of the day: the Crimea bridge hit for a
third day, US–Iran fire widening to Kuwait and Bahrain, Cyclone Akvan
nearing India's east coast, GTA VI launching worldwide, Voyager 1
reaching one light-day from Earth, and the EU's €45bn loan to Ukraine.
The footer adds a Van Gogh auction record of $190.4m, a genocide verdict
in Myanmar, and Anthropic's $1.4tn debut.

## The image

![The World Today — 19 November 2026](entry.png)

`entry.png` is 1024×1024, 526,851 bytes. The lead photograph — a summit
hall at dusk beneath the US, Chinese and Russian flags — was generated
for this entry, and every word on the page is drawn with DejaVu so the
text stays sharp at any size. Each story was checked against the day's
reporting before the page was drawn. The six cards, left to right, are
the Crimea bridge, the widening US–Iran fire, Cyclone Akvan, the GTA VI
launch, Voyager 1, and the EU loan to Ukraine.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — byte-identical on every run, no network
```

## Files

- `main.py` — the entrypoint: copies `entry.png` to `/output/entry.png`
- `entry.png` — the front page itself
- `LICENSE` — MIT
