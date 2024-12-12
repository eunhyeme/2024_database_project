# Create Student table
from mysql.connector import cursor

cursor.execute('''
 CREATE TABLE IF NOT EXISTS Student (
     학번 INT PRIMARY KEY,
     학생이름 VARCHAR(100) NOT NULL,
     학과 VARCHAR(100) NOT NULL,
     이수학기 INT,
     성별 VARCHAR(10),
     이메일 VARCHAR(100),
     생년월일 DATE,
     성적 FLOAT,
     학적상태코드 INT,
     소속동아리번호 INT,
     FOREIGN KEY (학적상태코드) REFERENCES Status(학적상태코드),
     FOREIGN KEY (소속동아리번호) REFERENCES Club(동아리번호)
 );
 ''')

# Create Status table
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Status (
     학적상태코드 INT PRIMARY KEY,
     학적상태명 VARCHAR(100) NOT NULL
 );
 ''')

# Create Club table
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Club (
     동아리번호 INT PRIMARY KEY,
     동아리이름 VARCHAR(100) NOT NULL,
     연구실위치 VARCHAR(100),
     웹사이트 VARCHAR(100),
     주요연구분야 VARCHAR(100),
     담당교수교번 INT,
     회장학번 INT,
     FOREIGN KEY (담당교수교번) REFERENCES Professor(교번),
     FOREIGN KEY (회장학번) REFERENCES Student(학번)
 );
 ''')

# Create Professor table
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Professor (
     교번 INT PRIMARY KEY,
     교수이름 VARCHAR(100) NOT NULL,
     연구실위치 VARCHAR(100),
     이메일 VARCHAR(100),
     진임교원여부 BOOLEAN
 );
 ''')

# Create Interest table
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Interest (
     동아리번호 INT,
     연구분야 VARCHAR(100),
     PRIMARY KEY (동아리번호, 연구분야),
     FOREIGN KEY (동아리번호) REFERENCES Club(동아리번호)
 );
 ''')
