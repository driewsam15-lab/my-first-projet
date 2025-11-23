def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculator():
    print("=== Simple Python Calculator ===")
    print("Type 'q' at any time to quit.\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == "q":
            break

        num2 = input("Enter second number: ")
        if num2.lower() == "q":
            break

        op = input("Choose operation (+, -, *, /): ")
        if op.lower() == "q":
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Try again.\n")
            continue

        print(f"Result: {result}\n")

    print("Calculator closed. Goodbye!")

if __name__ == "__main__":
    calculator()
