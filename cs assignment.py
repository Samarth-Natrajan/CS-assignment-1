# Q.1 Write a python program to find average of three numbers entered by the user

choice = "y"
while (choice == 'y'):
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    num3 = int(input("enter the third number: "))

    average = (num1+num2+num3)/3 #formula of average

    print("the average of the three numbers is: ",average)
    choice = input("enter (y/n) to continue or terminate: ")

print("")



# Q.2 Write a python program to compute a person's income tax

#user details
gross_income = float(input("enter your salary in $ (to the nearesr penny): "))
dependent_num = int(input("enter number of dependent(s): "))

# declaring tax constants and calculation
tax_rate = 0.20 # or 20%
std_deduction = 10000 # in $
deduction_per_dependent = 3000 # in $
taxable_income = gross_income - std_deduction - (deduction_per_dependent*dependent_num)

tax_amount = taxable_income*tax_rate # payable tax amount
print("your tax amount is equal to(in $): ",tax_amount,'$')



# Q.3 Write a python program to store different data type values into a list
Student_details = [21105100,"Samarth","M","ECE",9.65]
print("a list of differernt data types like 'string','int','float' etc:- ")
print(Student_details)



# Q.4 Write a python program to enter marks of 5 students into a list and display

marks_record = []

for i in range(5):
    marks = int(input("enter marks of students(out of 100): "))
    marks_record.append(marks)

marks_record.sort() # sorts the list
print("sorted list of marks of students: ",marks_record)



# Q.5 a)
colors = ["Red","Green","White","Black","Pink","Yellow"]
colors.remove(colors[3])
print(colors)

# Q.5 b)
colors = ["Red","Green","White","Black","Pink","Yellow"]
colors[3:5] = ["Purple"]
print(colors)
