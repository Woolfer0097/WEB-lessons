import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')

args = parser.parse_args()
if args.arg:
    print("\n".join(args.arg))
else:
    print("no args")
