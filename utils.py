import sqlite3

def get_db_connection():
    try:
        connection = sqlite3.connect("swimming_pool.db")
        return connection
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return None


