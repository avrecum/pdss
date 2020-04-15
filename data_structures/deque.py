from collections import deque


class Deque:
    def __init__(self):
        self.d = deque()

    def __repr__(self):
        return str(self.d)

    def __str__(self):
        return str(self.d)

    def push_back(self, data):
        self.d.append(data)

    def push_front(self, data):
        self.d.appendleft(data)

    def pop_back(self):
        if self.d:
            return self.d.pop()
        return None

    def pop_front(self):
        if self.d:
            return self.d.popleft()
        return None

    def back(self):
        if self.d:
            return self.d[-1]
        return None

    def front(self):
        if self.d:
            return self.d[0]
        return None

    def reverse(self):
        self.d.reverse()
        return list(self.d)

    def size(self):
        return len(self.d)

    def rotate(self):
        self.d.rotate
        return list(self.d)

    def sort(self):
        self.d.sort()
        return list(self.d)

    def remove_first(self, data):
        self.d.remove(data)

    def remove_all(self, data):
        while self.d.__contains__(data):
            self.d.remove(data)

    def clear(self):
        self.d.clear()
        return list(self.d)
