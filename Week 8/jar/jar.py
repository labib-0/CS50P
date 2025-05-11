class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪"*self._size


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size

def main():
    cookis = Jar()
    cookis.deposit(9)
    cookis.withdraw(2)
    print(cookis)

if __name__ == "__main__":
    main()
