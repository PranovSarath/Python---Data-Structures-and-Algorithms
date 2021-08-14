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
        if self.head is None: #++++++++++++> O(1)
            self.head = newNode
            self.tail = newNode
        #if SLL is not empty 
        else:
            #if insertion is in first position
            if location == 0:
                newNode.next = self.head #++++++++> O(1)
                self.head = newNode
            #if insertion is in the last position
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode #++++++++++> O(1)
                self.tail = newNode
            #if insertion is in a given location
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    index += 1
                    tempNode = tempNode.next  #+++++++++++> O(n)
                nextNode = tempNode.next
                tempNode.next = newNode  #+++++++++++++>O(1)
                newNode.next = nextNode
                #if given location is the last node
                if tempNode == self.tail:
                    self.tail = newNode
        

    #Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:           #+++++++> O(1)
            print('The Singly Linked List does not exist')
        else:
            tempNode = self.head #+++++++++++++> O(1)
            while tempNode is not None:
                print(tempNode.value) #++++++++++> O(n)
                tempNode = tempNode.next

    #Delete node
    def deleteNode(self, location):
        if self.head is None:     #+++++++++> O(1)
            print("The SLL does not exist")
        else:
            #Delete the first node
            if location == 0:
                if self.head == self.tail:
                    self.head = None #+++++++++> O(1)
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail: #+++++++++> O(1)
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail: #+++++++> O(n)
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next #+++++++> O(n)
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    #Delete entire SLL
    def deleteEntireSLL(self):  #++++++++++> O(1)
        if self.head is None:
            print("The SLL does not exist")
        else:
            print("Deleting entire SLL")
            self.head = None
            self.tail = None

            

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

singlyLinkedList.traverseSLL()

singlyLinkedList.deleteNode(3)
print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])