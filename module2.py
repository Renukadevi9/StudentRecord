import re

FILE_NAME = "students.txt"

# Validate Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Add Student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")

        if not validate_email(email):
            raise ValueError("Invalid Email Format!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)

# View Students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found!")
                return

            print("\n===== Student Records =====")

            for record in records:
                student_id, name, email = record.strip().split(",")

                print(f"ID    : {student_id}")
                print(f"Name  : {name}")
                print(f"Email : {email}")
                print("-" * 30)

    except FileNotFoundError:
        print("No records file found!")

# Search Student
def search_student():
    sid = input("Enter Student ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for record in file:
                student_id, name, email = record.strip().split(",")

                if student_id == sid:
                    print("\nStudent Found")
                    print("ID    :", student_id)
                    print("Name  :", name)
                    print("Email :", email)
                    found = True
                    break

            if not found:
                print("Student not found!")

    except FileNotFoundError:
        print("No records file found!")

# Remove Student
def remove_student():
    sid = input("Enter Student ID to remove: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] != sid:
                    file.write(record)
                else:
                    found = True

        if found:
            print("Student removed successfully!")
        else:
            print("Student ID not found!")

    except FileNotFoundError:
        print("No records file found!")

# Main Program
while True:
    print("\n========== Student Record Manager ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        print("Thank you for using Student Record Manager!")
        break

    else:
        print("Invalid Choice! Please enter 1-5.")

