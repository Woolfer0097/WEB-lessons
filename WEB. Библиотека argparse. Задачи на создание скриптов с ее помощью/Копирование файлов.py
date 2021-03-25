import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--upper', action="store_true")
parser.add_argument('--lines', nargs='?', default=99999999)

args = parser.parse_args()
if args:
    data = []
    import_file, export_file = args.arg[0], args.arg[1]
    with open(import_file, "r") as file:
        data_temp = file.readlines()
    if int(args.lines) > len(data_temp):
        data = data_temp
    else:
        with open(import_file, "r") as file:
            for i in range(int(args.lines)):
                data.append(file.readline())
    if args.upper:
        data = [i.upper() for i in data]
    with open(export_file, "w") as file:
        file.writelines(data)
