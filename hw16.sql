CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL
);

CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    program_id INT,
    instructor_id INT,
    FOREIGN KEY (program_id) REFERENCES Programs(program_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade DECIMAL(3, 2) CHECK (grade >= 0 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Programs (program_name) 
VALUES ('Data Science') 
RETURNING program_id;

INSERT INTO Courses (course_name, program_id, instructor_id) 
VALUES ('Introduction ', 1, 1);

INSERT INTO students (student_id, first_name, last_name, email) 
VALUES (1,'Victory ', 'Born', 'vic@gmail.com')

DELETE FROM Courses WHERE course_id = 1;

INSERT INTO Instructors (first_name, last_name, email) 
VALUES ('John', 'Doe', 'john.doe@example.com') 
RETURNING instructor_id;

UPDATE Instructors 
SET email = 'new-email@example.com' 
WHERE instructor_id = 1;

SELECT Courses.course_name, Programs.program_name, Instructors.first_name, Instructors.last_name
FROM Courses
JOIN Programs ON Courses.program_id = Programs.program_id
JOIN Instructors ON Courses.instructor_id = Instructors.instructor_id;

SELECT AVG(grade) AS average_grade 
FROM Grades 
WHERE student_id = 1 AND course_id = 1;

SELECT Courses.course_name 
FROM Courses 
JOIN Programs ON Courses.program_id = Programs.program_id 
WHERE Programs.program_name = 'Data Science';

SELECT * FROM Instructors WHERE first_name LIKE 'Anna' OR last_name LIKE 'Smith';
