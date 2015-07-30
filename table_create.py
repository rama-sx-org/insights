import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'liveinsights'

TABLES = {}
TABLES['customers'] = (
    "CREATE TABLE `customers` ("
    "  `custid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `service_start_date` date NOT NULL,"
    "  `email_id` varchar(50) ,"
    "  `MTN` int(15) ,"
    "  `state` char(2) NOT NULL,"
    "  PRIMARY KEY (`custid`)"
    ") ENGINE=InnoDB")

TABLES['products'] = (
    "CREATE TABLE `products` ("
    "  `product_no` char(8) NOT NULL,"
    "  `product_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`product_no`)"
    ") ENGINE=InnoDB")

TABLES['usage'] = (
    "CREATE TABLE `usage` ("
    "  `custid` int(11) NOT NULL,"
    "  `cktid` int(11) NOT NULL,"
    "  `report_date` date NOT NULL,"
    "  `full_capacity` int(4) NOT NULL,"
    "  `current_capacity` int(4) NOT NULL,"
    "  PRIMARY KEY (`custid`,`'cktid')"
    ") ENGINE=InnoDB")

TABLES['online_profile'] = (
    "CREATE TABLE `online_profile` ("
    "  `custid` int(11) NOT NULL,"
    "  `online_user_id` varchar(16) NOT NULL,"
    "  `online_pwd` varchar(8) NOT NULL,"    
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  `status` char (1) NOT NULL,"
    "  PRIMARY KEY (`custid`)"
    ") ENGINE=InnoDB")

TABLES['cust_products'] = (
    "CREATE TABLE `cust_products` ("
    "  `custid` int(11) NOT NULL,"
    "  `product_no` char(8) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  `status` char (1) NOT NULL"    
    ") ENGINE=InnoDB")


##The preceding code shows how we are storing the CREATE statements in a Python dictionary called TABLES. We also define the database in a global variable called DB_NAME, which enables you to easily use a different schema. 
cnx = mysql.connector.connect(user='scott')
cursor = cnx.cursor()


##A single MySQL server can manage multiple databases. Typically, you specify the database to switch to when connecting to the MySQL server. This example does not connect to the database upon connection, so that it can make sure the database exists, and create it if not: 
def create_database(cursor):
    try:
        cursor.execute(
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

