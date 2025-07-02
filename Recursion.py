def fun(num):
    if num == 0: # base case stops the recursion
        return
    print(num)
    num = num - 1
    fun(num)

a = 10
fun(a)    

