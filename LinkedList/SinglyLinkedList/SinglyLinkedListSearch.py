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


    #Searching for a value in Singly Linked List
    def searchSLL(self, searchValue):
        if self.head is None:   #+++++++++++++> O(1)
            print("The SLL does not exist")
        else:
            tempNode = self.head
            while tempNode is not None: #+++++++++++++> O(1)
                if tempNode.value == searchValue: #+++++++> O(n)
                    return tempNode.value
                tempNode = tempNode.next #++++++++++> O(1)
            return "The value does not exist in this list"
    




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
print(singlyLinkedList.searchSLL(10))