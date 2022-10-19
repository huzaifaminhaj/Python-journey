'''
 RECURSION: is a function which calls itself.
  FORMULLA:
            factorial(n) = n * factorial(n-1)

'''

# THIS FUNCTIUON CAN BE DEFINED AS FOLLOWING
'''
def factorial(n):
    if n==1 or n==0:  #base condition which doesn't call the function any further to avpoid stackoverflow
        return 1
    else:
        return n * factorial (n-1)  #function calling itself.
'''    


# LET US UNDERSTAND FACTORIAL FIRSTLY

 #eg-      factorial of 5! = 5*4*3*2*1
     #     factorial of 3! = 3*2*1
     #     factorial of 1! = 1
     #     factorial of 0 =1
   
 # using FOR LOOP for finding factorial

'''
n = 4
product = 1
for i in range(n):
    product = product * (i+1)
print(product)
'''
# Let us find factorial using a FUNCTION now for n = 4 and using a FOR LOOP

def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product * (i+1)
    return product
print (factorial_iter(4))
    
