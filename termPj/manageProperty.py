import mysql.connector
from mysql.connector import Error
from connectInfo import *

#공공기물관리 메인페이지
def property_menu():
    while True:
        print("\n")
        print("==공공기물 관리==")
        print("1. 공공기물 조회")
        print("2. 공공기물 추가")
        print("3. 공공기물 삭제")
        print("4. 공공기물 상태수정")
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

# 공공기물 정보 삽입 함수
def insert_propety():
    print("\n### 공공기물 정보 입력 ###")
    product_code = input("제품 코드 입력: ")
    purchase_date = input("구매일자 입력 (YYYY-MM-DD): ")
    status = input("상태 입력 (In Use/Available/Out of Order): ")
    club_id = int(input("동아리 ID를 입력하세요: "))

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Equipment (product_code, purchase_date, status, club_id)
                VALUES (%s, %s, %s, %s)
            """, (product_code, purchase_date, status, club_id))
            connection.commit()
            print(f"공공기물 '{product_code}'가 성공적으로 추가되었습니다!")
    finally:
        connection.close()
