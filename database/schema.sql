CREATE DATABASE student_management;

\c student_management;

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE student_teacher (
    student_id INT REFERENCES students (student_id),
    teacher_id INT REFERENCES teachers (teacher_id),
    PRIMARY KEY (student_id, teacher_id)
);

CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    signed_in_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);