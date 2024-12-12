import pymysql
from connectInfo import *
from pymysql.cursors import DictCursor  # DictCursor 추가

def insert_club():
    print("\n### 동아리 정보 입력 ###")
    name = input("동아리 이름을 입력하세요: ")
    website = input("동아리 웹사이트를 입력하세요: ")
    office = input("동아리 연구실을 입력하세요: ")
    president_student_id = input("동아리 대표 학생 ID를 입력하세요: ")
    major_research_area = input("주요 연구 분야를 입력하세요: ")
    professor_id = input("담당 교수 교번을 입력하세요: ")

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            # 동아리 추가 쿼리
            cursor.execute("""
                INSERT INTO Club (동아리이름, 웹사이트, 연구실위치, 회장학번, 주요연구분야, 담당교수교번)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, website, office, president_student_id, major_research_area, professor_id))
            connection.commit()
            print(f"동아리 '{name}'가 성공적으로 추가되었습니다!")
    finally:
        if connection.open:
            connection.close()

# 동아리 정보 조회 함수
def view_clubs():
    connection = connect_db()
    try:
        # DictCursor 사용하여 컬럼명을 키로 사용
        with connection.cursor(DictCursor) as cursor:
            cursor.execute("SELECT * FROM Club")
            clubs = cursor.fetchall()
            print("\n### 동아리 정보 ###")
            for club in clubs:
                print(f"이름: {club['동아리이름']}({club['동아리번호']})\t| 회장학번: {club['회장학번']}\t| 주요 연구 분야: {club['주요연구분야']}")
    finally:
        connection.close()

# 동아리 삭제 함수
def delete_club():
    club_id = input("삭제할 동아리 번호를 입력하세요: ")

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Club WHERE 동아리번호 = %s", (club_id,))
            connection.commit()
            print(f"동아리 번호 '{club_id}'가 성공적으로 삭제되었습니다!")
    finally:
        connection.close()

# 동아리 회장(대표) 수정 함수
def update_club_president():
    club_id = input("회장을 변경할 동아리 번호를 입력하세요: ")
    new_president_id = input("새 회장 학번을 입력하세요: ")

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE Club
                SET 회장학번 = %s
                WHERE 동아리번호 = %s
            """, (new_president_id, club_id))
            connection.commit()
            print(f"동아리 번호 '{club_id}'의 회장이 학번 '{new_president_id}'로 변경되었습니다!")
    finally:
        connection.close()

# 동아리 관리 메뉴
def club_menu():
    while True:
        print("\n")
        print("== 동아리 관리 ==")
        print("1. 동아리 조회")
        print("2. 동아리 추가")
        print("3. 동아리 삭제")
        print("4. 동아리 회장(대표) 수정")
        print("5. 뒤로가기")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            view_clubs()
        elif choice == '2':
            insert_club()
        elif choice == '3':
            delete_club()
        elif choice == '4':
            update_club_president()
        elif choice == '5':
            print("메뉴로 돌아갑니다...")
            break
        else:
            print("올바른 번호를 선택하세요.")
