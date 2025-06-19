def longest_palindrome(s):
    n = len(s)
    result = ""
    for i in range(n):
        for j in range(i, n):
            temp = s[i:j+1]
            if temp == temp[::-1] and len(temp) > len(result):
                result = temp
    return result
print(longest_palindrome("babad"))  # Output: "bab" or "aba"

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
print(LRUCache(2).put(1, 1))  # Output: None

import heapq
def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances
print(dijkstra({1: {2: 1, 3: 4}, 2: {3: 2, 4: 5}, 3: {4: 1}, 4: {}}, 1))  # Output: {1: 0, 2: 1, 3: 3, 4: 4}    

def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
print(has_cycle({1: [2], 2: [3], 3: [1]}))  # Output: True

def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]
print(find_median_sorted_arrays([1, 3], [2]))  # Output: 2.0

def lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4   

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, TrieNode())
        curr.end = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end
print(Trie().insert("hello"))  # Output: None

import heapq
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)
print(MinHeap().push(5))  # Output: None

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
            grid[r][c] = "0"        
            for x, y in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r+x, c+y)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1
    return count
print(num_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Output: 3

def max_subarray(nums):
    max_sum = curr = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)
        max_sum = max(max_sum, curr)
    return max_sum
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

