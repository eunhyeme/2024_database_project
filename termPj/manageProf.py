import mysql.connector
from mysql.connector import Error
from connectInfo import *

#공공기물관리 메인페이지
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