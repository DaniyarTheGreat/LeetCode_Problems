import collections

"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
"""
def numberOfIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    visit = set()
    islands = 0

    def bfs(r,c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and grid[r][c] == "1"
                and (r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c)
                islands+=1
    return islands