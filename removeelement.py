# a program to remove an element from an array
# the element to be removed is 2
# used two pointer approach to remove the element
# return the new length of the array

def removeElement(nums,val):
    x = 0 
    for i in range(len(nums)):
        if nums[i] != val:
         nums[x] = nums[i]
         x = x + 1   
    return x 


print(removeElement([0,1,2,2,3,0,4,2],2))

