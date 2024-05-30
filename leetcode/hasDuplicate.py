
# Retrun true if duplicate exist otherwise false
def hasDuplicate(nums):
    dic = {}
    for num in nums:
        if num in dic:
            return True
        dic[num] = num
    return False