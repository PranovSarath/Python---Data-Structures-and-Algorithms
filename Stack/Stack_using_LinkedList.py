#Stack implementation using LinkedList
#Pros:
#Fast Performance
#cons:
#Implementation is not as easy as using list.

from typing import Counter


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next
    

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    #isEmpty method
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    #push method
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peep(self):
        if self.isEmpty():
            return "There is no value in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None



customStack = Stack()
print(customStack.isEmpty())
customStack.push(3)
customStack.push(31)
customStack.push(133)
customStack.push(321)
print(customStack)

customStack.pop()
print(customStack)

print(customStack.peep())
customStack.delete()

print(customStack)

    
