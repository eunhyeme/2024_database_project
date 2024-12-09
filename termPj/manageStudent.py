import mysql.connector
from mysql.connector import Error


# MySQL 데이터베이스 연결
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="your_centos_server_ip_or_hostname",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# CREATE 학생
def create_student(connection):
    try:
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        major = input("Enter student's major: ")
        email = input("Enter student's email: ")

        cursor = connection.cursor()
        query = "INSERT INTO students (name, age, major, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, int(age), major, email))
        connection.commit()
        print("Student added successfully.")
    except Error as e:
        print(f"Error: {e}")


# READ 학생 목록
def read_students(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n=== Student List ===")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Major: {row[3]}, Email: {row[4]}")
    except Error as e:
        print(f"Error: {e}")


# UPDATE 학생 정보
def update_student(connection):
    try:
        student_id = input("Enter the ID of the student to update: ")
        new_name = input("Enter new name (leave blank to skip): ")
        new_age = input("Enter new age (leave blank to skip): ")
        new_major = input("Enter new major (leave blank to skip): ")
        new_email = input("Enter new email (leave blank to skip): ")

        updates = []
        data = []
        if new_name:
            updates.append("name = %s")
            data.append(new_name)
        if new_age:
            updates.append("age = %s")
            data.append(int(new_age))
        if new_major:
            updates.append("major = %s")
            data.append(new_major)
        if new_email:
            updates.append("email = %s")
            data.append(new_email)

        if not updates:
            print("No updates provided.")
            return

        query = f"UPDATE students SET {', '.join(updates)} WHERE id = %s"
        data.append(int(student_id))
        cursor = connection.cursor()
        cursor.execute(query, tuple(data))
        connection.commit()
        print("Student updated successfully.")
    except Error as e:
        print(f"Error: {e}")


# DELETE 학생
def delete_student(connection):
    try:
        student_id = input("Enter the ID of the student to delete: ")
        cursor = connection.cursor()
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (int(student_id),))
        connection.commit()
        print("Student deleted successfully.")
    except Error as e:
        print(f"Error: {e}")


# 메뉴 표시 및 실행
def main_menu():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_student(connection)
        elif choice == "2":
            read_students(connection)
        elif choice == "3":
            update_student(connection)
        elif choice == "4":
            delete_student(connection)
        elif choice == "5":
            print("Exiting the program.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")


# 메인 실행
if __name__ == "__main__":
    main_menu()
