class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return '🍪'*self.size

    def deposit(self, n):
        self.size += n


    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Capacity must be non-negative')
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError('Size must be non-negative')
        if size > self.capacity:
            raise ValueError('Size must be less than or equal to capacity')
        self._size = size


def main():
    jar = Jar()
    print(f"{jar} cokies")
    jar.deposit(1)
    print(f"{jar} cokies")
    jar.deposit(11)
    print(f"{jar} cokies")
    jar.withdraw(1)
    print(f"{jar} cokies")
    jar.withdraw(10)
    print(f"{jar} cokies")
    jar.withdraw(1)
    print(f"{jar} cokies")
    print("ERROR")
    jar.withdraw(5)

if __name__ == '__main__':
    main()