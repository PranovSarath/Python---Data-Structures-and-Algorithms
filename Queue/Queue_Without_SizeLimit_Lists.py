class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        value = [str(x) for x in self.items]
        return ' <- '.join(value)

    
    def isEmpty(self):
        if self.items == [] or self.items == None:
            return True
        return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element has been inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None
        return "The queue has been deleted"


customQueue = Queue()
print(customQueue.isEmpty())
print(customQueue.enqueue(4))
print(customQueue.enqueue(14))
print(customQueue.enqueue(23))
print(customQueue.enqueue(67))
print(customQueue.enqueue(99))
print(customQueue)

print(customQueue.dequeue())
print(customQueue)

print(customQueue.peek())
print(customQueue.delete())
print(customQueue.isEmpty)
print(customQueue.peek())



