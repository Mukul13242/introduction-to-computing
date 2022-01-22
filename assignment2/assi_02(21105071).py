print('Question 1')
a='Python is a case sensitive language'
# (a) Length of string
print(len(a))
# (b) Reversing a string
print(a[len(a)::-1])
# (c) slicing
b=a[10:26]
print(b)
# (d) replacing
print(a.replace("a case sensitive", "object oriented"))
# (e) index of substring
print(a.index('a'))
# (f) remove white spaces
print(a.replace(" ", ""))

##################################################
print('Question 2')
name=str(input())
SID=int(input())
department=str(input())
CGPA=float(input())
print('''Hey, %s Here!
My SID is %d
I am from %s department and my CGPA is %f'''%(name,SID,department,CGPA))
#######################################################
print("Question 3")


a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)

######################################################################

print('Question 4 method 1')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)

#######################################################
    
print('Question 4 method 2')
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if (a>b and b>c):
    print("The greatest number is:",a)
elif(b>c):
    print("The greatest number is:",b)
else:
    print("The greatest number is:",c)

###########################################################

print('Question 5')
a=str(input("Write a sentence"))
if ("name" in a):
    print("yes")
else:
     print("No")

###################################################################

print('Question 6')
s1= int(input("Enter the length of first side of triangle: "))
s2= int(input("Enter the length of second side of triangle: "))
s3= int(input("Enter the length of third side of triangle: "))
if (s1+s2>s3 and s2+s3>s1 and s3+s1>s2):
    print("Yes")
else:
    print("No") 



