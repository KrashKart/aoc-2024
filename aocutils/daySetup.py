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
SOLN_PY_FILE = os.path.abspath(f"{DIR}/day_{padded_day}.py")

PY_FILE_TEMPLATE = f"import aocutils\n\n@aocutils.timeFunction\ndef main():\n\tref = aocutils.readFile({day})\n\ttotal1, total2 = 0, 0\n\n\taocutils.printParts(total1, total2)\nif __name__ == \"__main__\":\n\tmain()"

# DO NOT RUN too frequently to throttle requests!
if __name__ == "__main__":
    if os.path.exists(TXT):
        print("Input already retrieved!")
    else:
        # make day_nn directory
        if not os.path.exists(DIR):
            print(f"Making directory {DIR}")
            os.mkdir(DIR)
        else:
            print(f"{DIR} exists, continuing...")

        # get puzzle input for the day
        print("Retrieving...")
        response = r.get(LINK, cookies=COOKIES, headers=HEADERS)

        # create and write puzzle input to .txt file
        print(f"Creating and writing to {TXT}...")
        with open(TXT, "w") as f:
            f.write(response.text)

        # create and write .py file template to py file
        print(f"Creating and writing to {SOLN_PY_FILE}...")
        with open(SOLN_PY_FILE, "w") as f:
            f.write(PY_FILE_TEMPLATE)
        print("Done!")