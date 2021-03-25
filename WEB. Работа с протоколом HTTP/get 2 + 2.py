import requests


address = input()
port = input()
a = input()
b = input()

response = requests.get(f"{address}:{port}")
data1 = response.json()
print(*sorted([i for i in data1]))
print([i for i in data1["check"]])
