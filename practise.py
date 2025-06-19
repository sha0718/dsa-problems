n = 5 
for i in range(n):
    row = ""
    for j in range(n-i):
        if i % 2 == 0:  
          row = row + " * "
        else:
          row = row + str(i+1)  
    print(row)
 
    

