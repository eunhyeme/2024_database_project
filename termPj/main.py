import pymysql.cursors
from makeTable import *
from manageClub import *
from manageStudent import *
from manageProf import *
from manageProperty import *
import pymysql
from connectInfo import *
from termPj.maketitle import maketitle
from termPj.manageAhievement import achievement_menu


# 데이터베이스 조회 함수
def view_clubs():
    print("\n### 동아리 목록 조회 ###")
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Club")
            clubs = cursor.fetchall()
            if clubs:
                for club in clubs:
                    print(club)
            else:
                print("저장된 동아리가 없습니다.")
    finally:
        connection.close()

#메인메뉴
def main_menu():
    while True:
        print("\n")
        print("1. 동아리 관리")
        print("2. 학생 관리")
        print("3. 교수님 관리")
        print("4. 공공기물 관리")
        print("5. 동아리 실적 관리")
        print("6. 종료")

        choice = input("원하는 작업을 선택하세요 (1-6): ")

        if choice == '1':
            club_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            prof_menu()
        elif choice == '4':
            property_menu()
        elif choice == '5':
            achievement_menu()
        elif choice == '6':
            print("안녕히 가세요")
            break
        else:
            print("잘못된 값입니다. 다시 입력하세요.")

if __name__ == "__main__":
        maketitle()
        main_menu()

