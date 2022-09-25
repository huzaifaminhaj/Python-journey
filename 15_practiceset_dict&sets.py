
#q1 to enter an english word from user and show its meaning

'''
 engdict =  {

     "name":"naam",

     "work":"kaam",

     "eat":"khana",

     "earn":"kamana",

 }

 a = input ("Enter the english word \n")

 print("The meaning of this word is:", engdict[a])
'''

#q2 print unique numbers 
'''
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
num4 = int(input("enter a number"))
num5 = int(input("enter a number"))
num6 = int(input("enter a number"))
num7 = int(input("enter a number"))
num8 = int(input("enter a number"))
set1 = {num1,num2,num3,num4,num5,num6,num7,num8}
'''
# print("the unique numbers are:", set1)


#q3 we need to check if we can print 18 as an int and a18 as str in a set
'''

s = {18,"18"}

print(s)
'''
#q4
'''
s = set()
s.add (20)
s.add (20.0)
s.add ("20")
print (s)
print(len(s))
'''

#q5
'''
s = {}
print(type(s))
'''

#q6 
'''
mydict = {
    
}
a = str(input("enter a key\n"))
b = str(input("enter a value\n"))

a1 = str(input("enter a key\n"))
b1 = str(input("enter a value\n"))

a2 = str(input("enter a key\n"))
b2 = str(input("enter a value\n"))

mydict.update({
    a:b,
    a1:b1,
    a2:b2
    })
print(mydict.items())

'''  

# OR

'''
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)
'''
