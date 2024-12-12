import pymysql
from pymysql import Error
from connectInfo import *


# 공공기물 관리 메인페이지
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
            view_property()
        elif choice == '2':
            insert_property()
        elif choice == '3':
            delete_property()
        elif choice == '4':
            update_property_status()
        elif choice == '5':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


# 공공기물 조회 함수
def view_property():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        # 동아리별 제품 목록 조회
        query = """
                SELECT Club.동아리이름, Property.제품식별코드
                FROM Property
                JOIN Club ON Property.소유상태번호 = Club.동아리번호
                ORDER BY Club.동아리이름;
            """
        cursor.execute(query)
        results = cursor.fetchall()

        # 동아리별 제품 식별 코드를 그룹화하여 출력
        property_dict = {}

        for row in results:
            club_name = row[0]
            product_code = row[1]
            if club_name in property_dict:
                property_dict[club_name].append(product_code)
            else:
                property_dict[club_name] = [product_code]

        print("\n== 동아리별 공공기물 목록 ==")
        for club_name, product_codes in property_dict.items():
            print(f"\n동아리: {club_name}")
            print("제품 식별 코드: " + ", ".join(map(str, product_codes)))

    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()

# 공공기물 정보 삽입 함수
def insert_property():
    print("\n### 공공기물 정보 입력 ###")
    product_code = input("제품 코드 입력: ")
    purchase_date = input("구매일자 입력 (YYYY-MM-DD): ")
    status = input("소유중인 동아리번호: ")

    try:
        connection = connect_db()
        cursor = connection.cursor()
        insert_query = """INSERT INTO Property (제품식별코드, 구매시기, 소유상태번호)
                          VALUES (%s, %s, %s)"""
        cursor.execute(insert_query, (product_code, purchase_date, status))
        connection.commit()
        print(f"공공기물 '{product_code}'가 성공적으로 추가되었습니다!")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()


# 공공기물 삭제 함수
def delete_property():
    print("\n### 공공기물 삭제 ###")
    product_code = input("삭제할 공공기물의 제품 코드를 입력하세요: ")

    try:
        connection = connect_db()
        cursor = connection.cursor()
        delete_query = "DELETE FROM Property WHERE 제품식별코드 = %s"
        cursor.execute(delete_query, (product_code,))
        connection.commit()
        print(f"공공기물 제품 코드 {product_code}가 삭제되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()


# 공공기물 상태 수정 함수
def update_property_status():
    print("\n### 공공기물 상태 수정 ###")
    product_code = input("상태를 수정할 공공기물의 제품 코드를 입력하세요: ")
    new_status = input("새로운 소유 동아리 번호를 입력하세요: ")

    try:
        connection = connect_db()
        cursor = connection.cursor()
        update_query = "UPDATE Property SET 소유상태번호 = %s WHERE 제품식별코드 = %s"
        cursor.execute(update_query, (new_status, product_code))
        connection.commit()
        print(f"공공기물 제품 코드 {product_code}의 상태가 '{new_status}'로 수정되었습니다.")
    except Error as e:
        print(f"에러 발생: {e}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()


# 호출 예시
if __name__ == "__main__":
    property_menu()
