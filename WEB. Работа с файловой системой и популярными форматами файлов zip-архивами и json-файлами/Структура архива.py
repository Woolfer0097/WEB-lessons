from zipfile import ZipFile


def zip_open(file):
    with ZipFile(file) as myzip:
        for file in myzip.filelist:
            name = file.filename
            if name[-1] == "/":
                print("  " * (name.count("/") - 1) + file.orig_filename.split("/")[-2])
            else:
                print("  " * (name.count("/")) + file.orig_filename.split("/")[-1])


if __name__ == '__main__':
    zip_open("input.zip")
