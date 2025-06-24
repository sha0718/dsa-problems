# first aproach to find single number in an array

from collections import defaultdict

def singleNumber(nums):
    hash = defaultdict(int)
    for i in range(len(nums)):
        if not hash[nums[i]]:
            hash[nums[i]] = 1
        else:
            hash[nums[i]] += 1
    for i in range(len(nums)):
        if hash[nums[i]] == 1:
            return nums[i]
        
print(singleNumber([4,1,2,1,2]))        

# second aproach to find single number in an array using xor operation

def singleNumbers(nums):
    xor = 0
    for x in range(len(nums)):
        xor ^= nums[x]
    return xor

print(singleNumbers([6,1,2,1,2]))


