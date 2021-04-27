class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
#initiation of linked list
headNode = LinkedList(1)
secondNode = LinkedList(2)
thirdNode = LinkedList(3)

headNode.next = secondNode
secondNode.next = thirdNode

# iterate through the linked list
curNode = headNode
while curNode:
    print(curNode.data)
    curNode = curNode.next

# insert new listnode with value of 5 in between the seconfnode and thirdnode
curNode = headNode
while curNode.data != 2:
    curNode= curNode.next
newNode = LinkedList(5)
newNode.next = curNode.next
curNode.next = newNode

# iterate through the linked list
curNode = headNode
while curNode:
    print(curNode.data)
    curNode = curNode.next

# remove the listnode with value of 5
curNode = headNode
while curNode.next.data != 5:
    curNode = curNode.next

curNode.next = curNode.next.next

# iterate through the linked list
curNode = headNode
while curNode:
    print(curNode.data)
    curNode = curNode.next
