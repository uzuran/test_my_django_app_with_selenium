"""Database queries"""
from utils.db_connection import get_db_connection


def get_h1_strings_from_db():
    """Get the H1 string from the database."""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT h1_text FROM h1_strings")
    h1_string = cursor.fetchone()
    connection.close()

    return h1_string[0] if h1_string else None  # Return the first element of the tuple
