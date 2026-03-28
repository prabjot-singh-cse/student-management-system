import csv
from student import Student

FILE_NAME = "data.csv"


def add_student():
    reg = input("ENTER YOUR REGISTRATION NUMBER: ")
    name = input("ENTER YOUR NAME: ")
    age = input("ENTER YOUR AGE: ")
    course = input("ENTER YOUR COURSE: ")
    place = input("ENTER YOUR PLACE: ")

    stu = Student(reg, name, age, course, place)
    with open(FILE_NAME, 'a', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(stu.to_list())
    print("Student added successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            print("\n--- Student List ---")
            for row in reader:
                print(
                    f"Registration Number: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}, Place: {row[4]}")
    except FileNotFoundError:
        print("No data found.\n")


def search_student():
    x = input("Enter Registration Number to search: ")
    found = False

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == x:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("Student not found.\n")


def delete_student():
    x = input("Enter ID to delete: ")
    rows = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != x:
                rows.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student deleted (if existed).\n")


def update_student():
    x = input("Enter ID to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == x:
                print("Enter new details:")
                name = input("Name: ")
                age = input("Age: ")
                course = input("Course: ")
                rows.append([x, name, age, course])
                updated = True
            else:
                rows.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")


def menu():
    while True:
        print("""
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    menu()
