import mysql.connector
from mysql.connector import Error
from connectInfo import *

#실적관리 메인페이지
def achievement_menu():
    while True:
        print("\n")
        print("==실적 관리==")
        print("1. 실적 조회")
        print("2. 실적 추가")
        print("3. 실적 삭제")
        print("4. 뒤로가기")

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


# 실적 정보 삽입 함수
def insert_achievement():
    print("\n### 실적 정보 입력 ###")
    achievement_name = input("수상명을 입력하세요: ")
    award_date = input("수상일자를 입력하세요 (YYYY-MM-DD): ")
    club_id = int(input("동아리 ID를 입력하세요: "))

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Achievement (achievement_name, award_date, club_id)
                VALUES (%s, %s, %s)
            """, (achievement_name, award_date, club_id))
            connection.commit()
            print(f"실적 '{achievement_name}'가 성공적으로 추가되었습니다!")
    finally:
        connection.close()
