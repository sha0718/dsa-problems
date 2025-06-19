# Write a python program to find the second largest number in an array

# create a function name second largest that takes an array as a parameter
#  if len(arr) < 2:
#     return -1
# we can assign largest = arr[0] and secondlargest = arr[0]
# use for loop for iteration
# we can compare the current element to largest after that we can compare the current element to secondlargest
# update the secondlargest variable if the current element is greater than the current secondlargest
# return secondlargest

def secondLargest(arr):
    if len(arr) < 2:
        return -1
    largest = arr[0]
    secondlargest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i] > secondlargest:
            secondlargest = arr[i]
    return secondlargest

arr = [1, 2, 9, 4, 15,22,21]
print(secondLargest(arr))  

# Write a python program to find the second smallest number in an array

# create a function name second smallest that takes an array as a parameter
#  if len(arr) < 2:
#     return -1
# we can assign smallest = arr[0] and secondsmallest = arr[0]
# use for loop for iteration
# we can compare the current element to smallest after that we can compare the current element to secondsmallest
# update the secondsmallest variable if the current element is smaller than the current secondsmallest
# return secondsmallest

def secondSmallest(arr):
    if len(arr) < 2:
        return -1
    smallest = arr[0]
    secondsmallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            secondsmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondsmallest:
            secondsmallest = arr[i]
    return secondsmallest

arr = [3, 2, 9, 4, 15,22,21]
print(secondSmallest(arr))