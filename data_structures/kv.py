class KV:
    def __init__(self):
        self.d = dict()

    def __repr__(self):
        return str(self.d)

    def __str__(self):
        return str(self.d)

    def set(self, key, value):
        self.d[str(key)] = value

    def get(self, key):
        try:
            return self.d[str(key)]
        except KeyError:
            return None

    def size(self):
        return len(d)

    def remove(self, key):
        try:
            self.d[str(key)] = None
            return None
        except KeyError:
            return None
