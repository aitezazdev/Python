def factorial(n):
    if n == 1: 
        return 1 
    else: 
	    return n * factorial(n-1)

my_list = 5
res = factorial(my_list)
print(res)
