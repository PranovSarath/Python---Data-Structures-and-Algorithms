#Implementing Stack using List
#Pros:
#Easy to implement
#Cons:
#Speed problem when it grows


#Implementing Stack without any size limit
#Can have performance leaks as size of list grows

class Stack:
    def __init__(self):
        self.list = []

    
    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\t'.join(values)

    #isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #push method
    def push(self, value):
        self.list.append(value)
        print("Inserting...")
        return "The element has been successfully inserted"
    
    #pop method
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            print("Popping....")
            return self.list.pop()

    #peek method
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]


customStack = Stack()
customStack.push(1)
customStack.push(4)
customStack.push(10)
customStack.push(11)
print(customStack)
customStack.pop()
print(customStack)
print(customStack.isEmpty())

print(customStack.peek())