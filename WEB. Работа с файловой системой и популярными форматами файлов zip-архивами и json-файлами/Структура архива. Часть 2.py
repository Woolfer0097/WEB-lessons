from zipfile import ZipFile
import os


def human_read_format(size):
    extensions = ["Б", "КБ", "МБ", "ГБ"]
    count = 0

    while size >= 1024:
        count += 1
        size /= 1024
    return f"{round(size)}{extensions[count]}"


def zip_open(file):
    with ZipFile(file) as myzip:
        for file in myzip.filelist:
            name = file.filename
            if name[-1] == "/":
                print(f"{'  ' * (name.count('/') - 1)}{file.orig_filename.split('/')[-2]}")
            else:
                print(f"{'  ' * (name.count('/'))}{file.orig_filename.split('/')[-1]} "
                      f"{human_read_format(file.file_size)}")


if __name__ == '__main__':
    zip_open("input.zip")
