def missingNumbers(nums):
    n = len(nums) 
    totalSum = n * (n + 1) // 2
    sum = 0 
    numbers = []
    for i in range(n):
        sum = sum + nums[i]
    return totalSum - sum
    
    


print(missingNumbers([0,1, 2, 3, 4, 6, 7, 8, 9, 10]))    

