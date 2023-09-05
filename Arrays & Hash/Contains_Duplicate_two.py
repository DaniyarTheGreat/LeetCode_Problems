    
def containsNearbyDuplicate(nums,k):
  dic = {}
  for i in range(len(nums)):
    if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
      return True
    dic[nums[i]] = i
  return False

print(containsNearbyDuplicate([1,2,3,1,2,3],2))