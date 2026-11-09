import json
import requests
from bs4 import BeautifulSoup

USERNAME = "lokesh3ac-ai"

def fetch():
    url = f"https://github.com/users/{USERNAME}/contributions"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    days = soup.find_all("td", class_="ContributionCalendar-day")
    
    data = []
    for td in days:
        date = td.get("data-date")
        level = td.get("data-level", "0")
        if date:
            data.append({"date": date, "level": int(level)})
            
    with open("data/contributions.json", "w") as f:
        json.dump(data, f)
    print(f"Fetched {len(data)} contribution days.")

if __name__ == "__main__":
    fetch()