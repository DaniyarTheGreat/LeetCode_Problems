# # insertion sort O(n^2)
# def sort(nums):
#     for i in range(len(nums)):
#         j = i - 1
#         while j>=0 and nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#             j-=1
#     return nums
    
# nums = [5,2,3,1]
# sort(nums)
# print(nums)


def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr

# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
arr = [5, 2, 1, 3]
print(mergeSort(arr, 0, 4))

# def mergeSort(arr):
#     if len(arr) == 1:
#         return arr

#     arr_1 = arr[0:len(arr)//2]
#     arr_2 = arr[(len(arr)//2)+1:len(arr)]

#     mergeSort(arr_1)
#     mergeSort(arr_2)

#     return merge(arr_1, arr_2)

# def merge(arr_1, arr_2):
#     arr_3 = []

#     while arr_1 and arr_2:
#         if arr_1[0] > arr_2[0]:
#             arr_3.append(arr_2[0])
#             arr_2.remove(arr_2[0])
#         else:
#             arr_3.append([arr_1[0]])
#             arr_1.remove(arr_1[0])

#     while arr_1:
#         arr_3.append(arr_1[0])
#         arr_1.remove(arr_1[0])

#     while arr_2:
#         arr_3.append(arr_2[0])
#         arr_2.remove(arr_2[0])

#     return arr_3

# arr = [5,2,1,3]
# mergeSort(arr)
# print(arr)

