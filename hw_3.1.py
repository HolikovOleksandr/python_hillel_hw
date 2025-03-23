first_value = float(input("Hi, choose a first value for calculating: "))
second_value = float(input("Choose a second value for calculating: "))
operation = input("Choose an operation: +, -, *, /: ")
result = None

if operation == "+":
    result = first_value + second_value
elif operation == "-":
    result = first_value - second_value
elif operation == "*":
    result = first_value * second_value
elif operation == "/":
    if second_value == 0:
        print("Division by zero is not allowed")
    else:
        result = first_value / second_value
else:
    print("Invalid operation")
    
print(f"Result: {result}")
