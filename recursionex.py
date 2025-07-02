# a program to print n to 1 natural numbers using recursion

n = 20
def fun(x):
    if x == 0:
        return
    print(x)
    x = x - 1
    fun(x)

fun(n)

# a program to print 1 to n natural numbers using recursion

n = 20
def funs(x):
    if x == 0:
        return
    funs(x - 1)
    print(x)

funs(n)
