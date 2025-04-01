operator = input("Enter an operator: (+, -, *, /, ^): ")
num1 = float(input("Enter first number: "))  # Changed eval to float for better safety
num2 = float(input("Enter second number: "))  # Changed eval to float for better safety

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    if num2 != 0:  # Adding check for division by zero
        result = num1 / num2
        print(result)
    else:
        print("Error: Division by zero is not allowed.")

elif operator == "^":
    result = num1 ** num2
    print(result)

else:
    print(f"{operator} is not a valid operator")
