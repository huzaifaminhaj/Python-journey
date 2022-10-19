'''
Recursion is a function which calls itself.

Factorial(n) = n * factorial(n-1)


def factorial(n):

    if n==1 or n==0:    #base condition which doesn't call the function any further to avpoid stackoverflow
        return 1
    else:
        return n * factorial (n-1)    #function calling itself.
  

'''

def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)
#f = factorial_iter(5)
f = factorial_recursive(5)
print(f)
