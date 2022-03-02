"""
Heap array creation
"""
import heapq
class minHeapq:

    def __init__(self, arr = None):
        self.heap = []
        self.FRONT = 1
        if arr is None:
            self.size = 0
        else:
            self.heap += arr
            self.size = len(arr) -1
            self.minHeap()
    def parent(self,pos):
        return pos//2

    def leftChild(self,pos):
        return pos * 2

    def rightChild(self, pos):
        return (pos * 2) + 1

    def isLeaf(self,pos):
        if (self.size// 2) <= pos and pos < self.size:
            return True
        else:
            return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]


    def maxHeapify(self, pos):     # _use of hiding function

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            lChild = self.leftChild(pos)
            rChild = self.rightChild(pos)
            if self.heap[lChild] < self.heap[rChild]:
                if self.heap[lChild] < self.heap[pos]:
                    self.swap(pos, lChild)
                    #self.minHeapify(lChild)
            else:
                if self.heap[rChild] < self.heap[pos]:
                    self.swap(pos,rChild)
                    #self.minHeapify(rChild)

    def minHeapify(self, pos):     # _use of hiding function
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            lChild = self.leftChild(pos)
            rChild = self.rightChild(pos)
            if self.heap[lChild] > self.heap[rChild]:
                if self.heap[rChild] < self.heap[pos]:
                    self.swap(pos, lChild)
                    #self.minHeapify(lChild)
            else:
                if self.heap[lChild] < self.heap[pos]:
                    self.swap(pos,rChild)
                    #self.minHeapify(rChild)

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    #Function for delete
    # delete only front element, swap with last element then heapify
    def Delete(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return  popped

    # Function to print the contents of the heap
    def Print(self,heap=None):
        if heap is None:
            heap = self.heap
            size = self.size
        else:
            size = len(heap) - 1
        for i in range(1, (size // 2) + 1):
            print(" PARENT : " + str(heap[i])
                  + " LEFT CHILD : " +  (str(heap[2 * i]) if (2*i) <= (size) else "")
                  + " RIGHT CHILD : " +  (str(heap[2 * i + 1]) if (2*i +1) <= (size) else " "))

    # Function to insert a node into the heap
    # Insert node to the end of the array,
    # check to parent if is less
    def Insert(self, val):
        self.size += 1
        self.heap.append(val)
        current = self.size
        # parent jabtak badh hai tabtak swap karte raho
        while self.heap[current] < self.heap[self.parent(current)] and current != 1:
            self.swap(current,self.parent(current))
            current = self.parent(current)


arr = [10,9,8,7,6,5,4,3,2,1]
arr1 = [10,9,8,7,6,5,4,3,2,1]
#arr = [1,2,3,4,5,6,7,8,9,10]
test = minHeapq(arr)
#print("Deleted item ", test.Delete())
test.Print()
#test.Insert(0)
print('@@@@@@@@@@@@@')
heapq.heapify(arr1)
test.Print(arr1)
