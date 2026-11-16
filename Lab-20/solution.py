# Lab 20 - Daily Log Book Management System

import os

def display_menu():
    print("\n===============================")
    print("      OFFICE DAILY LOG BOOK     ")
    print("===============================")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")
    print("===============================")

def add_entry():
    filename = "daily_log.txt"
    try:
        # Using 'a' (append) mode to add new entries without overwriting old ones
        with open(filename, "a") as file:
            entry = input("Enter log entry to add: ")
            file.write(entry + "\n")
        print("Log entry added successfully!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def display_log():
    filename = "daily_log.txt"
    if not os.path.exists(filename):
        print("\nError: No log file found. Please add a log entry first.")
        return

    try:
        print("\n--- Complete Log Book ---")
        with open(filename, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("(The log book is currently empty.)")
            else:
                print(content, end="")
        print("-------------------------")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-3): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            display_log()
        elif choice == '3':
            print("\nThank you for using the Daily Log Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 3.")

if __name__ == "__main__":
    main()