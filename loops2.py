#  create a function named search element
# that takes an array and an element as parameters
# use for loop foer iteration
# return index of the element in the array
# if the element is not found, return -1

def searchElement(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1, 2, 9, 4, 15,22,34]
print(searchElement(arr , 22)) # Output: 5 searching an element in an array 


# create a function named countnegative
# that takes an array as a parameter
# use for loop for iteration
# return the count of negative elements in the array

def countnegative(arr):
    count = 0 
    for i in range(len(arr)):
        if arr[i] < 0:
            count += 1
    return count


arr = [1, -2, 9, -4, 15, -22, 34]
print(countnegative(arr)) # Output: 3 counting negative elements in an array


# create a function named findLargest
# that takes an array as a parameter
# largest = array first element
# use for loop for iteration
# assign the current element to largest
# update the largest variable if the current element is greater than the current largest

def findLargest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr = [1, 2, 9, 4, 15,22,34]
print(findLargest(arr)) # Output: 34 finding the largest element in an array

def findSmallest(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr = [1, 2, 9, 4, 15,22,34]
print(findSmallest(arr)) # Output: 1 finding the smallest element in an array
                    


