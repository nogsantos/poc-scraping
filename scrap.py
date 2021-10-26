import json
import sys

# import pandas as pd
from gazpacho import get, Soup

package = input("Enter the package name: ")

source = f"https://pypi.org/project/{package}/#history"

try:
    soup = Soup.get(source)
except Exception as err:
    sys.exit(f"{err}")

cards = soup.find('a', {'class': 'card'})

def scrap():
    return [
        {
            "version": card.find("p", {"class": "release__version"}, partial=False).text,
            'released_at': card.find("time").attrs['datetime']
        } for card in cards
    ]

# (pd.DataFrame(scrap())
#   .assign(released_at=lambda d: pd.to_datetime(d['released_at'])))

with open(f"{package}.json", "w") as f:
    json.dump(scrap(), f)

sys.exit(f"File {package}.json was successfully created")
