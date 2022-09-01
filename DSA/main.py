class PhoneBook:
    """Phonebook implementation using Python dictionary as underlying storage"""

    def __init__(self):
        """Creates an empty Phonebook"""
        self.records = {}

    def add(self, contact_name, phone_number):
        """Adds a contact with name and phone number"""
        if len(contact_name.strip()) > 0 and len(phone_number.strip()) > 0:
            if len(phone_number) != 10:
                print('Invalid Phone number')
            else:
                self.records[contact_name] = phone_number
                print("Added successfully")
        else:
            print("No details entered!!!")

    def remove(self, contact_name):
        """Removes contact details of name provided"""
        if contact_name in self.records:
            del self.records[contact_name]
        else:
            print("Name not found!!!")

    def search(self, contact_name):
        """Returns contact details of the name provided"""
        if len(contact_name) > 0:
            if contact_name in self.records:
                print(f"{contact_name} - {self.records[contact_name]}")

            else:
                self.list_by_prefix(contact_name[:2])

    def list(self):
        """Returns record of all contacts in  alphabetical order""" # n * nlogn
        for key, value in sorted(self.records.items()):
            print(f"{key} - {self.records[key]}")

    def num_of_records(self):
        """Returns the number of contacts in the phonebook"""# 1
        if len(self.records) <= 0:
            return 'Phonebook is empty'
        elif len(self.records) == 1:
            return '1 contact'
        else:
            return f'{len(self.records)} contacts'

    def list_by_prefix(self, pre):
        for key, value in self.records.items():
            if key.startswith(f'{pre}'):
                print(f"{key} - {self.records[key]}")


if __name__ == '__main__':

    import sys

    phone_book = PhoneBook()

    while True:

        print("""                _______PhoneBook Directory_______
                1. Add contact
                2. Search Contact
                3. Delete Contact
                4. View Contacts by alphabets
                5. View all Contacts
                6. Number of Contacts
                7. Exit""")

        choice = input("--> ")

        if choice == '1':

            name = input("Name: ")
            contact = input("Phone No(eg.0544.....): ")
            phone_book.add(name, contact)
            n = input("Press Enter to continue...")

        elif choice == '2':
            name = input("Name: ")
            phone_book.search(name)
            n = input("Press Enter to continue...")

        elif choice == '3':
            name = input("Name: ")
            phone_book.remove(name)
            n = input("Press Enter to continue...")

        elif choice == '4':
            pre = input("Prefix: ")
            print("_____PhoneBook Directory_____")
            phone_book.list_by_prefix(pre)
            n = input("Press Enter to continue...")

        elif choice == '5':
            print("_____PhoneBook Directory_____")

            phone_book.list()
            n = input("Press Enter to continue...")

        elif choice == '6':
            print(phone_book.num_of_records())
            n = input("Press Enter to continue...")

        elif choice == '7':
            sys.exit("Thanks for using our service, Bye!")

        else:
            print("Invalid option!!!")
            n = input("Press Enter to continue...")
