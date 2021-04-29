"""
left view of a binary tree
    1
2       3
--> 1 2

    1
2       3
            6

--> 1 2 6

"""
from tree import TreeNode, inorder
maxlevel = 0
def left_view(root, level):
    # in a way we will be going pre
    # root left and right if left is null
    # at each level print only once
    global maxlevel
    if root:
        if maxlevel < level:
            print(root.data)
            maxlevel = level
        left_view(root.left, level+1)
        left_view(root.right, level+1)

    

    pass

if __name__ == "__main__":
    rootNode = TreeNode(1)
    firstNode = TreeNode(2)
    secondNode = TreeNode(3)
    thirdNode = TreeNode(6)
    rootNode.left = firstNode
    rootNode.right = secondNode
    secondNode.right = thirdNode
    # do a traversal to show all the nodes
    # inorder(rootNode) #works
    left_view(rootNode, level =1)
