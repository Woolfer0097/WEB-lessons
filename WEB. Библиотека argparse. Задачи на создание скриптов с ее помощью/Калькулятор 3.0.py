import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')

try:
    args = parser.parse_args()
    if args.arg:
        if len(args.arg) == 2:
            print(sum([int(i) for i in args.arg]))
        elif len(args.arg) < 2:
            print("TOO FEW PARAMS")
        elif len(args.arg) > 1:
            print("TOO MANY PARAMS")
    else:
        print("NO PARAMS")

except Exception as exception:
    print(exception.__class__.__name__)
