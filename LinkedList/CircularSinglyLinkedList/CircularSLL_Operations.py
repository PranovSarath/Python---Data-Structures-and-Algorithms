from typing import NewType


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            

    def createCSLL(self, nodeValue): #++++++> O(1)
        node = Node(nodeValue)  
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    #insert in LinkedList
    def insertToCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            #Insert in first spot
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            
            #insert in last spot
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode
        return "The node has been successfully executed"    

    
    def traversalCSLL(self):
        if self.head is None:
            print("The circular SLL does not exist")

        else:
            tempNode = self.head
            location = 0
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, searchValue):
        if self.head is None:
            print("The CSLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == searchValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "the node does not exist in the CSLL"

    def deleteNodeFromCSLL(self, location):
        if self.head is None:
            print("The CSLL does not exist")
        else:
            #Deleting node from beginning
            if location == 0: #if there's only one node in the CSLL
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: #if there are multiple nodes
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1: #Deleting an element from the last position
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: 
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    

    def deleteEntireCSLL(self):
        self.tail.next = None
        self.head = None
        self.tail = None

            


circularSinglyLinkedList = CSLinkedList()
circularSinglyLinkedList.createCSLL(1)
print([node.value for node in circularSinglyLinkedList])
circularSinglyLinkedList.insertToCSLL(2,0)
print([node.value for node in circularSinglyLinkedList])
circularSinglyLinkedList.insertToCSLL(10,-1)
print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.insertToCSLL(-80,-1)

print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.insertToCSLL(3,2)

print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.traversalCSLL()
print(circularSinglyLinkedList.searchCSLL(-80))
print(circularSinglyLinkedList.searchCSLL(-90))

circularSinglyLinkedList.deleteNodeFromCSLL(0)
print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.deleteNodeFromCSLL(2)
print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.deleteNodeFromCSLL(-1)
print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.deleteEntireCSLL()
print([node.value for node in circularSinglyLinkedList])

