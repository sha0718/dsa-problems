# a program to reverse a string
# divide the string in half
# loop through the string
# swappping the characters
# return the reversed string

def reverseString(s):
    n = len(s)  # Use a different variable name
    half = n // 2
    for i in range(half):
        temp = s[i]
        s[i] = s[n - i - 1]
        s[n - i - 1] = temp
    return s

print(reverseString(["h", "e", "l", "l", "o"]))  # ['o', 'l', 'l', 'e', 'h']



