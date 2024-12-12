import pymysql
from pymysql import Error
from connectInfo import *


# 교수님 정보 관리 메인페이지
def prof_menu():
    while True:
        print("\n")
        print("==교수님 관리==")
        print("1. 교수님 조회")
        print("2. 교수님 추가")
        print("3. 교수님 삭제")
        print("4. 교수님 정보수정")
        print("5. 뒤로가기")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            view_professor()
        elif choice == '2':
            add_professor()
        elif choice == '3':
            delete_professor()
        elif choice == '4':
            update_professor()
        elif choice == '5':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


# 교수님 조회 함수
def view_professor():
    try:
        connection = connect_db()  # pymysql로 DB 연결
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Professor")
        professors = cursor.fetchall()
        print("\n== 교수님 목록 ==")
        for professor in professors:
            print(
                f"교번: {professor[0]}, 교수님 이름: {professor[1]}, 연구실 위치: {professor[2]}, 이메일: {professor[3]}, 진임교원여부: {professor[4]}")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:  # pymysql에서는 open 속성을 사용하여 연결 상태 확인
            cursor.close()
            connection.close()


# 교수님 추가 함수
def add_professor():
    try:
        connection = connect_db()  # pymysql로 DB 연결
        cursor = connection.cursor()
        print("\n== 교수님 추가 ==")
        교번 = input("교번을 입력하세요: ")
        교수이름 = input("교수님 이름을 입력하세요: ")
        연구실위치 = input("연구실 위치를 입력하세요: ")
        이메일 = input("이메일을 입력하세요: ")
        진임교원여부 = input("진임교원여부 (True/False): ")

        add_query = """INSERT INTO Professor (교번, 교수이름, 연구실위치, 이메일, 진임교원여부) 
                        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(add_query, (교번, 교수이름, 연구실위치, 이메일, 진임교원여부))
        connection.commit()
        print("교수님이 추가되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:  # pymysql에서는 open 속성을 사용하여 연결 상태 확인
            cursor.close()
            connection.close()


# 교수님 삭제 함수
def delete_professor():
    try:
        connection = connect_db()  # pymysql로 DB 연결
        cursor = connection.cursor()
        print("\n== 교수님 삭제 ==")
        교번 = input("삭제할 교수님의 교번을 입력하세요: ")

        delete_query = "DELETE FROM Professor WHERE 교번 = %s"
        cursor.execute(delete_query, (교번,))
        connection.commit()
        print(f"교수님 교번 {교번}이(가) 삭제되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:  # pymysql에서는 open 속성을 사용하여 연결 상태 확인
            cursor.close()
            connection.close()


# 교수님 정보 수정 함수
def update_professor():
    try:
        connection = connect_db()  # pymysql로 DB 연결
        cursor = connection.cursor()
        print("\n== 교수님 정보 수정 ==")
        교번 = input("수정할 교수님의 교번을 입력하세요: ")
        교수이름 = input("새 교수님 이름을 입력하세요: ")
        연구실위치 = input("새 연구실 위치를 입력하세요: ")
        이메일 = input("새 이메일을 입력하세요: ")
        진임교원여부 = input("새 진임교원여부 (True/False): ")

        update_query = """UPDATE Professor 
                          SET 교수이름 = %s, 연구실위치 = %s, 이메일 = %s, 진임교원여부 = %s 
                          WHERE 교번 = %s"""
        cursor.execute(update_query, (교수이름, 연구실위치, 이메일, 진임교원여부, 교번))
        connection.commit()
        print(f"교수님 교번 {교번}의 정보가 수정되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:  # pymysql에서는 open 속성을 사용하여 연결 상태 확인
            cursor.close()
            connection.close()


# 호출 예시
if __name__ == "__main__":
    prof_menu()
