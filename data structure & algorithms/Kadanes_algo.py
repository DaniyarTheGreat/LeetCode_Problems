"""
Kadanes algorithm: uses a dynamic programming approach to calculate the maximum subarray sum ending at each position in the array

Base for two pointers and sliding window problems

For example:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""

def kadanes(arr):
    maxSum = arr[0]
    curSum = 0
    for n in arr:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

lst = [4,-1,2,-7,3,4]
print(kadanes(lst))
