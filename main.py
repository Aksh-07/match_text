import os
all_files_list = os.listdir("all_files/")


def store_data():
    dict1 = {}
    for files in all_files_list:
        with open(f"all_files/{files}", "r") as d:
            dict1[d.name] = d.read().replace("\n", " ")

    return dict1


data = store_data()


def search(txt):
    for key, value in data.items():
        if txt in value:
            n = value.count(txt)
            print(f"Match Found in {key}, Total Occurences: {n}")
        else:
            print(f"Sorry, No Match Found in {key}")


while True:
    s = input("Enter text to search: ")

    if s == "quit":
        break
    else:
        search(s)






