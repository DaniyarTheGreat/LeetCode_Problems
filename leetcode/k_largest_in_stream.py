class KthLargest:
    def __init__(self,k, nums):
        self.heap = []
        self.nums = nums
        self.heapify(nums)
        self.k = k
        

    def add(self, val):
        self.heapify(self.nums.append(val))
        return self.heap[self.k]

    def helper(self, i):
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i*2+1] > self.heap[i*2] and self.heap[i] < self.heap[i*2+1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2+1]
                self.heap[i*2+1] = temp
                i = i*2+1
            elif self.heap[i] < self.heap[i*2]:
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

kthLargest = KthLargest(3, [1, 2, 3, 3])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(6))
print(kthLargest.add(7))
print(kthLargest.add(8))