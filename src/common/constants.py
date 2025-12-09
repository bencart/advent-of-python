import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

CORRECT = "✅"
WRONG = "❌"
YEAR = datetime.now().year
URL_TEMPLATE = "https://adventofcode.com/{year}/day/{day}/input"
COOKIE = os.environ.get("COOKIE")
REPO = "https://github.com/bencart/advent-of-python"
