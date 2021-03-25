import argparse


def count_lines(filename):
    try:
        with open(filename) as file:
            data = file.readlines()
        return len(data)
    except Exception:
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default="")

    args = parser.parse_args()
    print(count_lines(args.file))
