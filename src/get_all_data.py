import time
from datetime import datetime
from pathlib import Path

from aocd import get_data
from tqdm import tqdm

THIS_YEAR = datetime.now().year
THIS_MONTH = datetime.now().month
TODAY = datetime.now().day

YEARS = list(range(2015, THIS_YEAR))
DAYS = list(range(1, 26))

ALL_DAYS = []
for year in range(2015, THIS_YEAR):
    for day in range(1, 26):
        ALL_DAYS.append((year, day))
if THIS_MONTH == 12:
    for day in range(1, min(TODAY, 25) + 1):
        ALL_DAYS.append((THIS_YEAR, day))


def path_for_day(yd):
    year, day = yd
    return Path.home() / f"aoc-data/{year}/input-{day:02}.txt"


def path_missing(yd):
    return not path_for_day(yd).exists() or path_for_day(yd).stat().st_size == 0


ALL_DAYS = list(filter(path_missing, ALL_DAYS))
for year, day in tqdm(ALL_DAYS):
    path_for_day((year, day)).parent.mkdir(exist_ok=True)
    data = get_data(
        session="53616c7465645f5fee2c45065f28449af5f7c608e969e1221a143a530168a75afa92eca7a7d75472de5696032976e73fb947679ff44a28de69f587f3056c3d92",
        day=day,
        year=year,
    )
    path_for_day((year, day)).write_text(data, encoding="utf-8")

    time.sleep(1)  # let's not spam the API
