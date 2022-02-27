
print("Question 1") 
#Defining tower of Hanoi function
def tower_of_hanoi(n , source, destination, auxiliary): 
    step_number=1
    if n==1: 
        print (f"Move disk 1 from{source}to{destination}") 
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print (f"Move disk {n} from {source} {destination}") 
    tower_of_hanoi(n-1, auxiliary, destination, source)
#taking the  number of disk input from the user
no_of_disk=int(input("Enter number of disks in tower of Hanoi:"))
print('''The Disks are numbered starting from top of the tower. 
      Steps to move all disks from Source Tower to Destination Tower is given below''') 
#Using the function of tower of hanoi
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")

#################################################################QUE 2#############################################

print("Question 2")

#inputing rows by user
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nBy Using recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops in que 
print("\n Alternate method\n")
print("\n By Using loops:\n")
for line in range(1, n+1):

    #same as the recursion method
    print('  '*(n - line), end='')

    x = 1
    for j in range(1, line+1):

        print(x, end='   ')

        x = x * (line - j) // j
    print()



 ####################################    Question3  ###########################################################

print("Question3") 
#Taking input from the user
n1=int(input("\nEnter an Integer:"))
n2=int(input("Enter another Integer:"))
#Making a list of return values
def remmod( a, b):
    quo = a%b
    rem = a//b
    return rem,quo
    
list1= list(remmod(n1,n2))
#a1=Quotient
q=list1[0]
#a2=Remainder
r=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")

#Que3.a
print("\nQue3.a")
c1=callable(remmod(n1,n2))
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
#Que3.b
print("\nQue3.b")
#list of values
listv=[q,r]
if (n1==0 and n2==0 and q==0 and r==0):
    print("Some values are zero")
else:
    print("All the values are non zero")    

#Que3.c
print("\nQue3.c")
#new values of list
listr=[q,r]
for i in range (4,7):
    listr.append(i)
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
#Que3.d
print("\nQue3.d")
set1=set()
#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print("\nQue3.e")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Que3.f
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")

######################################################QUE 4####################################################

print("\n[Question.4]\n")
class student:
    #using constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defing print function
    def pfun(self):
        print(f"Hy, My name is {self.name} and my "
              f"roll no. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Destructor Called")
#makin mukul as object of student
mukul=student("mukul goyal",21105071)
mukul.pfun()
del mukul
############################################QUE 5############################################

print("QUE 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#intserting employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# updating salary of mehak
employee1.salary = 70000
print(f"a. The {employee1.name} salary is updated to {employee1.salary}")

# deleting a record
print("b. ", end='')
del employee3

#################################################QUE 6 ########################################
print("QUESTION 6\n")
#definig principle of game 
def samesense(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1="George"
player2="Barbie"
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by George:"))
word_player2=str(input(f"Enter Word by Barbie:"))
#using samesense function
result=samesense(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of Barbie and George is REAL")
elif result==False:
    print(f"\nFriendship of Barbie and George is FAKE")