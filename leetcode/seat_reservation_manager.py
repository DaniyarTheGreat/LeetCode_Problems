# 1845 leetcode

class SeatManager:

    def __init__(self, n: int):
        self.minHeap = [i for i in range(n+1)]

    def reserve(self) -> int:
        if len(self.minHeap) == 2:
            return self.minHeap.pop()
        res = self.minHeap[1]
        self.minHeap[1] = self.minHeap.pop() 
        self.treverseDown(1)
        return res

    def unreserve(self, seatNumber: int) -> None:
        self.minHeap.append(seatNumber)
        i = len(self.minHeap) - 1
        self.treverseUp(i)

    def treverseDown(self, i : int):
        while i*2 < len(self.minHeap):
            if i*2+1 < len(self.minHeap) and self.minHeap[i*2+1] < self.minHeap[i*2] and self.minHeap[i] > self.minHeap[i*2+1]:
                temp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[i*2+1]
                self.minHeap[i*2+1] = temp
                i = i * 2 + 1
            elif self.minHeap[i] > self.minHeap[i*2]:
                temp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[i*2]
                self.minHeap[i*2] = temp
                i = i * 2
    
    def treverseUp(self, i):
        while i >= 1 and self.minHeap[i] < self.minHeap[i//2]:
            temp = self.minHeap[i]
            self.minHeap[i] = self.minHeap[i//2]
            self.minHeap[i//2] = temp
            i = i // 2