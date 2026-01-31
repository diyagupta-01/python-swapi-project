import requests
import pandas as pd

# SWAPI endpoint for characters
url = "https://swapi.dev/api/people/"

response = requests.get(url)
data = response.json()

characters = data["results"]  # first 10
next_url = data["next"]       # get next page

# Fetch next page to make total 20 characters
if next_url:
    resp2 = requests.get(next_url).json()
    characters += resp2["results"]  # now total = 20

# Extract useful fields
rows = []
for c in characters:
    rows.append({
        "name": c["name"],
        "height": c["height"],
        "mass": c["mass"],
        "gender": c["gender"],
        "birth_year": c["birth_year"],
        "homeworld_url": c["homeworld"],
        "films_count": len(c["films"])
    })

df = pd.DataFrame(rows)

# Save to CSV
df.to_csv("swapi_characters.csv", index=False)

print("Done! Saved 20 characters to swapi_characters.csv")
