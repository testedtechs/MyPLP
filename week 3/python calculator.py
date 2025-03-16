num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
operation = input("Please enter the type of operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Number cannot be divided by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

print(f"{num1} {operation} {num2} = {result}")

exit()