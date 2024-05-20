def major_element(nums):
    count = 0
    the_num = 0
    for num in nums:
        if nums.count(num) > count:
            the_num = num
            count = nums.count(num)
    return the_num

nums = [3,3,4]
print(major_element(nums))