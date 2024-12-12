import pymysql
from connectInfo import *


# 학생 정보 출력
def show_student():
    connection = connect_db()  # connect_db()로 MySQL 연결
    try:
        with connection.cursor() as cursor:
            # Student 테이블에서 모든 학생 정보 조회
            query = "SELECT * FROM Student"
            cursor.execute(query)

            # 결과 출력
            students = cursor.fetchall()  # 모든 행을 가져옴

            if students:
                for student in students:
                    학번, 학생이름, 학과, 이수학기, 성별, 이메일, 생년월일, 성적, 학적상태코드, 소속동아리번호 = student
                    print(
                        f"학번: {학번}, 이름: {학생이름}, 학과: {학과}, 이수학기: {이수학기}, 성별: {성별}, 이메일: {이메일}, 생년월일: {생년월일}, 성적: {성적}, 학적상태코드: {학적상태코드}, 소속동아리번호: {소속동아리번호}")
            else:
                print("학생 정보가 없습니다.")
    finally:
        connection.close()

# 학생 정보 삽입
def insert_student():
    print("\n### 학생 정보 입력 ###")

    # 학생 이름 입력
    while True:
        name = input("학생 이름: ")
        if name.strip():
            break
        print("학생 이름은 비워둘 수 없습니다.")

    # 학번 입력
    student_number = input("학생 학번: ")

    # 성별 입력
    while True:
        gender = input("성별(번호입력 - 0:남자/1:여자): ")
        if gender in ['0', '1']:
            break
        print("성별은 '0' 또는 '1'로 입력해야 합니다.")

    # 이메일 입력
    while True:
        email = input("학생 이메일: ")
        if "@" in email and "." in email:
            break
        print("유효한 이메일 주소를 입력하세요 (예: example@example.com).")

    # 동아리 번호 입력
    while True:
        try:
            club_id = int(input("동아리 번호를 입력하세요 \n(0.무소속 /1.cuvic / 2.nova / 3.emsys / 4.PDA / 5.sammaru / 6.TUX / 7.nestnet): "))
            if 0 <= club_id <= 7:
                break
            print("동아리 번호는 0에서 7 사이의 숫자를 입력해야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    # 전공 입력
    while True:
        major = input("학과를 입력하세요: ")
        if major.strip():
            break
        print("학과는 비워둘 수 없습니다.")

    # 평균 학점 입력
    while True:
        try:
            GPA = float(input("평균 학점을 입력하세요 (0.0 ~ 4.5): "))
            if 0.0 <= GPA <= 4.5:
                break
            print("평균 학점은 0.0에서 4.5 사이의 값을 입력해야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    # 학기 입력
    while True:
        try:
            semester = int(input("학기를 입력하세요 (1 이상): "))
            if semester > 0:
                break
            print("학기는 1 이상의 숫자를 입력해야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    # 생일 입력
    while True:
        birth_date = input("생일을 입력하세요 (YYYY-MM-DD): ")
        try:
            import datetime
            datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            break
        except ValueError:
            print("생일은 'YYYY-MM-DD' 형식으로 입력해야 합니다.")

    # 학적 상태 입력
    status_dict = {
        '재학': 1,
        '휴학': 2,
        '군휴학': 3,
        '졸업': 4,
        '졸업유예': 5,
        '대학원': 6
    }
    while True:
        status = input("학적 상태를 입력하세요 (재학/휴학/군휴학/졸업/졸업유예/대학원): ")
        if status in status_dict:
            status_code = status_dict[status]
            break
        print("학적 상태는 '재학', '휴학', '군휴학', '졸업', '졸업유예', '대학원' 중 하나로 입력해야 합니다.")

    # 데이터베이스 연결 및 삽입
    connection = connect_db()  # connect_db()는 pymysql 또는 mysql.connector를 사용하여 연결하는 함수
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Student (학생이름, 학번, 성별, 이메일, 소속동아리번호, 학과, 성적, 이수학기, 생년월일, 학적상태코드)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, student_number, gender, email, club_id, major, GPA, semester, birth_date, status_code))
            connection.commit()
            print(f"학생 '{name}'가 성공적으로 추가되었습니다!")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        connection.close()

def update_student():
    student_number = input("수정할 학생의 학번을 입력하세요: ")

    # 데이터베이스 연결
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            # 학생의 현재 정보 조회
            cursor.execute("SELECT 학번, 학생이름, 학과, 이메일, 학적상태코드 FROM Student WHERE 학번 = %s", (student_number,))
            student = cursor.fetchone()

            if student:
                # 학생 정보 출력
                print(f"학생 정보: 학번={student[0]}, 이름={student[1]}, 학과={student[2]}, 이메일={student[3]}, 학적 상태코드={student[4]}")

                # 학적 상태를 사용자에게 입력받기
                new_status = input("새 학적 상태를 입력하세요 (재학/휴학/군휴학/졸업/졸업유예/대학원): ")

                # 학적 상태에 맞는 학적상태코드 얻기 (예: 재학 -> 1)
                status_dict = {
                    '재학': 1,
                    '휴학': 2,
                    '군휴학': 3,
                    '졸업': 4,
                    '졸업유예': 5,
                    '대학원': 6
                }
                new_status_code = status_dict.get(new_status, None)

                if new_status_code:
                    # 학적 상태 코드 업데이트
                    cursor.execute("""
                        UPDATE Student
                        SET 학적상태코드 = %s
                        WHERE 학번 = %s
                    """, (new_status_code, student_number))
                    connection.commit()
                    print(f"학생 {student_number}의 학적 상태를 '{new_status}'(으)로 업데이트 했습니다!")
                else:
                    print("잘못된 학적 상태가 입력되었습니다.")
            else:
                print("해당 학번의 학생을 찾을 수 없습니다.")
    finally:
        connection.close()

def delete_student():
    # 삭제 방법 선택
    choice = input("학생을 삭제하는 방법을 선택하세요:\n1. 졸업인 학생 삭제(용량정리)\n2. 특정 학생 삭제\n선택 (1 또는 2): ")

    # 데이터베이스 연결
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            if choice == '1':
                # 학적 상태가 졸업인 학생조회
                cursor.execute("""
                    SELECT 학번, 학생이름 FROM Student
                    WHERE 학적상태코드 = (SELECT 학적상태코드 FROM Status WHERE 학적상태명 = '졸업')
                """)
                students = cursor.fetchall()

                if students:
                    print("학적 상태가 '졸업'인 학생들:")
                    for student in students:
                        print(f"학번: {student[0]}, 이름: {student[1]}")

                    # 졸업한 학생 삭제
                    delete_confirm = input("위 학생들을 삭제하시겠습니까? (y/n): ")
                    if delete_confirm.lower() == 'y':
                        cursor.execute("""
                            DELETE FROM Student
                            WHERE 학적상태코드 = (SELECT 학적상태코드 FROM Status WHERE 학적상태명 = '졸업')
                        """)
                        connection.commit()
                        print("졸업한 학생들이 삭제되었습니다.")
                    else:
                        print("삭제가 취소되었습니다.")
                else:
                    print("학적 상태가 '졸업'인 학생이 없습니다.")

            elif choice == '2':
                # 특정 학번을 입력받아 삭제
                student_number = input("삭제할 학생의 학번을 입력하세요: ")

                # 학생 정보 조회
                cursor.execute("SELECT 학번, 학생이름 FROM Student WHERE 학번 = %s", (student_number,))
                student = cursor.fetchone()

                if student:
                    print(f"삭제할 학생: 학번={student[0]}, 이름={student[1]}")
                    delete_confirm = input("이 학생을 삭제하시겠습니까? (y/n): ")
                    if delete_confirm.lower() == 'y':
                        cursor.execute("DELETE FROM Student WHERE 학번 = %s", (student_number,))
                        connection.commit()
                        print(f"학번 {student_number} 학생이 삭제되었습니다.")
                    else:
                        print("삭제가 취소되었습니다.")
                else:
                    print("해당 학번의 학생을 찾을 수 없습니다.")
            else:
                print("잘못된 선택입니다. 1 또는 2를 선택하세요.")

    finally:
        connection.close()

# 학생관리 메인페이지
def student_menu():
    while True:
        print("\n")
        print("==학생관리==")
        print("1. 학생 조회")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학적상태 수정")
        print("5. 뒤로가기")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            show_student()
        elif choice == '2':
            insert_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
