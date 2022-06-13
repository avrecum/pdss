class Stack:
    def __init__(self):
        self.l = []

    def get(self):
        return self.l

    def __str__(self):
        return str(self.l)

    def __repr__(self):
        return str(self.l)

    def push(self, item):
        self.l.append(item)

    def pop(self):
        try:
            return self.l.pop()
        except IndexError:
            return None

    def peek(self):
        try:
            return self.l[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.l)
