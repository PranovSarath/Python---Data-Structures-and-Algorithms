from LinkedList import LinkedList, Node

def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False
    
    len1 = len(ll1)
    len2 = len(ll2)

    shorter = ll1 if len1 < len2 else ll2
    longer = ll2 if len1 < len2 else ll1

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode



#Helper addition method
def addSameNode(ll1, ll2 , value):
    tempNode = Node(value)
    ll1.tail.next = tempNode
    ll1.tail = tempNode

    ll2.tail.next = tempNode
    ll2.tail = tempNode


llA = LinkedList()
llA.generate(3,0,10)

llB = LinkedList()
llB.generate(3,0,10)

addSameNode(llA,llB, 11)
addSameNode(llA,llB, 14)
addSameNode(llA,llB, 21)

print(llA)
print(llB)

print(intersection(llA,llB))


llX = LinkedList()
llX.generate(10,0,100)

llY = LinkedList()
llY.generate(10,0,100)

print(llX)
print(llY)

print(intersection(llX,llY))
