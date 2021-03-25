import json
import sys


tests = [i.strip("\n") for i in sys.stdin.readlines()]
count = 0

with open('scoring.json') as file:
    data = json.loads(file.read())
    for i in range(1, len(tests) + 1):
        if tests[i - 1] == 'ok':
            for score in data["scoring"]:
                if i in score["required_tests"]:
                    count += score["points"] // len(score["required_tests"])

print(count)
