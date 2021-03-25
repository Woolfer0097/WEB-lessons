import zipfile
import os
import json


count = 0
print(zipfile.ZipFile("input.zip"))
for root, dirs, files in os.walk(os.curdir):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as contact:
                data = json.load(contact)
                for dictionary in data:
                    if dictionary["city"] == "Москва":
                        count += 1
print(count)
