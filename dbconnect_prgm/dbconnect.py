import mysql.connector
def get_connection():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        database="cms",
        passwd="Password@123",
        auth_plugin="mysql_native_password"
    )
    return db