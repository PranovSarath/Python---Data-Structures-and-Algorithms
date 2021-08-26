#Create stack with a min method
#operating in O(1) time complexity

class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string
    
class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value

    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value , next = self.minNode )
        else:
            self.minNode = Node(value = item , next = self.minNode)
        self.top = Node(value = item, next = self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


CustomStack = Stack()
CustomStack.push(14)
print(CustomStack.min())
CustomStack.push(20)
print(CustomStack.min())
CustomStack.push(3)
print(CustomStack.min())
CustomStack.push(6)
print(CustomStack.min())

CustomStack.pop()
print(CustomStack.min())
CustomStack.pop()
print(CustomStack.min())
CustomStack.pop()
print(CustomStack.min())


    
