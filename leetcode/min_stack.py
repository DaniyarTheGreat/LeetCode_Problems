class min_stack:
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)
    
    def pop(self):
        self.stack.pop()
        self.min.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min[-1]
    

obj = min_stack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())