# # MySQL 서버 정보
# HOST = "192.168.56.1"
# PORT = 4567         # MySQL 서버 포트
# USER = "eunhye"     # MySQL 사용자 이름
# PASSWORD = "7981"   # MySQL 비밀번호
# DATABASE = "madang" # 사용할 데이터베이스 이름
# #
import pymysql

HOST = "localhost"
PORT =3306  # MySQL 서버 포트
USER = "root"     # MySQL 사용자 이름
PASSWORD = "0000"   # MySQL 비밀번호
DATABASE = "cbnu_swclub" # 사용할 데이터베이스 이름

def connect_db():
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset="utf8mb4"
    )

