#!/usr/bin/python3
"""
Creates the database alx_book_store in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Close cursor and connection safely
        try:
            cursor.close()
            connection.close()
        except Exception:
            pass

if __name__ == "__main__":
    create_database()
