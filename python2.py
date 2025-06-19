class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, val):
        self.queue.append(val)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
    
print(Queue().enqueue(1))  # Output: None
print(Queue().dequeue())  # Output: None    

def digit_sum(n):
    return sum(int(d) for d in str(n))
print(digit_sum(123))  # Output: 6

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  # Output: True

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fibonacci(10)  # Output: 0 1 1 2 3 5 8

def common_elements(a, b):
    return list(set(a) & set(b))
print(common_elements([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 3, 3]))  # Output: [1, 2, 3]

def custom_len(s):
    count = 0
    for _ in s:
        count += 1
    return count
print(custom_len("hello"))  # Output: 5

def exists(lst, val):
    return val in lst
print(exists([1, 2, 3], 2))  # Output: True

def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
print(largest_word("Find the largest word in this sentence"))  # Output: "sentence"

def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))  # Output: "olleh"

