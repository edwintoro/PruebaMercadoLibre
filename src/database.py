import mysql.connector
import datetime


database = mysql.connector.CMySQLConnection(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'Laura123',
    database = 'pruebamercadolibre',
    auth_plugin='mysql_native_password'
)

if database.is_connected():
    print("conecto")
else:
    print(" no conecto")
