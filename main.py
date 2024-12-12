from database.crud_operations import (
    add_student, view_students, update_student, delete_student,
    register_user, login_user, get_teachers_for_student
)

if __name__ == "__main__":
    register_user('teachers', 'teacher 1', 'teacher1@school.com', 'password123')

    add_student('student 1', 'student1@student.com', 'password123')
    add_student('student 2', 'student2@student.com', 'password456')

    print("All Students:")
    view_students()

    print("Updating student1 email...")
    update_student(1, email='student1.new@student.com')

    print("Teachers for student with ID 1:")
    get_teachers_for_student(1)

    login_user('teachers', 'teacher1@school.com', 'password123')

    print("deleting student with id 2...")
    delete_student(2)
