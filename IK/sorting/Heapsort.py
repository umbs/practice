class Heap:

    heap_size = 0

    def __init__(self):
        pass

    def bubble(self, arr, idx):
        '''
        Bubble up the element at index idx to it's rightful place
        '''
        pass

    def heapified(self, arr, idx):
        '''
        Tells if an element at index idx satisfies heap property: node is
        smaller than it's children
        returns True or False
        '''
        pass

    def sink(self, arr, idx):
        '''
        Sink the element at index idx to it's right ful place
        '''
        pass

    def insert(self, arr, k):
        '''
        Insert an element K at the end and bubble up to right place
        '''
        Heap.heap_size += 1
        arr[Heap.heap_size] = k
        self.bubble(arr, Heap.heap_size)

    def look(self, arr):
        '''
        Get top element of the Heap
        '''
        return arr[1]

    def get_top(self, arr):
        '''
        Remove and return top element of the Heap
        '''
        sol = arr[1]
        self.bubble(arr, Heap.heap_size)
        Heap.heap_size -= 1

        return sol
