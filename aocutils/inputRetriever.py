import requests as r
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
day = now.day
year = now.year
padded_day = str(day).rjust(2, "0")

HEADERS = {'User-Agent': os.getenv("HEADER")}
COOKIES = {'session': os.getenv("SESSION_COOKIE_ID")}
LINK = f"https://adventofcode.com/{year}/day/{day}/input"

DIR = os.path.abspath(f"{os.getenv('DIRPATH')}/aoc_{year}/day_{padded_day}")
TXT = os.path.abspath(f"{DIR}/day_{padded_day}.txt")

# DO NOT RUN too frequently to throttle requests!
if os.path.exists(TXT):
    print("Input already retrieved!")
else:
    if not os.path.exists(DIR):
        print(f"Making directory {DIR}")
        os.mkdir(DIR)
    else:
        print(f"{DIR} exists, continuing...")

    print("Retrieving...")
    response = r.get(LINK, cookies=COOKIES, headers=HEADERS)

    print(f"Writing to {TXT}...")
    with open(TXT, "w") as f:
        f.write(response.text)
    print("Done!")