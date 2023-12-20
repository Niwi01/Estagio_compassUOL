import json

with open("person.json", "r") as f:
    data = json.load(f)
print(data)