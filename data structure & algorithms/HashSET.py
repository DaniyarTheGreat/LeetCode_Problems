class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HasSet:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None
    
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index = index + 1
            index = index % self.capacity

    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity *= 2
        old_map = self.map
        new_map = [None for pair in range(self.capacity)]
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair:
                self.put(pair.key, pair.val)
        