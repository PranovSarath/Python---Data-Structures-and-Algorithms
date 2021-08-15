class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
    

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    #Creation of a doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The circular DLL is created successfully"

    
    #Insertion Method
    def insertToCDLL(self,value ,location):
        if self.head is None:
            return "The circular DLL does not exist"
        else:
            newNode = Node(value)
            #Insert Node in the front
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            #Insert node at the last location
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            #insert node at a given location
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    #Traversal function
    def traverseCDLL(self):
        if self.head is None:
            print("The circular DLL does not exist")
        else:
            tempNode = self.head
            print("Traversal started")
            while tempNode:
                print(tempNode.value, end='\t')
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            print("\nTraversal Complete")

    
    def reverseTraverseCDLL(self):
        if self.head is None:
            print("The circular DLL does not exist")
        else:
            tempNode = self.tail
            print("Reverse Traversal Started")
            while tempNode:
                print(tempNode.value, end='\t')
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
            print('\nReverse Traversal Complete')
        
    
    def searchCDLL(self, searchValue):
        if self.head is None:
            print("The circular DLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == searchValue:
                    return tempNode.value
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            return "There's no matching value in the Circular DLL"



    def deleteNodefromCDLL(self, location):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            #Delete node from first position
            if location == 0: #if node has only 1 element
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else: #if there are multiple elements
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            
            elif location == -1:   #if last node is to be deleted
                if self.head == self.tail: #if there's only one node
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:  #if there are multiple nodes
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            #if node at a particular location is to be deleted
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("Node has been successfully deleted")


    #Function to delete entire linked list
    def deleteEntireCDLL(self):
        if self.head is None:
            print("The circular DLL does not exist")
        else:
            tempNode = self.head
            self.tail.next = None
            while tempNode:
                tempNode.prev = None  
                tempNode = tempNode.next          
            self.head = None
            self.tail = None
        print("The Circular DLL has been deleted")



myCDLL = CircularDoublyLinkedList()
myCDLL.createCDLL(5)
print([node.value for node in myCDLL])

myCDLL.insertToCDLL(10,0)
print([node.value for node in myCDLL])
myCDLL.insertToCDLL(12,-1)
print([node.value for node in myCDLL])
myCDLL.insertToCDLL(300,2)
print([node.value for node in myCDLL])

myCDLL.traverseCDLL()
myCDLL.reverseTraverseCDLL()
print(myCDLL.searchCDLL(300))
print(myCDLL.searchCDLL(500))

print([node.value for node in myCDLL])
myCDLL.deleteNodefromCDLL(0)
print([node.value for node in myCDLL])
myCDLL.deleteNodefromCDLL(1)
print([node.value for node in myCDLL])
myCDLL.deleteNodefromCDLL(-1)
print([node.value for node in myCDLL])

myCDLL.deleteEntireCDLL()
print([node.value for node in myCDLL])