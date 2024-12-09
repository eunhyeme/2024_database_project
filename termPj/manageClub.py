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
        member_count = input("Enter initial member count (default 0): ") or 0

        cursor = connection.cursor()
        query = "INSERT INTO students_clubs (name, description, member_count) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, description, int(member_count)))
        connection.commit()
        print("Club added successfully.")
    except Error as e:
        print(f"Error: {e}")


# READ 동아리 목록
def read_clubs(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM students_clubs"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n=== Club List ===")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Members: {row[3]}")
    except Error as e:
        print(f"Error: {e}")


# UPDATE 동아리 정보
def update_club(connection):
    try:
        club_id = input("Enter the ID of the club to update: ")
        new_name = input("Enter new club name (leave blank to skip): ")
        new_description = input("Enter new description (leave blank to skip): ")
        new_member_count = input("Enter new member count (leave blank to skip): ")

        updates = []
        data = []
        if new_name:
            updates.append("name = %s")
            data.append(new_name)
        if new_description:
            updates.append("description = %s")
            data.append(new_description)
        if new_member_count:
            updates.append("member_count = %s")
            data.append(int(new_member_count))

        if not updates:
            print("No updates provided.")
            return

        query = f"UPDATE students_clubs SET {', '.join(updates)} WHERE id = %s"
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
        query = "DELETE FROM students_clubs WHERE id = %s"
        cursor.execute(query, (int(club_id),))
        connection.commit()
        print("Club deleted successfully.")
    except Error as e:
        print(f"Error: {e}")


# 메뉴 표시 및 실행
def main_menu():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    while True:
        print("\n=== Department Club Management ===")
        print("1. Add Club")
        print("2. View Clubs")
        print("3. Update Club")
        print("4. Delete Club")
        print("5. Exit")

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
            print("Exiting the program.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")


# 메인 실행
if __name__ == "__main__":
    main_menu()
