# write a python program to reverse an integer both positive and negative 

def reverseInteger(n):
    temp = n     
    rev = 0
    n = abs(n)
    while n > 0:
        last = n % 10
        rev = 10*rev + last 
        n = n // 10
    if temp > 0:
        return rev
    else:
        return -rev

print(reverseInteger(1123))

