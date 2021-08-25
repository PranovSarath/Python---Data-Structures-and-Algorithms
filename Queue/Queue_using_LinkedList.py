class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.LinkedList.head == None:
            return "The queue is empty"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next 
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.LinkedList.head

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


customQueue = Queue()
customQueue.enqueue(10)
customQueue.enqueue(200)
customQueue.enqueue(599)
customQueue.enqueue(1000)
print(customQueue)

print(customQueue.isEmpty())
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())