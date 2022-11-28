import tkinter
import os
from secret import admin, data
from random import choice
from tkinter import messagebox


items = []
local_list = []
h_dir = os.path.expanduser('~')
path = h_dir + "\\RewardCollector"
list_path = os.path.join(path, "listy.txt")


def verify_key(key: str) -> bool:  # FULL WORKING DO NOT TOUCH
    query = admin.find()
    count = 0

    for item in query:
        while IndexError:
            try:
                l = item["lisence"][count][0]
                if key in l:
                    if user_verify(key):
                        return True
                count += 1
            except IndexError:
                return False


def user_verify(key: str) -> bool:
    query = data.find_one({"licence": f"{key}"})
    try:
        if query["uuid"] == str:
            return False
    except TypeError:
        return True


def generate_keys(count: int):  # FULL WORKING
    try:
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        l = []
        for i in range(0, count):
            tmp = ((choice(alphabets) + choice(numbers) + choice(alphabets) + choice(numbers)) + "-" +
                   choice(alphabets) + choice(numbers) + choice(alphabets) + choice(numbers) + "-" +
                   choice(alphabets) + choice(numbers) + choice(alphabets) + choice(numbers) + "-" +
                   choice(alphabets) + choice(numbers) + choice(alphabets) + choice(numbers) + "-" +
                   choice(alphabets) + choice(numbers) + choice(alphabets) + choice(numbers)
                   )
            l.append(tmp)

        admin.update_one({"user": "admin"}, {"$push": {"lisence": [l]}})
        return l
    except tkinter.TclError:
        messagebox.showerror("Error", "Value must be numeric")


def download_list():
    query = admin.find_one({"user": "admin"})
    global items
    items = query["item_list"][0]


def checkforupdate_list():
    query = admin.find_one({"user": "admin"})
    read_local_list()
    try:
        if query["item_list"][0][0] == local_list[0]:
            pass
        if query["item_list"][0][::-1] == local_list[::-1]:
            pass
        else:
            create_text()
    except IndexError:
        create_text()


def read_local_list():
    try:
        with open(list_path, "r") as l:
            # read lines and add to list
            while True:
                line = l.readline()
                if not line:
                    break
                local_list.append(line.strip())
    except FileNotFoundError:
        create_text()


def create_text():
    if not os.path.exists(path):
        os.mkdir(path)
    download_list()
    with open(list_path, "w") as file:
        for i in range(len(items)):
            file.write(f"{items[i]}\n")
        file.close()


