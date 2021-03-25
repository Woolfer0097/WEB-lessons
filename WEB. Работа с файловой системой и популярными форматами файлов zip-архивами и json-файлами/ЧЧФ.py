def human_read_format(size):
    extensions = ["Б", "КБ", "МБ", "ГБ"]
    count = 0

    while size >= 1024:
        count += 1
        size /= 1024
    return f"{round(size)}{extensions[count]}"


if __name__ == '__main__':
    print(human_read_format(1023))
