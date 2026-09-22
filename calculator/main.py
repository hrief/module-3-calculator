from calculator.operations import add, subtract, multiply, divide


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.")

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in OPERATIONS:
            print("Invalid operation. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = OPERATIONS[operation](num1, num2)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__": # pragma: no cover
    main()