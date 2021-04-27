# implementing stacks in pythonn
# opertions allowedd on stack
#    push 
#    pop
#    list all elements in a stack

class Queue:
    """
        opertions allowedd on stack
           enqueue
           dequeue
           checkQueue: list all elements in a Queue
           checkHead : see the Head element in the Queue
           checkTail : see the Tail element in the Queue
        >>> from datastructures import Queue
        >>> qu = Queue() # empty queue
        >>> qu = Queue([1,2,3,4,5,6]) # initializing non-empty queue
        >>> qu.enqueue(1)
        >>> qu.dequeue()
        >>> qu.checkQueue()
        >>> qu.checkTail()
        >>> qu.checkHead()
    """
    def __init__(self, initval=[]):
        self.arr = initval

    def dequeue(self):
        # pop off the the last index element
        self.arr = self.arr[1:]
        return self.arr
    
    def enqueue(self, element):
        self.arr.append(element)
        return self.arr

    def checkQueue(self):
        return self.arr
    
    def checkHead(self):
        return self.arr[0]
    
    def checkTail(self):
        return self.arr[-1]