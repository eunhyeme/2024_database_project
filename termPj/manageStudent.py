import mysql.connector
from mysql.connector import Error
from connectInfo import *
# 학생 정보 삽입
def insert_student():
    print("\n### 학생 정보 입력 ###")
    name = input("학생 이름: ")
    student_number = input("학생 학번: ")
    gender = input("성별(남자/여자): ")
    email = input("학생 이메일: ")
    club_id = int(input("동아리 ID를 입력하세요: "))
    major = input("전공을 입력하세요: ")
    GPA = float(input("평균학점을 입력하세요: "))
    semester = int(input("학기를 입력하세요: "))
    birth_date = input("생일을 입력하세요 (YYYY-MM-DD): ")
    status = input("학적 상태를 입력하세요 (Enrolled/Leave of Absence/Military Leave/Graduated/Postponed Graduation/Graduate School): ")

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Student (name, student_number, gender, email, club_id, major, GPA, semester, birth_date, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, student_number, gender, email, club_id, major, GPA, semester, birth_date, status))
            connection.commit()
            print(f"학생 '{name}'가 성공적으로 추가되었습니다!")
    finally:
        connection.close()

#학생 정보 삭제

#학생 정보 출력

#학생 정보 수정


#학생관리 메인페이지
def student_menu():
    while True:
        print("\n")
        print("==학생관리==")
        print("1. 학생 조회")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학생 정보수정")
        print("5. 뒤로가기")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            create_tables()
        elif choice == '2':
            insert_club()
        elif choice == '3':
            insert_student()
        elif choice == '4':
            view_clubs()
        elif choice == '5':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")







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


def create_tables():
    """테이블 생성"""
    conn = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset="utf8mb4"
    )
    if conn.open:
        print("DB연결 완료.")
    else:
        print("DB연결 불가.")
        return
    cursor = conn.cursor()

    # Create Student table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        학번 INT PRIMARY KEY,
        학생이름 VARCHAR(100) NOT NULL,
        학과 VARCHAR(100) NOT NULL,
        이수학기 INT,
        성별 VARCHAR(10),
        이메일 VARCHAR(100),
        생년월일 DATE,
        성적 FLOAT,
        학적상태코드 INT,
        소속동아리번호 INT,
        FOREIGN KEY (학적상태코드) REFERENCES Status(학적상태코드),
        FOREIGN KEY (소속동아리번호) REFERENCES Club(동아리번호)
    );
    ''')

    # Create Status table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Status (
        학적상태코드 INT PRIMARY KEY,
        학적상태명 VARCHAR(100) NOT NULL
    );
    ''')

    # Create Club table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Club (
        동아리번호 INT PRIMARY KEY,
        동아리이름 VARCHAR(100) NOT NULL,
        연구실위치 VARCHAR(100),
        웹사이트 VARCHAR(100),
        주요연구분야 VARCHAR(100),
        담당교수교번 INT,
        회장학번 INT,
        FOREIGN KEY (담당교수교번) REFERENCES Professor(교번),
        FOREIGN KEY (회장학번) REFERENCES Student(학번)
    );
    ''')

    # Create Professor table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Professor (
        교번 INT PRIMARY KEY,
        교수이름 VARCHAR(100) NOT NULL,
        연구실위치 VARCHAR(100),
        이메일 VARCHAR(100),
        진임교원여부 BOOLEAN
    );
    ''')

    # Create Interest table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Interest (
        동아리번호 INT,
        연구분야 VARCHAR(100),
        PRIMARY KEY (동아리번호, 연구분야),
        FOREIGN KEY (동아리번호) REFERENCES Club(동아리번호)
    );
    ''')

    conn.commit()
    cursor.close()
    conn.close()

def add_student(학번, 학생이름, 학과, 이수학기, 성별, 이메일, 생년월일, 성적, 학적상태코드, 소속동아리번호):
    """Add a new student to the database."""
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="club_management",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Student (학번, 학생이름, 학과, 이수학기, 성별, 이메일, 생년월일, 성적, 학적상태코드, 소속동아리번호)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (학번, 학생이름, 학과, 이수학기, 성별, 이메일, 생년월일, 성적, 학적상태코드, 소속동아리번호))
    conn.commit()
    cursor.close()
    conn.close()
