# a program to print star pattern five times    
n = 5
for i in range(n):
    row = " "
    for j in range(n):
        row = row + " * "
    print(row)

# a program to print star pattern four times but in order 1 to 4
n = 4
for i in range(n):
    row = " "
    for j in range(i+1):
        row  = row + " * "
    print(row)

# a program to print number pattern five times but in order 1 to 5
n = 5 
for i in range(n):
    row = ""
    for j in range(i + 1):
        row = row + str(j + 1) + " "
    print(row)

# a program to print number pattern five times but in order 1 to 5 wiith succeding numbers        
n = 5 
for i in range(n):
    row = ""
    for j in range(i + 1):
        row = row + str(i + 1) + " "
    print(row)
        
# a program to print number pattern five times but in order 5 to 1 reverse order

n = 5 
for i in range(n):
    row = ""
    for j in range(n-i):
        row = row + str(j+ 1) + " "
    print(row)        

# a program to print star pattern five times but in order 5 to 1 reverse order
n = 5 
for i in range(n):
    row = ""
    for j in range(n-i):
        row = row + " * "
    print(row)   

n = 5
for i in range(n):
    row = ""
    for j in range(n-i-1):
        row = row + " ."
    for k in range(i+1):
        row = row + " * "
    print(row)

n = 5
for i in range(n):
    row = ""
    toggle = 1
    for j in range(i+1):
       row = row + str(toggle)
       if toggle == 1:
        toggle = 0
       else:
        toggle = 1
    print(row)

n = 5
toggle = 1
for i in range(n):
    row = ""
    for j in range(i+1):
       row = row + str(toggle)
       if toggle == 1:
        toggle = 0
       else:
        toggle = 1
    print(row)
