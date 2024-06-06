from collections import deque
class Node:
    def __init__(self, float, unit):
        self.float = float
        self.unit = unit


def graph_populate(facts: list, adj_lst: dict):
    for (left_unit, number, right_unit) in facts:
        if left_unit not in adj_lst:
            adj_lst[left_unit] = Node(number, right_unit)
        
def answer_query(query, facts):
    adj_lst = {}
    graph_populate(facts, adj_lst)
    queue = deque()
    visit = set()
    queue.append(query[0][0])
    visit.add(query[0][0])

    for (num, root, target) in query:
        curr = queue.popleft()
        
