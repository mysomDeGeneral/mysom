# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Dict, Any

records = {}


class PhoneBook:

    def __init__(self):
        self.records = records

    def add(self, name, phone_number):
        self.records[len(self.records)] = {'name': name, 'phone': phone_number}

    def remove(self, name):
        for data in self.records:
            if name == self.records[data].get('name') or name == self.records[data].get('phone'):
                del self.records[data]
            else:
                print("Name not found!!!")

    def search(self, name):
        for data in self.records:
            if name == self.records[data].get('name') or name == self.records[data].get('phone'):
                for info in self.records[data]:
                    print(info.value)
                #   print(f"{name.capitalize()} - {self.records[name]}")


            else:
                print("Name not found!!!")

    def list(self):
        for name in self.records:
            print(f"{name.capitalize()} - {self.records[name]}")

    def num_of_records(self):
        return len(self.records)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys

    phone_book = PhoneBook()
    while True:

        print("_____PhoneBook_____")
        print("1. Add contact\n"
              "2. Search Contact\n"
              "3. Delete Contact\n"
              "4. View Contacts\n"
              "5. Exit\n")

        choice = int(input("--> "))

        if choice == 1:

            name = input("Name: ")
            contact = int(input("Phone No: "))
            phone_book.add(name, contact)

        elif choice == 2:
            name = input("Name: ")
            phone_book.search(f"{name}")

        elif choice == 3:
            name = input("Name: ")
            phone_book.remove(f"{name}")

        elif choice == 4:
            phone_book.list()

        elif choice == 5:
            sys.exit()

        else:
            print("Invalid input!!!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
