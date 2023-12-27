import mysql.connector
conn = mysql.connector.connect(host='localhost', password='basant1313', user='root')

if conn.is_connected():
 print("Connection Established...")