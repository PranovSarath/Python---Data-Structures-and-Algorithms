class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        return "The Doubly Linked List is created successfully"
    
    #Insertion operation on a doubly linked list
    def insertNodeDLL(self, nodeValue, location):
        #Checking if DLL is empty
        if self.head is None: #++++++++++> O(1)
            print('The node cannot be inserted')
        else:
            newNode = Node(nodeValue)
            #Inserting node in the first position
            if location == 0:  #+++++++++> O(1)
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            #Insert an element in the last position
            elif location == -1: #+++++++++> O(1)
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            #Insert in any given location
            else: 
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode = tempNode.next #+++++++++> O(n)
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    def traversal(self):
        if self.head is None:
            print("There is no element to traverse")
        else:
            print("Traversal")
            tempNode = self.head
            while tempNode:
                print(tempNode.value, end='\t')
                tempNode = tempNode.next
            print()

    def reverse_traversal(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            print("Reverse Traversal")
            tempNode = self.tail
            while tempNode:
                print(tempNode.value, end='\t')
                tempNode = tempNode.prev
            print()

    def searchDLL(self, searchVal):
        if self.head is None:
            return "The doubly linked list does not exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == searchVal:
                    return tempNode.value
                tempNode = tempNode.next
            return "The value cannot be found in the DLL"

    
    def deleteNodeDLL(self, location):
        if self.head is None:
            print("The Doubly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            #to delete node from the end
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print('The node has been successfully deleted')


    #delete the entire DLL
    def deleteEntireDLL(self):
        if self.head is None:
            print("The DLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
            



            
            
            
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
print([node.value for node in doublyLL])
doublyLL.insertNodeDLL(0, 0)
print([node.value for node in doublyLL])
doublyLL.insertNodeDLL(2,-1)
print([node.value for node in doublyLL])
doublyLL.insertNodeDLL(6,2)
print([node.value for node in doublyLL])

doublyLL.traversal()
print("--------------------------------")
doublyLL.reverse_traversal()

print(doublyLL.searchDLL(6))
print(doublyLL.searchDLL(150))

print([node.value for node in doublyLL])

doublyLL.deleteNodeDLL(0)
print([node.value for node in doublyLL])

doublyLL.deleteNodeDLL(1)
print([node.value for node in doublyLL])

doublyLL.deleteNodeDLL(-1)
print([node.value for node in doublyLL])

doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])
