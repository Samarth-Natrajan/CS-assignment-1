# Q.1
user_input = input("please enter this - 'Python is a case sensitive language': ")
print("Length of the input string = ",len(user_input)) # part a)

reversed_user_input = user_input[::-1] # part b)
print(" ")
print("reversed input string:-\n",reversed_user_input)

sliced_user_input = user_input[10:26] # part c)
print(" ")
print("sliced string:-\n",sliced_user_input)

new_string = user_input.replace("a case sensitive","object oriented") # part d)
print(" ")
print("after replacing:-\n",new_string)

print(" ")
print("index of 'a':- ",user_input.find("a")) # part e)

new_string2 = "" # part f)
for i in user_input:
    if i != " ":
        new_string2+=i
print(" ")
print("input string after removing white spaces:-\n",new_string2)

 
# Q.2
name = "Samarth Shridhar Natrajan"
SID = 21105100
department = "ECE"
cgpa = "9.9" 
print("Hey,",name,"Here!\nMy SID is",SID,"\nI am from",department,"and my CGPA is",cgpa)


# Q.3
a = 56
b = 10
binary_and_operator = a & b  # AND operator
print("AND operation:-\n",binary_and_operator)
print(" ")

binary_or_operator = a | b   # OR operator
print("OR operation:-\n",binary_or_operator)
print(" ")

binary_xor_operator = a ^ b  # XOR operator
print("XOR operation:-\n",binary_xor_operator)
print(" ")
# Left and Right shift operator
binary_leftshift_operator1 = a << 2
binary_leftshift_operator2 = b << 2
print("Binary Left Shift Operation:-\n",binary_leftshift_operator1,",",binary_leftshift_operator2)
print(" ")

binary_rightshift_operator1 = a>>2
binary_rightshift_operator2 = b>>4
print("Binary Right Shift Operation:-\n",binary_rightshift_operator1,",",binary_rightshift_operator2)
print("")



# Q.4
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
if ((num1>=num2 and num1>num3) or (num1>num2 and num1>=num3)):
    print("the greatest number is: ",num1)
elif ((num2>num1 and num2>=num3) or (num2>=num1 and num2>num3)):
    print("the greatest number is: ",num2)
elif ((num3>=num1 and num3>num2) or (num3>num1 and num3>=num2)):
    print("the greatest number is: ",num3)
else:
    print("all are equal")


# Q.5
string = input("enter a string: ")
for i in range(0,len(string)-3):
    if string[i:i+4] == "name":
        print("YES!")
        break
else:
    print("NO!")


# Q.6
side1 = int(input("enter the length of first side: "))
side2 = int(input("enter the length of second side: "))
side3 = int(input("enter the length of third side: "))

# Declaring Sum of any two sides
a = side1 + side2
b = side2 + side3
c = side3 + side1
if (a>side3 and b>side1 and c>side2):
    print("YES!")
else:
    print("NO!")

