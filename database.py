import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password123@',
            database='election_db'
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None