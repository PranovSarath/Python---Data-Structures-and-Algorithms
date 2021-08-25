class CircularQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top == self.maxSize-1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue"


    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

    
    def peek(self):
        if self.isEmpty():
            return "The circular queue is empty"
        else:
            return self.items[self.start]

                


customQueue = CircularQueue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())

print(customQueue.enqueue(3))
print(customQueue.enqueue(10))
print(customQueue.enqueue(17))
print(customQueue.enqueue(99))
print(customQueue)

print(customQueue.isFull())
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())

print(customQueue.delete())
print(customQueue)
print(customQueue.isEmpty())

    