def remove_ele(nums, val):
    for i in range(len(nums)):
        if nums[i] != val:
            continue
        for j in range(i+1, len(nums)):
            if nums[j] == val:
                continue
            else:
                nums[i] = nums[j]
                nums[j] = val
                break
    count = 0                
    while val in nums:
        nums[nums.index(val)] = '_'
        count += 1
    return len(nums) - count

nums = [3,2,2,3]
print(remove_ele(nums, 3))
print(nums)

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k