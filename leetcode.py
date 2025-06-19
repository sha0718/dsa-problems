# Write a python program to reverse an array

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))

# Write a python program to find the maximum and minimum element in an array

def find_max_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    return max_element, min_element

arr = [5, 8, 3, 9, 2]
print(find_max_min(arr))

# Write a python program to search an element in an array

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [4, 2, 7, 1, 9]
key = 7
index = linear_search(arr, key)
print(index)

# Write a python program to find the duplicates in an array

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))

# Write a python program to find the subarray with the largest sum

def subarray_sum(arr, target_sum):
    current_sum = arr[0]
    start = 0
    for end in range(1, len(arr) + 1):
        # Shrink window if current_sum > target_sum
        while current_sum > target_sum and start < end - 1:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            print("Subarray found from index", start, "to", end - 1)
            return True
        if end < len(arr):
            current_sum += arr[end]
    print("No subarray found")
    return False

arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
subarray_sum(arr, target_sum)


