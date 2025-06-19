# Write a Python function to check whether a number is a palindrome or not.

def palindrome_number(n):
    rev = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    if rev == n:
        return True
    else:
        return False
print(palindrome_number(7127))       
