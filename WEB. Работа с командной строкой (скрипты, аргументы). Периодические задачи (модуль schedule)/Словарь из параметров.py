import sys

res = {}
if len(sys.argv) > 1:
    for i in sys.argv:
        if "=" in i:
            res[i.split("=")[0]] = i.split("=")[1]
    if "--sort" in sys.argv:
        res = dict(sorted(res.items(), key=lambda x: x[0]))

for key, value in res.items():
    print(f"Key: {key} Value: {value}")
