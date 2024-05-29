def searchMatrix(matrix, target):
    row, L, R = 0, 0, 0
    for index in range(len(matrix)):
        if matrix[index][0] < target:
            row = index
            R = len(matrix[index]) - 1
        elif matrix[index][0] == target:
            return True
    while L <= R:
        mid = (L+R) // 2
        if target > matrix[row][mid]:
            L = mid + 1
        elif target < matrix[row][mid]:
            R = mid - 1
        else:
            return True
    return False