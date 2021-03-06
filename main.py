import os
all_files_list = os.listdir("all_files/")


def store_data():
    # store data in memory to avoid opening/closing of file for every new search
    files_data = {}
    for files in all_files_list:
        with open(f"all_files/{files}", "r") as d:
            files_data[d.name] = d.read().replace("\n", " ").lower()  # case-insensitive matching
            d.close()
    return files_data


data = store_data()


def search(txt):
    for key, value in data.items():
        print(f"Match Found in {key}, Total Occurrences: {value.count(txt)}")\
            if txt in value else print(f"Sorry, No Match Found in {key}")


while True:
    s = input("Enter text to search: ").lower()  # case in-sensitive matching
    if s == "quit":
        break
    search(s)






