class Node:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

    def get_value(self):
        return self.value
    
    def get_prev_node(self):
        return self.prev
    
    def get_next_node(self):
        return self.next
    
    def set_next_node(self, next):
        self.next = next

    def set_prev_node(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringfy_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    def remove_node(self, remove_value):
        current_node = self.get_head_node()
        if current_node.get_value() == remove_value:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == remove_value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        current_node = self.head
        if current_node is not None:
            current_node.set_prev_node(new_node)
            new_node.set_next_node(current_node)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        current_node = self.tail
        if current_node is not None:
            current_node.set_next_node(new_node)
            new_node.set_prev_node(current_node)
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def remove_head(self):
        current_head = self.head
        if current_head is None:
            return None
        self.head = current_head.get_next_node()
        if current_head is not None:
            self.head.set_prev_node(None)
        if current_head == self.tail:
            self.remove_tail()
        return current_head.get_value()
    
    def remove_tail(self):
        current_tail = self.tail
        if current_tail is None:
            return None
        self.tail = current_tail.get_prev_node()
        if current_tail is not None:
            self.tail.set_next_node(None)
        if current_tail == self.head:
            self.remove_head()
        return current_tail.get_value()
    
    def remove_by_value(self, value):
        removed_node = None
        current_head = self.head
        current_tail = self.tail
        while (current_head is not None) or (current_tail is not None):
            if current_head.get_value() == value:
                removed_node = current_head
                break
            elif current_tail.get_value() == value:
                removed_node = current_tail
                break
            current_tail = current_tail.get_prev_node()
            current_head = current_head.get_next_node()
        if removed_node is None:
            return None
        if removed_node == self.head:
            self.remove_head()
        elif removed_node == self.tail:
            self.remove_tail()
        else:
            next_node = removed_node.get_next_node()
            prev_node = removed_node.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

class Queue:
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()
        
    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        else:
            print("Nothing to see here!")
    
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.tail = item_to_add
                self.head = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("No more space!")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            if self.get_size() == 1:
                self.head, self.tail = None, None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Queue is empty now!")

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
        print("Nothing to see here")

    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("No more space left")

    def pop(self):
        pop_node = self.top_item
        if not self.is_empty():
            self.top_item = pop_node.get_next_node()
            self.size -= 1
            return pop_node.get_value()
        else:
            print("Stack is empty")

    def print_list(self):
        stack_lst = []
        top = self.top_item
        while top:
            stack_lst.append(top.get_value())
            top = top.get_next_node()
        stack_lst.reverse()

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions
    