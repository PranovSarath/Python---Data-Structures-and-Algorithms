from typing import NewType
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, nodeValue=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next


    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        # result = 0
        # node = self.head
        # while node:
        #     result += 1
        #     node = node.next
        # return result
        values = len([str(x.value) for x in self])
        return values

    def add(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
        

if __name__ == '__main__':
    customLL = LinkedList()
    customLL.generate(10, 0, 99)
    print(customLL)
    print(len(customLL))
