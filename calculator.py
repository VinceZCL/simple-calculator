#Importing math module for math.sqrt() function
import math

#User input notes
print("This is a Calculator.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. To the power of...")
print("6. Square root")
method = int(input("Please select a method: "))

#Identifying user inputs
while method > 6 or method < 1:
    print("Error, please retry.") #Returning an error message if user input is invalid
    method = int(input("Please select a method: ")) #Prompt another user input

#Initiate digits input
if method == 1 or method == 2 or method == 3 or method == 4 or method == 5:
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
else:
    num1 = float(input("Please enter your number: ")) #If desired method is square root

if method == 1: #Addition
    num3 = num1 + num2
    num3 = float(num3)
    print(num1, " add ", num2, " is ", num3)
elif method == 2: #Subtraction
    num3 = num1 - num2
    num3 = float(num3)
    print(num1, " subtract ", num2, " is ", num3)
elif method == 3: #Multiplication
    num3 = num1 * num2
    num3 = float(num3)
    print(num1, " multiplied by ", num2, " is ", num3)
elif method == 4: #Division
    num3 = num1 / num2
    num3 = float(num3)
    print(num1, " divided by ", num2, " is ", num3)
elif method == 5: #To the power of
    num3 = num1 ** num2
    num3 = float(num3)
    print(num1, " to the power of ", num2, " is ", num3)
else: #Square root
    num3 = math.sqrt(num1)
    num3 = float(num3)
    print("The square root of ", num1, " is ", num3)
