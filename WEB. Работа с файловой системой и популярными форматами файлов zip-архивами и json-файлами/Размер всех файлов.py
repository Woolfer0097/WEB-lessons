import os


def human_read_format(size):
    extensions = ["Б", "КБ", "МБ", "ГБ"]
    count = 0

    while size >= 1024:
        count += 1
        size /= 1024
    return f"{round(size)}{extensions[count]}"


def get_files_sizes():
    res = []
    files = [i for i in os.listdir() if os.path.isfile(i)]
    for file in files:
        res.append(f"{file} {human_read_format(os.path.getsize(file))}")
    return "\n".join(res)


if __name__ == '__main__':
    print(get_files_sizes())
