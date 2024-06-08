
# leetcode 42 hard
def trap(height: list[int]) -> int:
    l,r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    res = 0
    while l < r:
        if maxL < maxR:
            l+=1
            maxL = max(maxL, height[l])
            res += maxL - height[l]
        else:
            r-=1
            maxR= max(maxR, height[r])
            res += maxR - height[r]
    return res