import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=6900,
  user="wilson",
  passwd="password",
  db="test"
)
Cursor = mydb.cursor()
sql = "SELECT * FROM test.testing"
Cursor.execute(sql)
