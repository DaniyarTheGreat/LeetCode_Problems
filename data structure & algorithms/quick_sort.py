def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left], arr[i] = arr[i], temp
            left+=1

    arr[e] = arr[left]
    arr[left] = pivot

    quick_sort(arr, s, left-1)
    quick_sort(arr, left+1, e) 


arr = [6, 2, 1, 4, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)