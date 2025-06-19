a = 10
b = 20 
sum  = a + b
print("The sum of", a, "and", b, "is", sum)


first_name = 1
last_name = 2
full_name = first_name + last_name
print("My name is", full_name)

list = [1,2,3,4,5,"ankit", True,]
print(list[6])

def helloworld():
    print("Hello World")
helloworld()   

def greet (name):
    print("Namaste", name)
greet("Ankit")
greet("Ankita")


def multiply(a, b):
    return a * b 
print(multiply(10, 20))

def square (x):
    return x * x
print(square(-5))  # Output: 25

def eligible_to_vote(age):
    
    if age < 0:
        return "Invalid age"
    elif age <= 18:
        return "You are not eligible to vote" 
    else:
        return "You are eligible to vote"
print(eligible_to_vote(15))
print(eligible_to_vote(20))
print(eligible_to_vote(-5))

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(10))
print(even_odd(15))