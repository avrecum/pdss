class List:
    def __init__(self):
        self.l = []

    def __repr__(self):
        return self.l.__repr__()

    def __str__(self):
        return self.l.__str__()

    def add_last(self, data):
        self.l.append(data)
        return self.l

    def add_first(self, data, index):
        self.l.insert(0, data)
        return self.l

    def add_before(self, data, index):
        self.l.insert(index, data)
        return self.l

    def add_after(self, data, index):
        self.l.insert(index+1, data)

    def remove(self, data):
        self.l.remove(data)

    def remove_all(self, data):
        self.l = filter(lambda a: a == data, self.l)
        return self.l

    def first_index_of(self, data):
        try:
            return self.l.index(data)
        except ValueError:
            return None

    def last_index_of(self, data):
        rev = self.l.reverse()
        try:
            rev_index = self.l.index(data)
            return len(rev) - 1 - rev_index
        except ValueError:
            return None

    def count(self, data):
        return self.l.count(data)

    def reverse(self, data):
        self.l.reverse()
        return self.l

    def sort(self):
        self.l.sort()
        return self.l

    def size(self):
        return len(self.l)
