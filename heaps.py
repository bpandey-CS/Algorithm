import math

class Heap():
    """
        The majestic heaps
    """

    def __init__(self):
        self.array = [] # actual heaps
        self.size = 0 # heap size
    
    def insertElement(self, key):
        self.array.append(key) # just an array that appends
        self.size = self.size + 1
        return True
    
    def insertElements(self, elements: list):
        self.array.extend(elements) # just an array that appends
        self.size = self.size + len(elements)
        return True
    
    def minHeapify(self, i):
        left_child = 2*i + 1
        right_child = 2*i + 2
        smallest = i
        if(left_child < self.size and self.array[left_child] < self.array[smallest]):
            smallest = left_child
        if(right_child < self.size and  self.array[right_child] < self.array[smallest]):
            smallest = right_child
        if smallest != i:
            self.array[smallest], self.array[i] = self.array[i], self.array[smallest]
            self.minHeapify(smallest)
        
    def buildMinHeap(self):
        for i in range(math.floor(self.size/2)-1, -1, -1):
            self.minHeapify(i)
    
    def insertMinHeap(self, key):
        # increase will be on similar grounds
        self.insertElement(key)
        i = self.size-1
        while(i>0 and self.array[i//2] > self.array[i]):
            self.array[i//2], self.array[i] = self.array[i], self.array[i//2]
            i = i//2

    def extractMin(self):
        if not self.size:
            return "Heap Underflow"
        key = self.array[0]
        self.array[0], self.array[self.size-1] = self.array[self.size-1], self.array[0]
        self.size = self.size - 1
        self.minHeapify(0)
        return key

    def heapSort(self):
        self.buildMinHeap()
        for i in range(self.size-1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.size = self.size-1
            self.minHeapify(0)
        return self.array