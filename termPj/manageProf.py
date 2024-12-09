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


# CREATE 동아리
def create_club(connection):
    try:
        name = input("Enter club name: ")
        description = input("Enter club description: ")
        professor_id = input("Enter professor ID (leave blank if none): ") or None

        cursor = connection.cursor()
        query = "INSERT INTO clubs (name, description, professor_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, description, professor_id))
        connection.commit()
        print("Club added successfully.")
    except Error as e:
        print(f"Error: {e}")


# READ 동아리 목록
def read_clubs(connection):
    try:
        cursor = connection.cursor()
        query = """
        SELECT c.id, c.name, c.description, p.name AS professor_name
        FROM clubs c
        LEFT JOIN professors p ON c.professor_id = p.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n=== Club List ===")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Professor: {row[3] or 'None'}")
    except Error as e:
        print(f"Error: {e}")


# UPDATE 동아리
def update_club(connection):
    try:
        club_id = input("Enter the ID of the club to update: ")
        new_name = input("Enter new name (leave blank to skip): ")
        new_description = input("Enter new description (leave blank to skip): ")
        new_professor_id = input("Enter new professor ID (leave blank to skip): ")

        updates = []
        data = []
        if new_name:
            updates.append("name = %s")
            data.append(new_name)
        if new_description:
            updates.append("description = %s")
            data.append(new_description)
        if new_professor_id:
            updates.append("professor_id = %s")
            data.append(new_professor_id)

        if not updates:
            print("No updates provided.")
            return

        query = f"UPDATE clubs SET {', '.join(updates)} WHERE id = %s"
        data.append(int(club_id))
        cursor = connection.cursor()
        cursor.execute(query, tuple(data))
        connection.commit()
        print("Club updated successfully.")
    except Error as e:
        print(f"Error: {e}")


# DELETE 동아리
def delete_club(connection):
    try:
        club_id = input("Enter the ID of the club to delete: ")
        cursor = connection.cursor()
        query = "DELETE FROM clubs WHERE id = %s"
        cursor.execute(query, (int(club_id),))
        connection.commit()
        print("Club deleted successfully.")
    except Error as e:
        print(f"Error: {e}")


# CREATE 교수
def create_professor(connection):
    try:
        name = input("Enter professor name: ")
        department = input("Enter professor's department: ")
        email = input("Enter professor's email: ")

        cursor = connection.cursor()
        query = "INSERT INTO professors (name, department, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, department, email))
        connection.commit()
        print("Professor added successfully.")
    except Error as e:
        print(f"Error: {e}")


# READ 교수 목록
def read_professors(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM professors"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n=== Professor List ===")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Email: {row[3]}")
    except Error as e:
        print(f"Error: {e}")


# UPDATE 교수
def update_professor(connection):
    try:
        professor_id = input("Enter the ID of the professor to update: ")
        new_name = input("Enter new name (leave blank to skip): ")
        new_department = input("Enter new department (leave blank to skip): ")
        new_email = input("Enter new email (leave blank to skip): ")

        updates = []
        data = []
        if new_name:
            updates.append("name = %s")
            data.append(new_name)
        if new_department:
            updates.append("department = %s")
            data.append(new_department)
        if new_email:
            updates.append("email = %s")
            data.append(new_email)

        if not updates:
            print("No updates provided.")
            return

        query = f"UPDATE professors SET {', '.join(updates)} WHERE id = %s"
        data.append(int(professor_id))
        cursor = connection.cursor()
        cursor.execute(query, tuple(data))
        connection.commit()
        print("Professor updated successfully.")
    except Error as e:
        print(f"Error: {e}")


# DELETE 교수
def delete_professor(connection):
    try:
        professor_id = input("Enter the ID of the professor to delete: ")
        cursor = connection.cursor()
        query = "DELETE FROM professors WHERE id = %s"
        cursor.execute(query, (int(professor_id),))
        connection.commit()
        print("Professor deleted successfully.")
    except Error as e:
        print(f"Error: {e}")


# 메뉴 표시 및 실행
def main_menu():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    while True:
        print("\n=== Club and Professor Management System ===")
        print("1. Add Club")
        print("2. View Clubs")
        print("3. Update Club")
        print("4. Delete Club")
        print("5. Add Professor")
        print("6. View Professors")
        print("7. Update Professor")
        print("8. Delete Professor")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_club(connection)
        elif choice == "2":
            read_clubs(connection)
        elif choice == "3":
            update_club(connection)
        elif choice == "4":
            delete_club(connection)
        elif choice == "5":
            create_professor(connection)
        elif choice == "6":
            read_professors(connection)
        elif choice == "7":
            update_professor(connection)
        elif choice == "8":
            delete_professor(connection)
        elif choice == "9":
            print("Exiting the program.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")


# 메인 실행
if __name__ == "__main__":
    main_menu()
