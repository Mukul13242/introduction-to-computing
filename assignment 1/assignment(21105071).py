#      program 1
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
num3=int(input("Enter the num3:"))
avg=(num1+num2+num3)/3
print("the avg is",avg)



#  program 2
standard_deviation=10000
tax_rate=0.2
gross_income=float(input("Enter gross_income: "))
number_of_dependents=int(input("Enter number_of_dependents:"))
dependent_deduction=3000
taxable_income=float(gross_income-standard_deviation-(dependent_deduction)*(number_of_dependents))
tax=taxable_income*tax_rate
print("tax",tax)

#    program 3
print("student=[21105071,mukul,male,ece,9.5]")


#  program 4
print("Marks of 5 students :")
Marks=[89,53,18,45,56]
print("List befor sorting",Marks)
Marks.sort()
print(" List after Sorting",Marks)


# program 5
# # part A
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color) 

# part B
color_2=['Red','Green','White','Black','Pink','Yellow']
color_2.pop(3)
print(color_2)
color_2.pop(3)
print(color_2)
color_2.insert(3,'Purple')
print(color_2)


