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
    adj_lst = {}
    graph_traversal(node, adj_lst, None)



def graph_traversal(node: Node, adj_lst, parent=None):
    if not node:
        return
    
    adj_lst[node] = []
    if parent:
        adj_lst[node.val].append(parent.val)
    if node.left:
        adj_lst[node.val].append(node.left.val)
    if node.right:
        adj_lst[node.val].append(node.right.val)
    
    graph_traversal(node.left, adj_lst, node)
    graph_traversal(node.right, adj_lst, node)


def k_distance(target, k, adj_lst):
    queue = deque
    visit = set()
    queue.append(target)
    visit.add(target)
    while queue and k > 0:
        for i in range(len(queue)):
            curr = queue.popleft()
            for nei in adj_lst[curr]:
                if nei not in visit and nei != target:
                    queue.append(nei)
                    visit.add(nei)
        k-=1
    return [queue.popleft() for n in queue]

