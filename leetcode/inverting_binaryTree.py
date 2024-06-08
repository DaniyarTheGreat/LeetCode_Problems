from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert_binary_tree(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    preOrder(root)

def preOrder(node: Node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

node_1 = Node("a")
node_2 = Node("b")
node_3 = Node("c")
node_4 = Node("d")
node_5 = Node("e")
node_6 = Node("f")
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_3.left = node_5
node_3.right = node_6

invert_binary_tree(node_1)
