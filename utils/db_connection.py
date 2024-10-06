# db_connection.py
import configparser
import mysql.connector


class DbConnection:
    def __init__(self, config_path='config.ini'):
        self.config = self._load_config(config_path)
        self.connection = None

    def _load_config(self, config_path):
        """Load database configuration from a config file."""
        config = configparser.ConfigParser()
        config.read(config_path)
        return {
            'host': config['mysql']['host'],
            'user': config['mysql']['user'],
            'password': config['mysql']['password'],
            'database': config['mysql']['database']
        }

    def get_connection(self):
        """Establish and return a database connection."""
        if self.connection is None:
            self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
