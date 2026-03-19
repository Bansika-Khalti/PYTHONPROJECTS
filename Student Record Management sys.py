# Student Record Manager

# Dictionary to store student data
students = {}

# Function to add a student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    
    # Tuple (immutable student basic info)
    basic_info = (student_id, name, age)
    
    # Set (unique courses)
    courses = set(input("Enter courses (comma separated): ").split(","))
    
    # Store in dictionary
    students[student_id] = {
        "info": basic_info,
        "courses": courses
    }
    
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("No students found\n")
    else:
        for sid, data in students.items():
            info = data["info"]
            courses = data["courses"]
            
            print(f"ID: {info[0]}, Name: {info[1]}, Age: {info[2]}")
            print(f"Courses: {', '.join(courses)}")
            print("-" * 30)


# Function to search student
def search_student():
    sid = input("Enter Student ID to search: ")
    
    if sid in students:
        info = students[sid]["info"]
        courses = students[sid]["courses"]
        
        print(f"Found: {info[1]}, Age: {info[2]}")
        print(f"Courses: {', '.join(courses)}\n")
    else:
        print("Student not found\n")


# Function to remove student
def remove_student():
    sid = input("Enter Student ID to remove: ")
    
    if sid in students:
        del students[sid]
        print("Student removed successfully\n")
    else:
        print("Student not found\n")


# Main menu function
def main():
    while True:
        print("\n==== Student Manager ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        # If-else conditions
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
main()