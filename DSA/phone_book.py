class PhoneBook(object):
    class Contact:
        __slots__ = 'name', 'phone_number'

        def __init__(self, n, p):
            self.name = n
            self.phone_number = p

        def __eq__(self, other):
            return self.name == other.name

        def list(self):
            return self.name + '-' + self.phone_number

    def __init__(self):
        self.record = []

    def __len__(self):
        return len(self.record)

    def get_contact(self, n):
        for data in self.record:
            if n == data.name:
                return data.name.capitalize() + '-' + data.phone_number
        return 'Name not found!!!'

    def add_contact(self, n, p):
        for data in self.record:
            if n == data.name:
                data.phone_number = p
                return
        self.record.append(self.Contact(n, p))

    def del_contact(self, n):
        for i in range(len(self.record)):
            if n == self.record[i].name:
                self.record.pop(i)
                return
        return 'Name not found!!!'

    def list_contacts(self):
        for i in range(len(self.record)):
            return self.record[i]



if __name__ == '__main__':
    p = PhoneBook()
    p.add_contact('mike', '545148108')
    p.add_contact('josh', '54523424')
    print(p.get_contact('mike'))
    print(p.get_contact('josh'))
    p.del_contact('mike')
    print(p.get_contact('mike'))
    print(p.list_contacts())
