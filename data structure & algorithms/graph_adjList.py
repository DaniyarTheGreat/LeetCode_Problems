from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.bfs(self.graph, src, dst)

    def bfs(self, graph, src, dst):
        visit = set()
        visit.add(src)
        queue = deque()
        queue.append(src)
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True
                for place in graph[curr]:
                    if place not in visit:
                        visit.add(place)
                        queue.append(place)
        return False
