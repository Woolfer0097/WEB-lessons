import json
import csv

with open("magic_help.json", "r", encoding="utf-8") as file:
    data = json.load(file)

creatures = []

for creature in data:
    if creature["hide"] > 10:
        creatures.append(creature)
creatures = sorted(creatures, key=lambda dictionary: dictionary["hide"], reverse=True)

with open("hide_and_seek.csv", "w", newline='') as csvfile_write:
    writer = csv.DictWriter(
        csvfile_write, fieldnames=list(data[0].keys()),
        delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for creature in creatures:
        writer.writerow(creature)
