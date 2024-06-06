def rob(nums):
    if len(nums) == 1:
        return nums[0]
    rec = [0,0]
    i,j = 0, 1
    while i < len(nums):
        rec[0] += nums[i]
        i+=2

    while j < len(nums):
        rec[1] += nums[j]
        j+=2 
    return max(rec)

print(rob([2,9,8,3,6]))