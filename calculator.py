import math

print("This is a Calculator.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. To the power of...")
print("6. Square root")
method = int(input("Please select a method: "))

while method > 6 or method < 1:
    print("Error, please retry.")
    method = int(input("Please select a method: "))

if method == 1 or method == 2 or method == 3 or method == 4 or method == 5:
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
else:
    num1 = float(input("Please enter your number: "))

if method == 1:
    num3 = num1 + num2
    num3 = float(num3)
    print(num1, " add ", num2, " is ", num3)
elif method == 2:
    num3 = num1 - num2
    num3 = float(num3)
    print(num1, " subtract ", num2, " is ", num3)
elif method == 3:
    num3 = num1 * num2
    num3 = float(num3)
    print(num1, " multiplied by ", num2, " is ", num3)
elif method == 4:
    num3 = num1 / num2
    num3 = float(num3)
    print(num1, " divided by ", num2, " is ", num3)
elif method == 5:
    num3 = num1 ** num2
    num3 = float(num3)
    print(num1, " to the power of ", num2, " is ", num3)
else:
    num3 = math.sqrt(num1)
    num3 = float(num3)
    print("The square root of ", num1, " is ", num3)