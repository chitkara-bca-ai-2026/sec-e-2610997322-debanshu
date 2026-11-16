# Lab 16: Utility Calculator
# Modular Functions and Session History


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result, or None if dividing by zero."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return the remainder, or None if dividing by zero."""
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    """Return base raised to the given exponent (default is 2)."""
    return base ** exp


def format_number(n):
    """Return an integer if the number has no decimal part."""
    if isinstance(n, (int, float)) and n == int(n):
        return int(n)
    return n


def get_number(prompt):
    """Read and validate a numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def display_menu():
    """Display the calculator menu."""
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")


def main():
    """Run the utility calculator."""
    history = []

    print("=" * 12, "ENTERPRISE MODULAR UTILITY CALCULATOR", "=" * 12)

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("Invalid choice! Please select a number from 1 to 8.")
            continue

        if choice == "8":
            print("Exiting... Thank you!")
            break

        if choice == "7":
            print("\nCalculation History:")

            if not history:
                print("No calculations performed yet.")
            else:
                for index, record in enumerate(history, start=1):
                    print(f"{index}. {record}")

            continue

        # Get operands for arithmetic operations
        a = get_number("Enter first number: ")

        if choice == "6":
            exponent_input = input(
                "Enter exponent (press Enter for default square): "
            ).strip()

            if exponent_input == "":
                result = power(a)
                expression = f"{a} ** 2"
            else:
                try:
                    exponent = float(exponent_input)
                    result = power(a, exponent)
                    expression = f"{a} ** {exponent}"
                except ValueError:
                    print("Invalid exponent! Please enter a number.")
                    continue

        else:
            b = get_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)
                expression = f"{a} + {b}"

            elif choice == "2":
                result = subtract(a, b)
                expression = f"{a} - {b}"

            elif choice == "3":
                result = multiply(a, b)
                expression = f"{a} * {b}"

            elif choice == "4":
                result = divide(a, b)
                expression = f"{a} / {b}"

            elif choice == "5":
                result = modulus(a, b)
                expression = f"{a} % {b}"

        # Handle division or modulus by zero
        if result is None:
            print("Error: Cannot divide or take modulus by zero.")
            continue

        # Handle arithmetic errors such as overflow
        try:
            result = format_number(result)
        except (OverflowError, ValueError):
            print("Error: The result is too large or invalid.")
            continue

        formatted_expression = expression.replace("**", "^")
        record = f"{formatted_expression} = {result}"

        print(f"[RESULT] {record}")

        # Record successful calculations
        history.append(record)


if __name__ == "__main__":
    main()