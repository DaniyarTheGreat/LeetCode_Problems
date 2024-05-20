def removeDuplicates(nums):
    for num in nums:
        while nums.count(num) > 1:
            nums.remove(num)
    print(nums)

nums = [1,1,2]
removeDuplicates(nums)

