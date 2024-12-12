# 2024_database_project
이 페이지는 충북대학교 2024-2 데이터베이스시스템 - Term Project 레포지토리입니다.
---

- 시작 전, connectInfo.py를 통해 개인 서버의 내용을 등록하세요
- pymysql라이브러리를 설치하세요
---
## 파일 설명
- connectInfo.py
  - host, server 정보
- manageAchievement.py
  - 성과테이블 관리 모듈 (미완)
- manageClub.py
  - 동아리테이블 관리 모듈
- manageProf.py
  - 교수님테이블 관리 모듈
- manageProperty.py
  - 공공기물테이블 관리 모듈
- manageStudent.py
  - 학생테이블 관리 모듈
---
## 실행 방법
mysql서버를 가동하신 상태에서 
1. swclub db를 생성하신 뒤,
2. 아래 테이블 생성 쿼리를 넣어 테이블을 만들고,
3. 더 아래 더미데이터를 넣어 초기값을 넣어주세요

term_project 파일 속 main.py를 실행하면
프로그램이 시작됩니다!


---
## 테이블 생성 쿼리
CREATE TABLE Status (
    학적상태코드 INT UNSIGNED PRIMARY KEY,
    학적상태명 VARCHAR(50)
);

CREATE TABLE Professor (
    교번 INT UNSIGNED PRIMARY KEY,
    교수이름 VARCHAR(30),
    연구실위치 VARCHAR(100),
    이메일 VARCHAR(100),
    진임교원여부 BOOLEAN
);

CREATE TABLE Student (
    학번 INT UNSIGNED PRIMARY KEY,
    학생이름 VARCHAR(30),
    학과 VARCHAR(50),
    이수학기 INT,
    성별 CHAR(1),
    이메일 VARCHAR(100),
    생년월일 DATE,
    성적 FLOAT,
    학적상태코드 INT UNSIGNED,
    소속동아리번호 INT,
    FOREIGN KEY (학적상태코드) REFERENCES Status(학적상태코드),
    FOREIGN KEY (소속동아리번호) REFERENCES Club(동아리번호)
);

CREATE TABLE Club (
    동아리번호 INT NOT NULL AUTO_INCREMENT,
    동아리이름 VARCHAR(50) NOT NULL,
    연구실위치 VARCHAR(100),
    웹사이트 VARCHAR(100),
    주요연구분야 VARCHAR(100),
    담당교수교번 INT UNSIGNED,
    회장학번 INT UNSIGNED,
    PRIMARY KEY (동아리번호),
     FOREIGN KEY (담당교수교번) REFERENCES Professor(교번),
    FOREIGN KEY (회장학번) REFERENCES Student(학번)
);

CREATE TABLE Interest (
    동아리번호 INT,
    연구분야 VARCHAR(100),
    PRIMARY KEY (동아리번호, 연구분야),
    FOREIGN KEY (동아리번호) REFERENCES Club(동아리번호)
);

CREATE TABLE Property (
    제품식별코드 INT PRIMARY KEY,
    구매시기 DATE,
    소유상태번호 INT
);

CREATE TABLE Achievement (
    수상식별코드 INT PRIMARY KEY,
    수상시기 DATE,
    수상명 VARCHAR(100)
);

CREATE TABLE BeAwarded (
    학번 INT UNSIGNED,
    수상식별코드 INT,
    PRIMARY KEY (학번, 수상식별코드),
    FOREIGN KEY (학번) REFERENCES Student(학번),
    FOREIGN KEY (수상식별코드) REFERENCES Achievement(수상식별코드)
);


---
## 테이블 초기화 더미 데이터


INSERT INTO Status (학적상태코드, 학적상태명) VALUES
(1, '재학'),
(2, '휴학'),
(3, '졸업'),
(4, '제적'),
(5, '졸업유예'),
(6, '대학원');

-- 학생 테이블에 더미 데이터 삽입
INSERT INTO Student (학번, 학생이름, 학과, 이수학기, 성별, 이메일, 생년월일, 성적, 학적상태코드, 소속동아리번호) VALUES
(1001, '홍길동', '소프트웨어학부', 3, 'M', 'hong@university.ac.kr', '2001-04-01', 4.0, 1, 1), -- 회장 (cuvic)
(1002, '김영희', '소프트웨어학부', 2, 'F', 'kim@university.ac.kr', '2002-05-02', 3.5, 1, 2), -- 회장 (nova)
(1003, '박철수', '소프트웨어학부', 4, 'M', 'park@university.ac.kr', '2000-06-03', 3.8, 1, 3), -- 회장 (emsys)
(1004, '최민지', '소프트웨어학부', 1, 'F', 'choi@university.ac.kr', '2003-07-04', 3.9, 1, 4), -- 회장 (PDA)
(1005, '이수지', '경영학과', 1, 'F', 'lee@university.ac.kr', '2003-08-05', 3.6, 1, 0), -- 무소속 (0)
(1006, '정하나', '소프트웨어학부', 3, 'F', 'jeong@university.ac.kr', '2001-09-06', 3.7, 1, 5), -- 회장 (sammaru)
(1007, '김유진', '생명과학과', 2, 'F', 'kim2@university.ac.kr', '2002-10-07', 3.5, 1, 6), -- 회장 (TUX)
(1008, '이현수', '소프트웨어학부', 4, 'M', 'lee2@university.ac.kr', '2000-11-08', 3.9, 1, 7); -- 회장 (nestnet)


INSERT INTO Property (제품식별코드, 구매시기, 소유상태번호) VALUES
(1, '2023-05-15', 1),
(2, '2023-06-20', 2),
(3, '2023-07-10', 1),
(4, '2023-08-25', 3),
(5, '2023-09-05', 2),
(6, '2023-10-15', 3),
(7, '2023-11-12', 1),
(8, '2023-12-01', 2);
