# fun old heaps

class BinaryTree:
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        # root - left - right
        print(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preorder()
        if self.getRightChild():
            self.getRightChild().preorder()
    
    def postorder(self):
        # right - left - root
        if self:
            self.getRightChild().postorder()
            self.getLeftChild().postorder()
            print(self.getRootVal())
    
    def inorder(self):
        # left - root - right
        if self:
            self.getLeftChild().inorder()
            print(self.getRootVal())
            self.getRightChild().inorder()
            

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print("=============")
# can be accomplished through build tree
# user inserts a node and it keeps on inserting it to the three
def buildHeap():
    no_of_nodes = int(input())
    for i in range(no_of_nodes):
        print("\nNode -> : ")
        n = int(input())
        print("\nLeft -> 1 Right -> 0 : ")
        l = int(input())
        # this is going to take time
r = BinaryTree('10')
r.insertLeft('9')
r.insertRight('8')
s = r.getLeftChild()
s.insertLeft('7')
s.insertRight('6')
t = r.getRightChild()
r.getRight().getLeft().insertLeft('5')
r.insertLeft('4')
r.insertLeft('3')
r.insertLeft('2')
r.insertLeft('1')

# def min_heapify(A, i):
#     """
#     :Heapify function for min heaps
#     starts heapifying form i
#         - A - array
#     """
#     heap_size = len(A)

