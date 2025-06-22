# a program to reverse a string
# divide the string in half
# loop through the string
# swappping the characters
# return the reversed string

def reverseString(s):
    len = len(s)
    half = len // 2
    for i in range(half):
        s[i], s[len - i - 1] = s[len - i - 1], s[i]
    return s

print(reverseString(["h","e","l","l","o"]))


