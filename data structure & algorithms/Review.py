class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root

def minValue(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, target):
    if not root:
        return None
    
    if target > root.val:
        root.right = remove(root.right, target)
    elif target < root.val:
        root.left = remove(root.left, target)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            minVal = minValue(root.right)
            root.val = minVal.val
            root.right = remove(root.right, minVal)
    return root

def BST(arr, target):
    L, R = 0, len(target) - 1

    while L <= R:
        mid = (L+R) // 2
        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid -1
        else:
            return mid
    return -1

def bucketSort(arr):
    counts = [0] * len(arr)

    for n in arr:
        counts[n] += 1
    
    l = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            arr[l] = i
            l += 1

def quickSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s
    
    for i in range(s, e):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left], arr[i] = arr[i], temp
            left += 1
    
    arr[e] = arr[left]
    arr[left] = pivot

    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)

def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    m = (s + e) // 2

    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)
    merge(arr,s, m, e)


def merge(arr, s, m, e):
    L = arr[s: m+1]
    R = arr[m+1: e+1]

    i,j,k = 0,0,s

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    return arr
    
def kadanes(arr):
    maxSub = arr[0]
    currSub = 0

    for n in arr:
        currSub = max(currSub, 0)
        currSub += n
        maxSub = max(maxSub, currSub)
    return maxSub