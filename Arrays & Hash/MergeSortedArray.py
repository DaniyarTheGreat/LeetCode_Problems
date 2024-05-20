def merge(nums1, nums2, m, n):
    nums = []
    for i in range(m):
        nums.append(nums1[i])
    
    for i in range(n):
        nums.append(nums2[i])

    for i, num in enumerate(sorted(nums)):
        nums1[i] = num

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,nums2,3,3)
print(nums1)
