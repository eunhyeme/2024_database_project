import mysql.connector
from mysql.connector import Error
from connectInfo import *


# 실적 관리 메인페이지
def achievement_menu():
    while True:
        print("\n")
        print("==실적 관리==")
        print("1. 실적 조회")
        print("2. 실적 추가")
        print("3. 실적 삭제")
        print("4. 뒤로가기")

        choice = input("원하는 작업을 선택하세요 (1-4): ")

        if choice == '1':
            view_achievement()
        elif choice == '2':
            insert_achievement()
        elif choice == '3':
            delete_achievement()
        elif choice == '4':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


# 실적 조회 함수
def view_achievement():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Achievement")
        achievements = cursor.fetchall()
        print("\n== 실적 목록 ==")
        for achievement in achievements:
            print(f"수상식별코드: {achievement[0]}, 수상명: {achievement[1]}, 수상일자: {achievement[2]}, 동아리 ID: {achievement[3]}")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# 실적 정보 삽입 함수
def insert_achievement():
    print("\n### 실적 정보 입력 ###")
    achievement_name = input("수상명을 입력하세요: ")
    award_date = input("수상일자를 입력하세요 (YYYY-MM-DD): ")
    club_id = int(input("동아리 ID를 입력하세요: "))

    try:
        connection = connect_db()
        cursor = connection.cursor()
        insert_query = """INSERT INTO Achievement (수상명, 수상일자, 동아리ID)
                          VALUES (%s, %s, %s)"""
        cursor.execute(insert_query, (achievement_name, award_date, club_id))
        connection.commit()
        print(f"실적 '{achievement_name}'가 성공적으로 추가되었습니다!")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# 실적 삭제 함수
def delete_achievement():
    print("\n### 실적 삭제 ###")
    achievement_code = input("삭제할 실적의 수상식별코드를 입력하세요: ")

    try:
        connection =connect_db()
        cursor = connection.cursor()
        delete_query = "DELETE FROM Achievement WHERE 수상식별코드 = %s"
        cursor.execute(delete_query, (achievement_code,))
        connection.commit()
        print(f"실적 수상식별코드 {achievement_code}가 삭제되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# 호출 예시
if __name__ == "__main__":
    achievement_menu()
