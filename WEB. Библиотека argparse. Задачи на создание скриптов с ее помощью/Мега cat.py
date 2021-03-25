import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--count', action="store_true")
parser.add_argument('--num', action="store_true")
parser.add_argument('--sort', action="store_true")

args = parser.parse_args()
try:
    if args:
        result_data = []
        filename = args.arg[-1]
        with open(filename, "r") as file:
            data = [i.strip("\n") for i in file.readlines()]
        row_count = len(data)
        for i in range(row_count):
            result_data.append(data[i])
        if args.sort:
            result_data.sort()
        if args.count:
            result_data.append(f"rows count: {row_count}")
        if args.num:
            for i in range(row_count):
                result_data[i] = f"{i} {result_data[i]}"
        print("\n".join(result_data))

except Exception:
    print("ERROR")
