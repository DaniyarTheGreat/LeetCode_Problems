def removeDuplicate(nums):
    new_nums = set(nums)
    nums_lst = []
    for n in new_nums:
        nums_lst.append(n)
    return len(new_nums)

nums = [1, 1 ,2]
print(removeDuplicate(nums))
print(nums)