def maxConsecutiveOnes(nums):
    count = 0 
    max_conut = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_conut = max(max_conut, count)
            count = 0
    return max(max_conut, count)    

print(maxConsecutiveOnes([1,1,0,1,1,1]))