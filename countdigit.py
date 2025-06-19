def count_digit(n):
    if n == 0:
        return 1
# coverts negative number to positive
    
    n = abs(n)
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

print(count_digit(-356))

