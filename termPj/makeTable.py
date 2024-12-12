# 테이블 생성 함수
def create_tables():
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            # 교수 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Professor (
                    professor_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    faculty_type ENUM('Full-time', 'Part-time') NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    office VARCHAR(100) NOT NULL
                );
            """)

            # 학생 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Student (
                    student_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    student_number VARCHAR(50) NOT NULL UNIQUE,
                    gender ENUM('Male', 'Female', 'Other') NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    club_id INT,
                    major VARCHAR(100),
                    GPA DECIMAL(3, 2),
                    semester INT,
                    birth_date DATE,
                    status ENUM('Enrolled', 'Leave of Absence', 'Military Leave', 'Graduated', 'Postponed Graduation', 'Graduate School') NOT NULL,
                    FOREIGN KEY (club_id) REFERENCES Club(club_id)
                );
            """)

            # 동아리 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Club (
                    club_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    website VARCHAR(100),
                    office VARCHAR(100),
                    president_student_id INT,
                    major_research_area VARCHAR(100),
                    FOREIGN KEY (president_student_id) REFERENCES Student(student_id)
                );
            """)

            # 실적 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Achievement (
                    achievement_id INT AUTO_INCREMENT PRIMARY KEY,
                    achievement_name VARCHAR(100),
                    award_date DATE,
                    club_id INT,
                    FOREIGN KEY (club_id) REFERENCES Club(club_id)
                );
            """)

            # 공공기물 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Equipment (
                    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
                    product_code VARCHAR(50) NOT NULL,
                    purchase_date DATE,
                    status ENUM('In Use', 'Available', 'Out of Order') NOT NULL,
                    club_id INT,
                    FOREIGN KEY (club_id) REFERENCES Club(club_id)
                );
            """)

            connection.commit()
            print("테이블이 성공적으로 생성되었습니다!")

    finally:
        connection.close()
