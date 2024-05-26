def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    operations = {'A': 'Add', 'S': 'Subtract', 'M': 'Multiply', 'D': 'Divide'}
    while True:
        operation = input("Do you want to add, subtract, multiply or divide? Please type A for Add, S for Subtract, M for Multiply or D for Divide: ").upper()
        if operation in operations:
            return operation
        else:
            print("Invalid input. Please enter A, S, M, or D.")

def calculate(x, y, operation):
    if operation == 'A':
        return x + y
    elif operation == 'S':
        return x - y
    elif operation == 'M':
        return x * y
    elif operation == 'D':
        if y == 0:
            return "Error: Division by zero is undefined."
        return x / y

def main():
    first_number = get_number("First: ")
    second_number = get_number("Second: ")
    operation = get_operation()
    result = calculate(first_number, second_number, operation)
    print("Result:", result)

if __name__ == "__main__":
    main()