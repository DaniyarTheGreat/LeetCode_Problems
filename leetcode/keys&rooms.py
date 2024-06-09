from collections import deque
# 841 leetcode

def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    queue = deque()
    visit = set()
    queue.append(0)
    visit.add(0)
    while queue:
        for j in range(len(queue)):
            curr = queue.popleft()
            for key in rooms[curr]:
                if key not in visit:
                    queue.append(key)
                    visit.add(key)
    return len(visit) == len(rooms)