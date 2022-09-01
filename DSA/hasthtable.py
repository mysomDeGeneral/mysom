class HashTable:
    def __int__(self,size):
        self.values = size * [None]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is None:
            raise KeyError(key)
        return value

    



