# db_queries.py

from .db_connection import DbConnection


class DbQueries:
    def __init__(self, config_path='../config.ini'):
        self.db_connection = DbConnection(config_path)

    def get_h1_strings(self):
        """Fetch H1 strings from the database."""
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT h1_text FROM h1_strings")
        h1_string = cursor.fetchone()
        return h1_string[0] if h1_string else None

    def get_nav_element(self):
        """Fetch navigation element from the database."""
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT nav_element FROM navbar_elements WHERE id = 1")
        nav_element = cursor.fetchone()
        return nav_element[0] if nav_element else None
