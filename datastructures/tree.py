# implementation of trees
# preorder
# post order
# in order ttraversal of trees

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# inorder traversal of tree 
# left root right
def inorder(root):
    result = []

    if root:
        inorder(root.left)
        print(root.data)
        result.append(root.data)
        inorder(root.right)
    return result

# preorder traversal of tree 
# root left right
def preorder(root):
    result = []

    if root:
        print(root.data)
        result.append(root.data)
        inorder(root.left)
        inorder(root.right)
    return result

# preorder traversal of tree 
# left right root
def postorder(root):
    result = []

    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.data)
        result.append(root.data)
    return result

if __name__ == '__main__':
    # initialization of a tree
    rootNode = TreeNode(1)
    leftNode = TreeNode(2)
    rightNode = TreeNode(3)

    rootNode.left = leftNode
    rootNode.right = rightNode
    print("===inorder traversal==")
    inorder(rootNode)
    print("===preorder traversal==")
    preorder(rootNode)
    print("===postorder traversal==")
    postorder(rootNode)





