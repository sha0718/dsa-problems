def moveZeroes(nums):
    x = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[x] = nums[i]  # Move non-zero to front
            x += 1
    for i in range(x, len(nums)):
        nums[i] = 0  # Fill remaining with zeros
    return nums

print(moveZeroes([0,1,0,3,12]))
