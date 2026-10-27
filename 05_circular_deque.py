class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.data[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.capacity
        self.data[tail] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


if __name__ == "__main__":
    q = MyCircularDeque(3)
    print([q.insertLast(1), q.insertLast(2), q.insertFront(3),
           q.insertFront(4), q.getRear(), q.isFull(),
           q.deleteLast(), q.insertFront(4), q.getFront()])
    # [True, True, True, False, 2, True, True, True, 4]
