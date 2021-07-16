class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = MaxHeap()
        self.minHeap = MinHeap()

    def addNum(self, num: int) -> None:
        # 大顶堆先进一个元素
        self.maxHeap.push(num)
        # 然后从大顶堆里出一个元素到小顶堆
        max_in_maxHeap = self.maxHeap.pop()
        self.minHeap.push(max_in_maxHeap)
        if self.maxHeap.size() < self.minHeap.size():
            # 如果大顶堆的元素少于小顶堆
            # 就要从小顶堆出一个元素到大顶堆
            self.maxHeap.push(self.minHeap.pop())

    def findMedian(self) -> float:
        if self.maxHeap.size() == self.minHeap.size():
            return (self.maxHeap.peak_top() + self.minHeap.peak_top()) / 2
        else:
            return self.maxHeap.peak_top()


class BinaryHeap():
    def __init__(self):
        self.heap = []

    def leftChild(self, i):
        return 2*i+1
    
    def rightChild(self, i):
        return 2*i + 2
    
    def parent(self, i):
        return (i-1)//2

    def size(self):
        return len(self.heap)

    def peak_top(self):
        return self.heap[0]
    
    def swap(self, id1, id2):
        # print(f"self.heap: {self.heap}, id1: {self.heap}, id2: {id2}")
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]
        
class MaxHeap(BinaryHeap):
    def __init__(self):
        # self.maxHeap = []
        BinaryHeap.__init__(self)
    
    # def swap(self, id1, id2):
    #     # print(f"self.heap: {self.heap}, id1: {self.heap}, id2: {id2}")
    #     self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]
        
    def push(self, node):
        self.heap.append(node)
        j = len(self.heap)-1
        while j > 0:
            fa = self.parent(j)
            if self.heap[j] > self.heap[fa]:
                self.swap(fa, j)
                j = fa
            else:
                break

    def pop(self):
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        j = 0
        flagDone = False
        while flagDone!= True:
            largest = j
            leftChild = self.leftChild(largest)
            rightChild = self.rightChild(largest)
            if leftChild < self.size() and self.heap[leftChild] > self.heap[largest]:
                largest =leftChild
            if rightChild < self.size() and self.heap[rightChild] > self.heap[largest]:
                largest =rightChild
            if largest != j:
                self.swap(largest, j)
                j = largest
            else:
                flagDone = True
        
        return ans

class MinHeap(BinaryHeap):
    def __init__(self):
        self.heap = []
        # BinaryHeap.__init__(self)
        
    def push(self, node):
        self.heap.append(node)
        j = len(self.heap)-1
        while j > 0:
            fa = self.parent(j)
            if self.heap[j] < self.heap[fa]:
                self.swap(fa, j)
                j = fa
            else:
                break

    def pop(self):
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        j = 0
        flagDone = False
        while flagDone!= True:
            largest = j
            leftChild = self.leftChild(largest)
            rightChild = self.rightChild(largest)
            if leftChild < self.size() and self.heap[leftChild] < self.heap[largest]:
                largest =leftChild
            if rightChild < self.size() and self.heap[rightChild] < self.heap[largest]:
                largest =rightChild
            if largest != j:
                self.swap(largest, j)
                j = largest
            else:
                flagDone = True
        
        return ans

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()