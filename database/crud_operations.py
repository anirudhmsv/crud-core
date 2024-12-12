from database.db_config import get_connection
from psycopg2 import sql

def register_user(table, name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("INSERT INTO {table} (name, email, password) VALUES (%s, %s, %s)")
            .format(table=sql.Identifier(table)),
            (name, email, password)
        )
        conn.commit()
        print(f"User {name} registered successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def login_user(table, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("SELECT name, password FROM {table} WHERE email = %s")
            .format(table=sql.Identifier(table)),
            (email,)
        )
        user = cursor.fetchone()
        if user and user[1] == password:
            cursor.execute(
                "INSERT INTO logs (user_name, signed_in_time) VALUES (%s, CURRENT_TIMESTAMP)", 
                (user[0],)
            )
            conn.commit()
            print(f"Welcome {user[0]}!")
        else:
            print("Invalid email or password.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def add_student(name, email, password): 
    register_user('students', name, email, password)

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_student(student_id, name=None, email=None):
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    params = []

    if name:
        updates.append("name = %s")
        params.append(name)
    if email:
        updates.append("email = %s")
        params.append(email)

    params.append(student_id)
    query = f"UPDATE students SET {', '.join(updates)} WHERE student_id = %s"
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_teachers_for_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT teachers.teacher_id, teachers.name
        FROM student_teacher
        JOIN teachers ON student_teacher.teacher_id = teachers.teacher_id
        WHERE student_teacher.student_id = %s
    """
    cursor.execute(query, (student_id,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
