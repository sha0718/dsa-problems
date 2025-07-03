# a program to find sum of array using recursion

arr = [5,3,2,0,1]

def sum(n):
    if n == 0:
        return arr[0]
    return arr[n] + sum(n-1)

print(sum(4))

# a program to find sum of odd elements of array using recursion

arr = [5, 3, 2, 0, 1, 9]

def sum_odd_elements(n):
    if n < 0:
        return 0
    return (arr[n] if arr[n] % 2 != 0 else 0) + sum_odd_elements(n - 1)

print(sum_odd_elements(len(arr) - 1))


