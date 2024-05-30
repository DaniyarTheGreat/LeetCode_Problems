class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i // 2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.head) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.helper(i=1)
        return res
    
    def helper(self, i):
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i*2+1] < self.heap[i*2] and self.heap[i] > self.heap[i*2+1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2+1]
                self.heap[i*2+1] = temp
                i = i*2+1
            elif self.heap[i] > self.heap[i*2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = temp
                i = i*2
            else:
                break
    
    def heapify(self, nums):
        nums.append(nums[0])
        self.heap = nums
        curr = ((len(self.heap)) - 1) // 2
        while curr > 0:
            i = curr
            self.helper(i)
            curr -= 1
        
