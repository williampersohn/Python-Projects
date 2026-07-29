class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._number = 0

    def __str__(self):
        cookies = ""
        for _ in range(self._number):
            cookies += "🍪"
        return cookies
    def deposit(self, n):
        if self._number + n > self._capacity:
            raise ValueError
        self._number += n


    def withdraw(self, n):
        if self._number - n < 0:
            raise ValueError
        self._number -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._number
