import os
all_files_list = os.listdir("all_files/")

s = input("Enter text to search: ")


def search(txt):
    for files in all_files_list:
        n = 0
        with open(f"all_files/{files}", "r") as data:
            data_list = data.readlines()
            for line in data_list:
                if txt in line:
                    n += 1
        print(f"In file {data.name} total no of matches for searched string: {n}")


search(s)


