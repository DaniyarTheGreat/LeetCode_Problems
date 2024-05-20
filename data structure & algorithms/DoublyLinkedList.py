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

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        new_node = Node(value)
        current_node= self.head
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
        if self.head is not None:
            self.head.set_prev_node(None)
        if current_head == self.tail:
            self.remove_tail()
        return current_head.get_value()

    def remove_tail(self):
        current_tail = self.tail
        if current_tail is None:
            return None
        self.tail = current_tail.get_prev_node()
        if self.tail is not None:
            self.tail.set_next_node(None)
        if current_tail == self.head:
            self.remove_head()
        return current_tail.get_value()

    # Bidirection, might throw AttributeError when list only has 1 node
    def remove_by_value(self,value):
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
        return removed_node
    
    # Easy solution, Single direction
    def remove_by_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.get_value() == value:
                if current_node == self.head:
                    self.remove_head()
                elif current_node == self.tail:
                    self.remove_tail()
                else:
                    next_node = current_node.get_next_node()
                    prev_node = current_node.get_prev_node()
                    next_node.set_prev_node(prev_node)
                    prev_node.set_next_node(next_node)
                return current_node
            current_node = current_node.get_next_node()
        return None
    
    def stringfy_list(self):
        string_list = ""
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
# subway = DoublyLinkedList()
# subway.add_to_head("Times Square")
# subway.add_to_head("Grand Central")
# subway.add_to_head("Central Park")
# print(subway.stringfy_list())
# subway.add_to_tail("Penn Station")
# subway.add_to_tail("Wall Street")
# subway.add_to_tail("Brooklyn Bridge")
# print(subway.stringfy_list())
# subway.remove_head()
# subway.remove_tail()
# print(subway.stringfy_list())
# subway.remove_by_value("Times Square")
# print(subway.stringfy_list())            
