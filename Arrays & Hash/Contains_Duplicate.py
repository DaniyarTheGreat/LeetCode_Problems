class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # fastes one so far
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    # time limit exceeded
        # tuples = tuple(nums)
        # for num in tuples:
        #     if tuples.count(num) > 1:
        #         return True
        # return False

    # Works but not fast enough
        # set1 = set(nums)
        # if len(nums) > len(set1):
        #     return True
        # return False

    # time limit exceeded
        # for num in nums:
        #     if nums.count(num) > 1:
        #         return True
        # return False