import requests as r
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
day = now.day
year = now.year
padded_day = str(day)
if day < 10:
    padded_day = "0" + padded_day

HEADERS = {'User-Agent': 'github.com/KrashKart by KrashKart'}
LINK = f"https://adventofcode.com/{year}/day/{day}/input"
DIR = f"./day_{padded_day}"
TXT = f"{DIR}/day_{padded_day}.txt"
COOKIES = {'session': os.getenv("SESSION_COOKIE_ID")}

# DO NOT RUN too frequently to throttle requests!
if os.path.exists(TXT):
    print("Input already retrieved!")
else:
    print("Retrieving!")
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    response = r.get(LINK, cookies=COOKIES, headers=HEADERS)

    with open(TXT, "w") as f:
        f.write(response.text)
    print("Done!")
