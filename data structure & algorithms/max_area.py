def maxAreaOfIsland(grid):
    max_area = 0
    visit = set()
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r,c):
        if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visit:
            return 0
        
        visit.add((r,c))
        area = 1
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        for dr, dc in directions:
            area += dfs(r+dr,c+dc)
        return area

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visit:
                max_area = max(dfs(r,c), max_area)

    return max_area

box=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
print(maxAreaOfIsland(box))