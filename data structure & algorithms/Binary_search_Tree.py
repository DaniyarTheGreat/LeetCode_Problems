from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root

def minValue(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minVal = minValue(root.right)
            root.val = minVal.val
            root.right = remove(root.right, minVal)
    return root

# in, pre, post are all DFS
# prints the tree inorder -- 2 , 3 , 4 , 5 , 6, 7 where 4 is the root 
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# prints the root first then left tree, finally right 4, 3, 2, 6, 5, 7
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# left tree then right lastly the root
def postorder(root):
    if not root:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

# Back tracking
# if there's a path from root to leaf where no 0 is included
def canReachLeaf(root):
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False

# back tracking
# finds the path from root to leaf where no 0 is included
def pathFinder(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if pathFinder(root.left, path):
        return True
    if pathFinder(root.right, path):
        return True
    path.pop()
    return False    