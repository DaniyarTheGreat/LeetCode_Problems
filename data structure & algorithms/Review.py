class Heap:
    def __init__(self) -> None:
        self.heap = [0]
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        self.bubble_up(i)

    def remove(self):
        if (len(self.heap)) <= 1:
            return
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        self.bubble_down(1)
        return res

    def bubble_down(self, i):
        while i*2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i*2+1] < self.heap[i*2] and self.heap[i] > self.heap[i*2+1]:
                temp = self.heap[i*2+1]
                self.heap[i*2+1] = self.heap[i]
                self.heap[i] = temp
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i*2]:
                temp = self.heap[i*2]
                self.heap[i*2] = self.heap[i]
                self.heap[i] = temp
                i = i * 2
            else:
                break

    def bubble_up(self, i):
        while i >= 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i // 2

    def heapify(self, nums : list):
        nums.append(nums[0])
        self.heap = nums
        curr = ((len(self.heap)) - 1) // 2
        while curr > 0:
            i = curr
            self.bubble_down(i)
            curr -= 1

class Pair:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key

class Hash:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.hash = [None, None]

    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.hash[index] == None:
                self.hash[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.hash[index].key == key:
                self.hash[index].val = val
                return
            index += 1
            index = index % self.capacity
            
    def get(self,key):
        index = self.hash(key)
        while self.hash[index] != None:
            if self.hash[index].key == key:
                return self.hash[index].val
            index += 1
            index %= self.capacity
        return None
    
    def remove(self, key):
        if not self.get(key): 
            return
        
        index = self.hash(key)
        while True:
            if self.hash[index] == key:
                self.hash[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity
        
    def rehash(self):
        self.capacity *= 2
        old_map = self.hash
        new_map = [None] * self.capacity
        self.hash = new_map
        self.size = 0
        for pair in old_map:
            if pair:
                self.put(pair.key, pair.val)

    