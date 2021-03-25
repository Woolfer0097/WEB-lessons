import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--sort', action="store_true")

args = parser.parse_args()
result_dict = {}
if args:
    for argument in args.arg:
        for (key, value) in [argument.split("=")]:
            result_dict[key] = value
    if args.sort:
        result_dict = sorted(result_dict.items(), key=lambda x: x[0])
        for (key, value) in result_dict:
            print(f"Key: {key}\tValue: {value}")
    else:
        for (key, value) in result_dict.items():
            print(f"Key: {key}\tValue: {value}")
