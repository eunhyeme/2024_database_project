from makeTable import *
from manageClub import *
from manageStudent import *
from manageProf import *
from manageProperty import *
import pymysql
from connectInfo import *

# MySQL 연결 함수
def connect_to_database():
    try:
        conn = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            charset="utf8mb4"
        )
        return conn
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        return None

# 1. 테이블 목록 조회
def show_tables(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("\n[테이블 목록]")
            for table in tables:
                print(f"- {table[0]}")
    except Exception as e:
        print(f"테이블 목록 조회 실패: {e}")

# 2. 데이터 삽입
def insert_data(conn, table_name):
    try:
        with conn.cursor() as cursor:
            # 테이블 컬럼 정보 가져오기
            cursor.execute(f"SHOW COLUMNS FROM {table_name};")
            columns = cursor.fetchall()
            col_names = [col[0] for col in columns]

            # 사용자로부터 데이터 입력
            print(f"{table_name} 테이블의 컬럼: {', '.join(col_names)}")
            values = tuple(input(f"{col} 값을 입력하세요: ") for col in col_names)

            # 데이터 삽입
            placeholders = ", ".join(["%s"] * len(values))
            query = f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({placeholders})"
            cursor.execute(query, values)
            conn.commit()
            print("데이터 삽입 성공!")
    except Exception as e:
        print(f"{table_name} 테이블 데이터 삽입 실패: {e}")

# 3. 데이터 삭제
def delete_data(conn, table_name):
    try:
        with conn.cursor() as cursor:
            # 삭제 조건 입력받기
            condition = input(f"{table_name} 테이블에서 삭제할 조건 (예: id=1): ")
            query = f"DELETE FROM {table_name} WHERE {condition}"
            cursor.execute(query)
            conn.commit()
            print("데이터 삭제 성공!")
    except Exception as e:
        print(f"{table_name} 테이블 데이터 삭제 실패: {e}")

# 4. 데이터 검색
def search_data(conn, table_name):
    try:
        with conn.cursor() as cursor:
            # 검색 조건 입력받기
            condition = input(f"{table_name} 테이블에서 검색할 조건 (없으면 Enter): ")
            query = f"SELECT * FROM {table_name}" + (f" WHERE {condition}" if condition else "")
            cursor.execute(query)
            rows = cursor.fetchall()
            print(f"\n[검색 결과: {table_name}]")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"{table_name} 테이블 데이터 검색 실패: {e}")

# 메인 함수
def main():
    conn = connect_to_database()
    if conn is None:
        return

    while True:
        print("\n=== DB 관리 프로그램 ===")
        print("1. 테이블 목록 보기")
        print("2. 데이터 삽입")
        print("3. 데이터 삭제")
        print("4. 데이터 검색")
        print("5. 종료")
        choice = input("선택: ")

        if choice == "1":
            show_tables(conn)
        elif choice == "2":
            table_name = input("데이터를 삽입할 테이블 이름: ")
            insert_data(conn, table_name)
        elif choice == "3":
            table_name = input("데이터를 삭제할 테이블 이름: ")
            delete_data(conn, table_name)
        elif choice == "4":
            table_name = input("데이터를 검색할 테이블 이름: ")
            search_data(conn, table_name)
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("다시 시도하세요")

    conn.close()

if __name__ == "__main__":
    main()
