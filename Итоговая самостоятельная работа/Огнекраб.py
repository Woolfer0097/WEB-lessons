import csv
from flask import Flask
import json
import argparse

app = Flask(__name__)


parser = argparse.ArgumentParser()
parser.add_argument('--server', nargs='?', default="127.0.0.1")
parser.add_argument('--port', nargs='?', default="5050")
parser.add_argument('--file', nargs='?', default="error")

args = parser.parse_args()

host, port = args.server, args.port
file = args.file


@app.route("/firecrab")
def return_json():
    with open("crabs.csv", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar=' ')
        rows = list(reader)
        result = {}
        for info in rows:
            if info["color"] not in result.keys():
                result[info["color"]] = [sorted([int(info["shell thickness"]), int(info["size"])], reverse=True)]
            else:
                result[info["color"]].append(sorted([int(info["shell thickness"]), int(info["size"])], reverse=True))
                result[info["color"]] = sorted(result[info["color"]], key=lambda x: x[1], reverse=True)
                result[info["color"]] = sorted(result[info["color"]], key=lambda x: x[0], reverse=True)
    return json.dumps(result, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    app.run(port=port, host=host)
