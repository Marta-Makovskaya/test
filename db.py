import psycopg2

DB_CONFIG = {
    "dbname": "skils",
    "user": "postgres",
    "password": "Paroll1$",
    "host": "localhost",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS programs 
        ( 
            program_id SERIAL PRIMARY KEY,
            program_name VARCHAR(100) UNIQUE
        );
        """)

        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS Instructors 
        (
            instructor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) UNIQUE,
            last_name VARCHAR(50) UNIQUE,
            email VARCHAR(100) UNIQUE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Courses  -- Specify the table name
        ( 
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            program_id INT,
            instructor_id INT,
            student_id INT,
            FOREIGN KEY (program_id) REFERENCES programs(program_id),
            FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Students 
        (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Grades 
        (
            grade_id SERIAL PRIMARY KEY,
            student_id INT,
            course_id INT,
            grade DECIMAL(3, 2) CHECK (grade >= 0 AND grade <= 100),
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );
        """)


def get_all_students():
    with connect_db() as con, con.cursor() as cur:
        cur.execute("SELECT * FROM Students")  # Added space before the asterisk (*)
        students = cur.fetchall()
        return students


def get_all_instructors():
    with connect_db() as con, con.cursor() as cur:
        cur.execute("SELECT * FROM Instructors")  # Added space before the asterisk (*)
        instructors = cur.fetchall()
        return instructors


def get_all_courses():  # Corrected the function name
    with connect_db() as con, con.cursor() as cur:
        cur.execute("SELECT * FROM Courses")  # Added space before the asterisk (*)
        courses = cur.fetchall()
        return courses


def get_all_programs():
    with connect_db() as con, con.cursor() as cur:
        cur.execute("SELECT * FROM programs")  # Added space before the asterisk (*)
        programs = cur.fetchall()
        return programs


def get_student_details(student_id):
    with connect_db() as con, con.cursor() as cur:
        cur.execute("""
        SELECT 
            s.student_id, 
            s.first_name, 
            s.last_name, 
            c.course_name, 
            g.grade 
        FROM 
            Students s 
        LEFT JOIN 
            Grades g ON s.student_id = g.student_id 
        LEFT JOIN 
            Courses c ON g.course_id = c.course_id 
        WHERE 
            s.student_id = %s;
        """, (student_id,))
        details = cur.fetchall()
        return details


# Example usage:
if __name__ == "__main__":
    init_db()  # Initialize the database
    print(get_all_students())
    print(get_all_instructors())
    print(get_all_courses())
    print(get_all_programs())