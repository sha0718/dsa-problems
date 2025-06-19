def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort([5, 4, 3, 2, 1])) # Output: [1, 2, 3, 4, 5]

def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
print(find_missing_number([1, 2, 4, 5]))  # Output: 3   

def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
print(is_balanced("{[()]}"))  # Output: True

from collections import Counter
def first_non_repeating(s):
    count = Counter(s)
    for c in s:
        if count[c] == 1:
            return c
    return None
print(first_non_repeating("aabbc"))  # Output: "b" 

from collections import defaultdict
def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams["".join(sorted(word))].append(word)
    return list(anagrams.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
print(MinStack().push(3))  # Output: None
print(MinStack().push(5))  # Output: None       
print(MinStack().get_min())  # Output: 3

import heapq
def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort([5, 2, 8, 1, 3]))  # Output: [1, 2, 3, 5, 8]

def rotate_list(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]



