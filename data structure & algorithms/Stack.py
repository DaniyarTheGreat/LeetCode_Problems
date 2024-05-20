class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_ndoe(self):
        return self.next_node
    
    def set_next_node(self, next_ndoe):
        self.next_node = next_ndoe

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def has_space(self):
        return self.limit > self.size
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("No more space left!")
    
    def pop(self):
        pop_node = self.top_item
        if not self.is_empty():
            self.top_item = pop_node.get_next_ndoe()
            self.size -= 1
            return pop_node.get_value()
        else:
            print("Stack is empty!")

    def print_list(self):
        stack_list = []
        top = self.top_item
        while top:
            stack_list.append(top.get_value())
            top = top.get_next_ndoe()
        stack_list.reverse()
        print("stack: {0}".format(stack_list))