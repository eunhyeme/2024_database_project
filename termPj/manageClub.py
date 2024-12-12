import pymysql
from connectInfo import *

# 동아리 정보 삽입 함수
def insert_club():
    print("\n### 동아리 정보 입력 ###")
    name = input("동아리 이름을 입력하세요: ")
    website = input("동아리 웹사이트를 입력하세요: ")
    office = input("동아리 연구실을 입력하세요: ")
    president_student_id = int(input("동아리 대표 학생 ID를 입력하세요: "))
    major_research_area = input("주요 연구 분야를 입력하세요: ")

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Club (name, website, office, president_student_id, major_research_area)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, website, office, president_student_id, major_research_area))
            connection.commit()
            print(f"동아리 '{name}'가 성공적으로 추가되었습니다!")
    finally:
        connection.close()

def club_menu():
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