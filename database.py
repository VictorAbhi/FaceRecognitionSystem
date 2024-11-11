import mysql.connector

# Function to connect to the MySQL database
class Database:
    def connect_to_db():
        try:
            # Connect to the MySQL server
            connection = mysql.connector.connect(
                host="localhost",  # XAMPP MySQL server
                user="root",       # Default user for XAMPP
                password="",       # Default password for XAMPP MySQL is an empty string
                database="face_recognition_db"  # The database you created
            )

            # Check if the connection was successful
            if connection.is_connected():
                print("Successfully connected to the database!")
                return connection
            else:
                print("Failed to connect to the database.")
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

