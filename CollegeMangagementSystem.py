import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()


# 🔹 Create Tables
def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id TEXT,
        course_id TEXT
    )
    """)

    conn.commit() #saves the changes to the database.


# 🔹 Add Student  stores student info: ID, Name, Age.
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    try:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (sid, name, age))
        conn.commit()
        print(" Student added!\n")
    except:
        print("Student ID already exists!\n")


# 🔹 Add Course   stores courses: ID, Name.
def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")

    try:
        cursor.execute("INSERT INTO courses VALUES (?, ?)", (cid, cname))
        conn.commit()
        print("Course added!\n")
    except:
        print("Course already exists!\n")



def enroll_student():
    sid = input("Enter Student ID: ")
    cid = input("Enter Coursedir(mymodule) ID: ")

    cursor.execute("SELECT * FROM students WHERE id=?", (sid,))
    student = cursor.fetchone()  #fetches one row.

    cursor.execute("SELECT * FROM courses WHERE id=?", (cid,))
    course = cursor.fetchone()

    if student and course:
        cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (sid, cid))
        conn.commit()
        print("Enrollment successful!\n")
    else:
        print("Invalid Student or Course ID\n")


# 🔹 View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if not data:
        print("No students found\n")
    else:
        for row in data:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")


# 🔹 View Courses
def view_courses():
    cursor.execute("SELECT * FROM courses")
    data = cursor.fetchall()  

    if not data:
        print("No courses available\n")
    else:
        for row in data:
            print(f"Course ID: {row[0]}, Name: {row[1]}")


# 🔹 View Enrollments
def view_enrollments():     # Enroll Student stores relationships between students and courses.
    cursor.execute("""
    SELECT students.name, courses.name
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
    """)

    data = cursor.fetchall()   #returns list of tuples.

    if not data:
        print("No enrollments\n")
    else:
        for row in data:
            print(f"{row[0]} enrolled in {row[1]}")


# 🔹 Main Menu
def main():
    create_tables()

    while True:
        print("\n===== College DB System =====")
        print("1.Add Student")
        print("2.Add Course")
        print("3.Enroll Student")
        print("4.View Students")
        print("5.View Courses")
        print("6.View Enrollments")
        print("7.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enroll_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            view_courses()
        elif choice == "6":
            view_enrollments()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()
conn.close()