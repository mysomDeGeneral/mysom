class PhoneBook:
    """Phonebook implementation using dictionary as storage"""

    def __init__(self):
        """Creates an empty Phonebook"""
        self.records = {}

    def add(self, contact_name, phone_number):
        """Adds a contact with name and phone_number"""
        self.records[contact_name] = phone_number

    def remove(self, contact_name):
        """Removes a contact from the phonebook if the name provided matches a data"""
        if contact_name in self.records:
            del self.records[contact_name]
        else:
            print("Name not found!!!")

    def search(self, contact_name):
        """Returns a contact details if the name provided matches a data in the phonebook"""
        if contact_name in self.records:
            print(f"{contact_name.capitalize()} - {self.records[contact_name]}")
        else:
            print("Name not found!!!")

    def list(self):
        """Returns record of all contacts in the phonebook"""
        for data in sorted(self.records):
            print(f"{data.capitalize()} - {self.records[data]}")

    def num_of_records(self):
        """Returns the number of contacts in the phonebook"""
        return len(self.records)


if __name__ == '__main__':
    import sys

    phone_book = PhoneBook()  # Creates a  new phonebook when the script is run

    while True:

        print("_____PhoneBook_____")
        print("1. Add contact\n"
              "2. Search Contact\n"
              "3. Delete Contact\n"
              "4. View Contacts\n"
              "5. Number of Contacts\n"
              "6. Exit\n")

        choice = input("--> ")

        if choice == '1':

            name = input("Name: ")
            contact = input("Phone No: ")
            phone_book.add(name, contact)

        elif choice == '2':
            name = input("Name: ")
            phone_book.search(name)

        elif choice == '3':
            name = input("Name: ")
            phone_book.remove(name)

        elif choice == '4':
            phone_book.list()

        elif choice == '5':
            print(phone_book.num_of_records())

        elif choice == '6':
            sys.exit("Thanks for using our service, Bye!")

        else:
            print("Invalid input!!!")
