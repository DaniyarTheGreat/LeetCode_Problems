"""
Repeatedly remove duplicate unitll we can't

"""
from collections import deque

def rem(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# print(rem(""))


def removal(s, k):
    dic = {}
    for char in s:
        dic[char] = 1 + dic.get(char, 0)
        if dic[char] == k:
            dic[char] -= k
    string = ''
    for key, val in dic.items():
        for n in range(val):
            string += key

    return string

print(removal("deeedbbcccbdaa", 3))


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def bfs(node: Node, target: int, k: int):
    count = 1


def postorder(root: Node, res: list, count: int):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)