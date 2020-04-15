class Set:
    def __init__(self):
        self.s = set()

    def __repr__(self):
        return str(list(self.s))

    def __str__(self):
        return str(list(self.s))

    def contains(self, data):
        return data in self.s

    def is_empty(self):
        return len(self.s) == 0

    def size(self):
        return len(self.s)

    def add(self, data):
        self.s.add(data)

    def union(self, other):
        return list(self.s.union(other.s))

    def apply_union(self, other):
        self.s = self.s.union(other.s)
        return list(self.s)

    def intersection(self, other):
        return list(self.s.intersection(other.s))

    def apply_intersection(self, other):
        self.s = self.s.intersection(other.s)
        return list(self.s)

    def difference(self, other):
        return list(self.s.difference(other.s))

    def apply_difference(self, other):
        self.s = self.s.difference(other.s)
        return list(self.s)

    def symmetric_difference(self, other):
        return list(self.s.symmetric_difference(other.s))

    def apply_symmetric_difference(self, other):
        self.s = self.s.symmetric_difference(other.s)
        return list(self.s)

    def is_subset(self, other):
        return self.s.issubset(other.s)

    def is_superset(self, other):
        return self.s.issuperset(other.s)

    def remove(self, data):
        self.s.remove(data)
        return list(self.s)
