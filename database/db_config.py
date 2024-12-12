import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="student_management",
        user="test",
        password="postgres",
        host="10.10.10.129",
        port="5432"
    )
