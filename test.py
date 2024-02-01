import sqlite3
from sqlite3 import Error

def create_registration(conn, name, email, dob):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (?, ?, ?)", (name, email, dob))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating registration: {e}")
        return None

def read_all_registrations(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Registration")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error retrieving registrations: {e}")
        return None

def update_registration(conn, reg_id, name, email, dob):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Registration SET Name=?, Email=?, DateOfBirth=? WHERE ID=?", (name, email, dob, reg_id))
        conn.commit()
        return True
    except Error as e:
        print(f"Error updating registration: {e}")
        return False

def delete_registration(conn, reg_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Registration WHERE ID=?", (reg_id,))
        conn.commit()
        return True
    except Error as e:
        print(f"Error deleting registration: {e}")
        return False

# Main function
def main():
    try:
        conn = sqlite3.connect('registration.db')
        print("Connected to SQLite database")
    except Error as e:
        print(f"Error connecting to database: {e}")
        return


    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Registration (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL,
                DateOfBirth DATE
            )
        """)
        print("Registration table created successfully")
    except Error as e:
        print(f"Error creating Registration table: {e}")

    reg_id = create_registration(conn, "John Doe", "john.doe@example.com", "1990-01-15")
    if reg_id:
        print(f"New registration created with ID: {reg_id}")

        update_result = update_registration(conn, reg_id, "John Updated", "john.updated@example.com", "1990-01-20")
        if update_result:
            print("Registration updated successfully")

        registrations = read_all_registrations(conn)
        if registrations:
            print("\nAll Registrations:")
            for row in registrations:
                print(row)

        delete_result = delete_registration(conn, reg_id)
        if delete_result:
            print("Registration deleted successfully")

    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
