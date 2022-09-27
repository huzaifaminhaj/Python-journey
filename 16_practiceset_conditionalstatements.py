#q1 write a prog to find greatest of four numbers entered by the user
'''
a = int (input("enter first number"))
b = int (input("enter second number"))
c = int (input("enter third number"))
d = int (input("enter four number"))

if a>b and a>c and a>d:
    print("the greatest number is:", a)
elif b>a and b>c and b>d:
    print("the greatest number is:", b)
elif c>d and c>a and c>b:
    print("the greatest number is:", c)
elif d>a and d>b and d>c:
    print("the greatest number is:", d)    
else:
    print("none of the conditions are true")
'''

#q2 Write a prog to find out whether a student is PASS or FAIL if it requires total 40% and atleast 30% in each subject to pass. Assume 3 subjects and take marks as input from user.

'''
sub1 = int(input("enter marks for sub1:\n"))
sub2 = int(input("enter marks for sub2:\n"))
sub3 = int(input("enter marks for sub3:\n"))
if sub1<33 or sub2<33 or sub3<33: 
    print("you are FAIL because you have less than 33 marks in any of the subjects")

elif (sub1+sub2+sub3)/3  <40:
    print("you have Failed because the total percentage is  less than 40")

else:
    print ("You have Passed")
'''

#q3 spam detection

'''
text= str (input("Enter the text recieved"))
a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"
if text == a:
    print ("spam")
elif text == b:
    print("spam")
elif text == c:
    print("spam")
elif text == d:
    print("spam")
else:
   print("No spam found")
'''
   #-----------OR------------
'''
text= str (input("Enter the text recieved"))
a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"
if text == a or text == b or text == c:
    print ("SPAM")
else:
    print ("No SPAM found")
'''
#------------OR-----------
'''
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
'''

#q4 take username from user as input and check if the characters are less than 10 or not
'''
username = str (input("enter the username:\n"))
if len(username) <10:
    print("the username if of less than 10 charqacters")
else:
    print("the characters are greaters than 10")
'''

#q5  Write a program which finds out whether a given name is present in the list or not
'''
list = ["huzaif", "manaan", "saneeb"]
name = input("enter a name")
if name in list:
    print("the name is in the list")
else:
    print("the name is not in the list")    
'''
#q6 write a prog to calculate the grade of a student from his marks from the foloowing:
# 90-100: EX, 80-90: A, 70-80: B, 60-70: C, 50-60:D.

'''
marks = int(input("Enter your marks\n"))

if marks < 100 and  marks >= 90:
    print("your grade is EX")
elif marks <90 and marks >= 90:
    print("your grade is A")
elif marks <80 and marks >= 70:
    print("your grade is B ")
elif marks <70 and marks >= 60:
    print("your grade is C ")
elif marks <60 and marks >= 50:
    print("your grade is D ")
 '''   

#---------OR---------------
'''
marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)
'''


#q7 write a program to find out whether a given post is talking about "Huzaif" or not

name = ("Huzaif")
name1 = ("huzaif")
post = (input("Type the post/form here:\n"))
if name in post:
    print("The word Huzaif is present in the post.")
elif name1 in post:
    print("The word huzaif is present in the post.")
else:
    print("The word Huzaif/huzaif is not present in the post")

