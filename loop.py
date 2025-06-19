
# a program to print n natual number ?

# input = n number
# 1 wiil be starting point 
# n + 1 will be ending point
# increment by 1 
# loop continues to run till the condition is true


n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(i)

# a program to create multiplication table

#  input = n number
# n will be multiplied by i 
# after that mmultiplication table will be printed


n = int(input("Enter a number: "))

for i in range(1, 11):  
   print(n, "x", i, "=", n*i)

# print a table from 1  to n where tables are printed from 1:10
# input = n number 
# double for loops are used 
# i will be multiplied by j
# n will be multiplied by i
# after that multiplication table will be printed

n = int(input("Enter a number: "))

for i in range(1, 11):  
    for j in range(1, n+1):
          print(j, "x", i, "=", j*i)
    print(n, "x", i, "=", n*j)


 




   
