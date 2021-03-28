import sys


data = sys.stdin.readlines()
for raw_string in data:
    string = raw_string.strip("\n")
    while string.count("A") >= 5 or string.count("Y") >= 3:
        string = string.replace("YYY", "A", 1)
        string = string.replace("AAA", "Y", 1)
    print(string)
