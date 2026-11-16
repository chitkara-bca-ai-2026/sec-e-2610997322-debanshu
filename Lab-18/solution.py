# Lab 18 - Mathematics Learning Tool

def factorial(n):
    # Base Case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive Step: n * factorial(n - 1)
    return n * factorial(n - 1)

def fibonacci(n):
    # Base Cases: fib(0) = 0, fib(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Step: fib(n - 1) + fib(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    while True:
        print("\n" + "=" * 30)
        print(" MATHEMATICS LEARNING TOOL")
        print("=" * 30)
        print("Select an operation:")
        print("1. Calculate Factorial")
        print("2. Generate Fibonacci Series")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Error: Please enter a non-negative integer.")
                else:
                    result = factorial(num)
                    print(f"{num}! = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid integer.")
                
        elif choice == '2':
            try:
                terms = int(input("Enter number of terms to generate: "))
                if terms <= 0:
                    print("Error: Please enter a positive integer.")
                else:
                    fib_series = [fibonacci(i) for i in range(terms)]
                    print(f"Fibonacci series: {fib_series}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid integer.")
                
        elif choice == '3':
            print("Thank you for using the Mathematics Learning Tool. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
