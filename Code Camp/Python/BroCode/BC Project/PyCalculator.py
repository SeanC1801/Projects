# Simple Calculator

operator = input("Enter a operator (+ - * / %): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "%":
    result = num1 % num2
    print(round(result, 3))
else:
    print(f'"{operator}" is not a valid input. Enter a valid operator and try again.')