def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))  # Output: True

def find_max_min(lst):
    return max(lst), min(lst)
print(find_max_min([3, 1, 4, 1, 5, 9]))  # Output: (9, 1)

def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1
print(linear_search([1, 2, 3, 4, 5], 3))  # Output: 2   

from collections import Counter
def frequency_count(lst):
    return dict(Counter(lst))
print(frequency_count([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}

def merge_sorted_lists(a, b):
    return sorted(a + b)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2] if len(lst) >= 2 else None
print(second_largest([3, 1, 4, 1, 5, 9]))  # Output: 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))  # Output: 120

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  # Output: True

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop() if self.stack else None
print(Stack().push(1))  # Output: None
print(Stack().pop())  # Output: None












