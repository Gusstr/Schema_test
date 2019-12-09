import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="proj2",
)
# mycursor.execute("CREATE TABLE User_Account (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), workingplace VARCHAR(255), password VARCHAR(255))")

# mycursor.execute("CREATE TABLE Admin_Account (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), companyname VARCHAR(255), password VARCHAR(255))")


def new_user(A, B, C):
    insertname = A + "_" + B
    mycursor = mydb.cursor()
    sql = "INSERT INTO user_account (name, password) VALUES (%s, %s)"
    val = (insertname, C)
    mycursor.execute(sql, val)
    mydb.commit()

def new_admin(A, B, C, D):
    insertname = B + "_" + C
    mycursor = mydb.cursor()
    sql = "INSERT INTO admin_account (companyname, name, password) VALUES (%s, %s)"
    val = (A, insertname, C)
    mycursor.execute(sql, val)
    mydb.commit()

    companyscheam = A + "_schema"
    mycursor.execute("CREATE TABLE 'companyschema' (time VARCHAR(255), date VARCHAR(255), work VARCHAR(255)")






