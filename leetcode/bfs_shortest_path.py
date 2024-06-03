import collections

def orangesRotting(grid: list[list[int]]) -> int:
    fresh = 0
    ROWS, COLS = len(grid), len(grid[0])
    rotted = set()
    queue = collections.deque()
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 2:
                rotted.add((i,j))
                queue.append((i,j))
            elif grid[i][j] == 1:
                fresh += 1
            j += 1
    second = 0
    while queue and fresh > 0:
        for i in range(len(queue)):
            r, c = queue.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if (min(new_r,new_c) < 0 or new_r == ROWS or new_c == COLS
                or (new_r,new_c) in rotted or grid[new_r][new_c]==0):
                    continue
                rotted.add((new_r, new_c))
                queue.append((new_r, new_c))
                fresh -= 1
        second += 1
    return second if fresh == 0 else -1


grid=[[2,1,1],[1,1,1],[0,1,2]]
print(orangesRotting(grid))
