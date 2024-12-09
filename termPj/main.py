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
        print(f"MySQL 연결 오류: {e}")
        return None

# CRUD 함수들 (동아리와 교수 관리 코드 재사용)
# CREATE, READ, UPDATE, DELETE 함수들은 이전에 작성한 것을 그대로 사용

# 동아리 관리 메뉴
def club_management_menu(connection):
    while True:
        print("\n=== 동아리 관리 ===")
        print("1. 동아리 추가")
        print("2. 동아리 목록 조회")
        print("3. 동아리 수정")
        print("4. 동아리 삭제")
        print("5. 메인 메뉴로 돌아가기")

        choice = input("선택한 작업 번호를 입력하세요: ")
        if choice == "1":
            create_club(connection)
        elif choice == "2":
            read_clubs(connection)
        elif choice == "3":
            update_club(connection)
        elif choice == "4":
            delete_club(connection)
        elif choice == "5":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 교수 관리 메뉴
def professor_management_menu(connection):
    while True:
        print("\n=== 교수 관리 ===")
        print("1. 교수 추가")
        print("2. 교수 목록 조회")
        print("3. 교수 정보 수정")
        print("4. 교수 삭제")
        print("5. 메인 메뉴로 돌아가기")

        choice = input("선택한 작업 번호를 입력하세요: ")
        if choice == "1":
            create_professor(connection)
        elif choice == "2":
            read_professors(connection)
        elif choice == "3":
            update_professor(connection)
        elif choice == "4":
            delete_professor(connection)
        elif choice == "5":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 메뉴
def main_menu():
    connection = connect_to_db()
    if not connection:
        print("데이터베이스 연결에 실패했습니다.")
        return

    while True:
        print("\n=== 메인 메뉴 ===")
        print("1. 동아리 관리")
        print("2. 교수 관리")
        print("3. 프로그램 종료")

        choice = input("선택한 작업 번호를 입력하세요: ")
        if choice == "1":
            club_management_menu(connection)
        elif choice == "2":
            professor_management_menu(connection)
        elif choice == "3":
            print("프로그램을 종료합니다.")
            connection.close()
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 실행
if __name__ == "__main__":
    main_menu()
