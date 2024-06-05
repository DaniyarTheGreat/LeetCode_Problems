def most_freq(nums, k):
    dic = {}
    res = []
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    for i in range(k):
        for key, val in dic.items():
            max_val = max(dic.values())
            if val == max_val:
                res.append(key)
                dic.pop(key)
                break
    return res

nums = [1,2,2,3,3,3]
k = 2

print(most_freq(nums, k))