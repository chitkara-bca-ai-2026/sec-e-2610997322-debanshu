print("="*50)
print("             Library Management System")
print("="*50)

print("select an operation:")
print(" 1. View cataloged books")
print(" 2. Add New book Record")
print(" 3. View Unique library Categories")
print(" 4. Add category to student wish list")
print(" 5. Run Category Gap Analysis")
print(" 6. Exit")


choice = input("Enter your choice (1-6): ")

books={"The Great Gatsby": {"author": "F. Scott Fitzgerald", "category": "Fiction"},
       "To Kill a Mockingbird": {"author": "Harper Lee", "category": "Fiction"}}

if choice == "1":
    print("Viewing cataloged books...")
    # Code to view cataloged books goes here
    print("Cataloged Books:")
    for book, details in books.items():
        print(f"Title: {book}, Author: {details['author']}, Category: {details['category']}")
    

elif choice == "2":
    print("Adding new book record...")
    # Code to add new book record goes here
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter book category: ")
    books[title] = {"author": author, "category": category}
    print(f"Added {title} by {author} in category {category}.")

elif choice == "3":
    print("Viewing unique library categories...")
    # Code to view unique library categories goes here
    unique_categories = set(details['category'] for details in books.values())
    print("Unique Categories:")
    for category in unique_categories:
        print(category)

elif choice == "4":
    print("Adding category to student wish list...")
    # Code to add category to student wish list goes here
    wish_list = []
    category = input("Enter category to add to wish list: ")
    if category not in wish_list:
        wish_list.append(category)
        print(f"Added {category} to student wish list.")
    else:
        print(f"{category} is already in the wish list.")

elif choice == "5":
    print("Running Category Gap Analysis...")
    # Code to run Category Gap Analysis goes here
    pass

elif choice == "6":
    print("Exiting Library Management System...")
    # Code to exit the system goes here
    pass

else:
    print("Invalid choice. Please select a valid option (1-6).")