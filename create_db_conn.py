import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'liveinsights'

The preceding code shows how we are storing the CREATE statements in a Python dictionary called TABLES. We also define the database in a global variable called DB_NAME, which enables you to easily use a different schema. 
cnx = mysql.connector.connect(user='scott')
cursor = cnx.cursor()


A single MySQL server can manage multiple databases. Typically, you specify the database to switch to when connecting to the MySQL server. This example does not connect to the database upon connection, so that it can make sure the database exists, and create it if not: 
def create_database(cursor):
    try:        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
