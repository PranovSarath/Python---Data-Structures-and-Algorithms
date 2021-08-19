#Stack with Size Limit

class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return "\t".join(values)

    #isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #push method
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
    #pop method
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()

    #peek emthod
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]

    def delete(self):
        self.list = []    

myStack = Stack(5)
myStack.push(1)
myStack.push(21)
myStack.push(16)
myStack.push(64)
print(myStack)
print(myStack.isFull())
myStack.push(104)
print(myStack.isFull())

myStack.push(256)
print(myStack)
print(myStack.peek())

myStack.pop()
print(myStack)

myStack.delete()
print(myStack)