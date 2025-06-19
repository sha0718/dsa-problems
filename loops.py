
for i in range(3,5):
    print ("hello world", i)
# whats wrong: the value of i is reassigned to 3, so the loop is always printing "hello world 3"

for i in range(5):
    print("hello world", i)

for i in range(2,9,2):
    print("hello world", i)    

for i in range(5,0,-1):
    print("hello world", i)

def greet(i):
    print("Namaste!", i)

for i in range(5):
    greet(i) 

arr = [1, 2, 9, 4, 15,22,34]
n = len(arr)
for i in range(n):
    print(arr[i])   

arr = [1, 2, 9, 4, 15,22,34,37]    
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], "is even")
    else:
        print(arr[i], "is odd")

i = 0
while i < 5:
    print("hello world", i)
    i += 1        

    