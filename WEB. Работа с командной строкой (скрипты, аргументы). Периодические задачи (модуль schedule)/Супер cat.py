import sys
import os

try:
    for i in sys.argv:
        if os.path.splitext(i)[1] == ".txt":
            filename = i
    with open(filename, "r") as file:
        data = [i.strip("\n") for i in file.readlines()]
    if len(sys.argv) > 1:
        row_count = len(data)
        if "--sort" in sys.argv:
            data.sort()
        if "--num" in sys.argv:
            if "--count" in sys.argv:
                for i in range(row_count):
                    print(f"{i} {data[i]}")
                print(f"rows count: {row_count}")
            else:
                for i in range(row_count):
                    print(f"{i} {data[i]}")
        elif "--count" in sys.argv:
            for i in range(row_count):
                print(data[i])
            print(f"rows count: {row_count}")
        else:
            for i in range(row_count):
                print(data[i])
except Exception:
    print("ERROR")
