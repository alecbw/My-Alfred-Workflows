import requests
import sys

query = sys.argv[1].replace(" ", "+")
response = requests.get(f"https://jobs.smartrecruiters.com/sr-jobs/search?keyword={query}&limit=100")

print(response.raise_for_status())
data = response.json()['content']
for row in data:
    print(row.get("company", {}).get("name"), row.get("applyUrl"))

