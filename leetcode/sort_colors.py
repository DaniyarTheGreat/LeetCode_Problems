def sort(nums):
    colors = [0,0,0]
    for n in nums:
        colors[n] += 1
    
    i = 0
    for n in range(len(colors)):
        for j in range(colors[n]):
            nums[i] = n
            i+=1