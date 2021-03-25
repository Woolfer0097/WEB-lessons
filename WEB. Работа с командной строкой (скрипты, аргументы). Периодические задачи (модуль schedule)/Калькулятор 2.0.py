import sys


def calculator():
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            count = 0
            res = 0
            for i in sys.argv[1:]:
                if not i.isnumeric():
                    return "ValueError"
            numbers = [int(i.lstrip("0")) for i in sys.argv[1:] if i.replace(".", " ") == i]
            if len(numbers) != len(sys.argv[1:]):
                return "ValueError"
            else:
                for i in numbers:
                    if count % 2 == 0:
                        res += i * 1
                    else:
                        res += i * (-1)
                    count += 1
                return res
        else:
            return sys.argv[1]
    else:
        return "NO PARAMS"


if __name__ == '__main__':
    print(calculator())
