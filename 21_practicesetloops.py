#q1 write a prog to print multiplication table of a given number using for loop

'''
num = int (input ("enter a number"))
for i in range(1,10):
    print (f"{num} x {i} = {num*i}")
    
    # OR # print(num, "x" ,i , "=", num * i)
'''

#q2 write a prog to greet all the persons in the list with S initials only
'''
l1 = ["Huzaif", "Saneeb", "Tanzeel", "Shahid"]
for item in l1:
    if item.startswith("S" or "s"):
        print ("Good morning" , item)
'''

#q3 attempt q1 using while loop

"""
num = int (input("enter a numnber"))
i = 1
while i <=10:
    print (num, "x" , i, "=",  num*i)
    print (f" {num} X {i} = {num*i}")
    i = i+1
"""

#q4 write a prog if  GIVEN NUMBER IS PRIME OR NOT

#q5 write a prog to find the sum of first n natural numbers
'''
n = int (input ("enter a number"))
n1 = 0
while n >0:
    n1 = n + n1
    n = n-1
    print (n1)
'''


#q6 to find a factorial of a number which is taken by user

# n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

'''
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial)
'''

#q7 write a program to print the following pattern
 #            *
 #           ***
#           *****         for n =3.


