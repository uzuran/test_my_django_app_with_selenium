import mysql.connector

import configparser

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

# Now you can use the config data for database connection


def get_db_connection():
    # Directly specify your database connection parameters here
    connection = mysql.connector.connect(**db_config)
    return connection
