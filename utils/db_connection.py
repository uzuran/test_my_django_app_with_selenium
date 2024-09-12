"""Database connection"""
import configparser
import mysql.connector

# Create a parser object
config = configparser.ConfigParser()

# Read the config.ini file using relative path
config.read('../config.ini')

# Fetching the values from the file
db_config = {
    'host': config['mysql']['host'],
    'user': config['mysql']['user'],
    'password': config['mysql']['password'],
    'database': config['mysql']['database']
}


def get_db_connection():
    """Return: connection for MySql"""
    connection = mysql.connector.connect(**db_config)
    return connection
