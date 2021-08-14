class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #insert in LinkedList
    def insertToSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        #if SLL is not empty 
        else:
            #if insertion is in first position
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            #if insertion is in the last position
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            #if insertion is in a given location
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    index += 1
                    tempNode = tempNode.next
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                #if given location is the last node
                if tempNode == self.tail:
                    self.tail = newNode




singlyLinkedList = SLinkedList()
singlyLinkedList.insertToSLL(1,1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertToSLL(2,-1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertToSLL(10,-1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertToSLL(-80,-1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertToSLL(3,2)

print([node.value for node in singlyLinkedList])