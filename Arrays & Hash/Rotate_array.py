def rotate(nums, k):
    first_part = []
    second_part = []
    for i in range(0, k + 1):
        first_part.append(nums[i])
    
    for i in range(k + 1, len(nums)):
        second_part.append(nums[i])

    second_part.extend(first_part)
    for i,num in enumerate(second_part):
        nums[i] = num

nums = [1 ,2 ,3 ,4, 5, 6, 7]
# rotate(nums, k=3)
print(nums[:])

