# 515 leetcode

from collections import deque
class TreeNode:
    pass

def largestValues(self, root: TreeNode | None) -> list[int]:
    if not root:
        return
    queue = deque()
    visit = []
    queue.append(root)
    while queue:
        local_max = []
        for i in range(len(queue)):
            curr = queue.popleft()
            local_max.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        visit.append(max(local_max))
    return visit