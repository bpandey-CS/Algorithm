# implementing stacks in pythonn
# opertions allowedd on stack
#    push 
#    pop
#    list all elements in a stack

class Stack:
    """
        opertions allowedd on stack
           push
           pop
           checkStack: list all elements in a stack
           checkTop : see the top element in the  stack
        >>> from datastructures import Stack
        >>> st = Stack() # empty stack
        >>> st = Stack([1,2,3,4,5,6]) # initializing non-empty stack
        >>> st.push(1)
        >>> st.pop()
        >>> st.checkStack()
        >>> st.checkTop()
    """
    def __init__(self, initval=[]):
        self.arr = initval

    def pop(self):
        # pop off the the last index element
        return self.arr.pop()
    
    def push(self, element):
        self.arr.append(element)
        return self.arr

    def checkStack(self):
        return self.arr
    
    def checkTop(self):
        return self.arr[-1]
    