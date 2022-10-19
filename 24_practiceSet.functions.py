#q1  Write a program using function to find greatest of three numbers
'''
def func1 (num1, num2, num3):
    
    if num1 > num2 > num3:
        return num1
    elif num2 > num3 >num1:
        return num2
    else:
        return num3
f = func1(40,50,45)
print (f)

'''
#q2 WRITE A PROG USING FUNCTION TO CONVERT CELSIUS TO FAHRENHITE


#q3  WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS
'''

def recur_sum(n):
    if n<= 1:
        return n
    else:
        return recur_sum(n-1) + n

s = recur_sum(5)
print (s)

'''
#q4  WRITE A PYTHON FUNC TO PRINT FIRST N LINES OF THE FOLLOWING PATTERN
#   ***
#   **
#   *
'''
n = 5
for i in range (n):
    print ("*" * (n-i))  # prints n-i times.
'''

#q5 WRIE A PYTHON FUNCTION TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER
'''

def multiplication_table(n):
    for i in range (10):
        print (n, "x", i + 1, "=", n*(i+1))

num = int(input ("enter a number"))
multiplication_table(num)

'''

