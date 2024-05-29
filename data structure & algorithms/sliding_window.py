# Return the left and right indexs of the maximum subarray

def sliding_window(arr):
    maxSum = arr[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(arr)):
        if curSum < 0:
            curSum = 0
            L = R
        curSum += arr[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R
    return [maxL, maxR]