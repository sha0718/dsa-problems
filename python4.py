def move_zeroes(nums):
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums
print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

def find_peak(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
print(find_peak([1, 2, 3, 1]))  # Output: 3

import re
def valid_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]
print(valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True 

def two_sum(nums, target):
    seen = {}
    for i, val in enumerate(nums):
        if target - val in seen:
            return [seen[target - val], i]
        seen[val] = i
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print(has_cycle(Node(1)))  # Output: False

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
print(merge_lists(ListNode(1), ListNode(2)))  # Output: ListNode(1)

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node] - visited)
print(bfs({1: {2, 3}, 2: {4}, 3: {4}, 4: set()}, 1))  # Output: 1 2 3 4

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
print(dfs({1: {2, 3}, 2: {4}, 3: {4}, 4: set()}, 1))  # Output: 1 2 4 3

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
print(QueueUsingStacks().enqueue(1))  # Output: None
print(QueueUsingStacks().dequeue())  # Output: None

from collections import Counter
def find_duplicates(nums):
    count = Counter(nums)
    return [k for k, v in count.items() if v > 1]
print(find_duplicates([1, 2, 3, 4, 4, 5, 5]))  # Output: [4, 5]

