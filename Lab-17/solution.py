def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll Number: {roll}")
    print(f"Name: {student['Name']}")
    print(f"Marks: {student['Marks']}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

def add_student(students, roll, name, marks):
    if roll in students:
        print("\nError: Roll number already exists.")
    else:
        students[roll] = {"Name": name, "Marks": marks}
        print("\nStudent record added successfully.")

def main():
    students = {
        "101": {"Name": "Namra", "Marks": [85, 90, 88]},
        "102": {"Name": "Suho", "Marks": [78, 82, 80]},
        "103": {"Name": "Sieun", "Marks": [92, 88, 95]}
    }

    while True:
        print("\nSTUDENT RECORD SYSTEM")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            if not students:
                print("\nNo student records found.")
            else:
                print("\n--- Student Records ---")
                for roll, student in students.items():
                    display_student(roll, student)
                    print("-" * 30)

        elif choice == '2':
            roll = input("Enter Roll Number: ").strip()
            name = input("Enter Name: ").strip()
            try:
                marks = []
                for i in range(3):
                    m = int(input(f"Enter mark for subject {i+1}: ").strip())
                    marks.append(m)
                add_student(students, roll, name, marks)
            except ValueError:
                print("\nError: Marks must be integer values.")

        elif choice == '3':
            roll = input("Enter Roll Number to search: ").strip()
            student = students.get(roll)
            if student:
                print("\n--- Student Found ---")
                display_student(roll, student)
            else:
                print("\nStudent not found.")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("\nError: Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()