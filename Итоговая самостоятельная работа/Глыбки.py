import requests
import json


def horklump(address, port, **kwargs):
    # response = requests.get(f"http://{address}:{port}")
    # data = response.json()
    with open("test.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    if kwargs["place"] in data.keys():
        data[kwargs["place"]].append(dict((key, value)
                                          for key, value in kwargs.items()
                                          if key in list(kwargs.keys())[1:]))
    else:
        data[kwargs["place"]] = [dict((key, value)
                                      for key, value in kwargs.items()
                                      if key in list(kwargs.keys())[1:])]
    return json.dumps(data, indent="\t", ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    print(horklump("127.0.0.1", 5000, place="France", weight=13, count=3))
    print(horklump("127.0.0.1", 5000, place="England", color="blue", magic="high"))
