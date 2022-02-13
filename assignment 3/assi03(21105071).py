print("question1\n")
def word_count(str):     #using the function
  count=dict()         #making dictinory
  words=str.split()    #splitting the  string
  if len(words)==1:
    for i in str:
      if i in count:
        count[i]=count[i]+1
      else:
        count[i]=1
    return count
  else:
    for x in words:
      if x in count:
        count[x]=count[x]+1
      else:
        count[x]=1
    return count

string=input("Enter the string\n")
y=word_count(string)
print(y)

   ######################################QUESTION 2############################################################ 



print("Question2")
def leap_year(year: int) -> bool:                                                                                #Function for checking if the given year is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("invalid date according to question,conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #Condition for no. of days in February
        if leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      #Setting no. of days in the given month
    if leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                #Syntax for incrementing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))

   ######################################QUESTION 3############################################################ 
print("Question 3")

list1=list(map(int,input("Enter the numbers separated by space:").split()))  #inputing the lists

list2=[]          #Creating second empty list
for j in list1:
    output = (j,j**2)
    list2.append(output)
print("Final Output is given as:")
print(list2)




   ######################################QUESTION 4############################################################ 

print("Question 4")
grade_point=int(input("Enter the grade_point:\n"))
grade=["+A","A","B+","B","C+","C","D"]
Performence=["Outstanding","Excellent","VERY GOOD","Good","Average","Below Average","Poor"]
if 4<=grade_point<=10:
  i=10-grade_point
  print("Your Grade is %s and %s"%(grade[i],Performence[i]))
else:
  print("Grade is invalid")
    
   ######################################QUESTION 5############################################################ 

print("quetion 5")
string="ABCDEFGHIJK"
j=0
while len(string)-2*j>=1:
  x=string[0:len(string)-2*j]
  print(" "*j+x)
  j=j+1
   ######################################QUESTION 6############################################################ 

print("\nQ.6")
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
#List containing Y or N
liste=["Y","y","n","N"]
#Main code
while repeat=="Y" or repeat=="y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'(will be helpful while sorting)
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")


   ######################################QUESTION 7############################################################ 
print("\nQ.7")
#Taking input
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
#printing error message when N<=0
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {two_decimal}")

   ######################################QUESTION 8############################################################ 

print("question 8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

set4=Set1.union(Set2)-Set1.intersection(Set2)

print("Q.8(a)")
print(" Set of all elements that are in Set1 and Set2 but not both:",set4)
set5=(Set1|Set2|Set3)-Set1.intersection(Set2)-Set2.intersection(Set3)-Set3.intersection(Set1)

print("Q.8(b)")
print('''a new set of all elements that are in only one of the three sets Set1,Set2 and Set3:''',set5)

print("Q.8(c)")
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:")
set6 = (Set1|Set2|Set3) - (Set1^Set2^Set3) - (Set1&Set2&Set3)
print(set6)

print("Q.8(d)")
print(" Set of all integers in the range 1 to 10 that are not in Set1:")
set7 = set()
for i in range(1,11):
    if i not in Set1:
        set7.add(i)
print(set7)

print("Q.8(e)")
print(" Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:")
set8 = set(range(1,11)) - (Set1|Set2|Set3)
print(set8)








