# for i in range(3):
#     for j in range(3):
#         print(i,j)
    

# for i in range(3):
#     for j in range(i):
#         print(i,j)    

# for i in range(5):
#     for j in range(i+1):
#         print(i,j)       

# for i in range(3):
#     for j in range(i + 1):  # j can go up to i
#         if j == i and j > 0:
#             print(i, j)

# for i in range(3):
#     for j in range(i, 0, -1):  # j from i down to 1
#         if j == i:
#             print(i, j)

for i in range(5, 0, -1):  # i = 5 down to 1
    for j in range(i):     # j = 0 to i-1
        print(i, j)            
