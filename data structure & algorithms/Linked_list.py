class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value
    
    def set_next_node(self, next_node):
        self.next_node = next_node

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


a = Node(5)
b = Node(1,a)
c = Node(90,b)
d = Node(32,c)
e = LinkedList(d)
print(e.stringfy_list())

a = LinkedList(2)
a.insert_beginning(3)
a.insert_beginning(4)
a.insert_beginning(5)
print(a.stringfy_list())