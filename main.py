import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="student_db"
)

cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
""")

# Insert student
def add_student(name, age, course):
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully!")

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

# Update student
def update_student(student_id, name):
    query = "UPDATE students SET name=%s WHERE id=%s"
    cursor.execute(query, (name, student_id))
    conn.commit()
    print("Student updated!")

# Delete student
def delete_student(student_id):
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted!")

# Example usage
add_student("Attar", 19, "IT")
view_students()

