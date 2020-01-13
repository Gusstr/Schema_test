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
    insertname = A + "_" + B
    mycursor = mydb.cursor()
    sql = "INSERT INTO admin_account (companyname, name, password) VALUES (%s, %s, %s)"
    val = (D, insertname, C)
    mycursor.execute(sql, val)
    mydb.commit()

    companyscheam = D + "_schema"
    sql = "CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, workingplace VARCHAR(255) DEFAULT '{}', time VARCHAR(255), date VARCHAR(255), work VARCHAR(255))".format(companyscheam, D)
    mycursor.execute(sql)
    mydb.commit()

def loginadmin(A, B):
  mycursor = mydb.cursor()
  sql = "SELECT password FROM admin_account WHERE companyname = %s"
  Cname = (A, )
  mycursor.execute(sql, Cname)


  myresult = mycursor.fetchall()
  
  clean_result = ""
  for x in myresult:
    password = clean_result + x[0]
  
  if password == B:
    I = 1
  else:
    I = 0
  mydb.commit()    
  return(I)

def show_schema(A):
  global nameC
  nameC = A + "_schema"
  mycursor = mydb.cursor(buffered=True)
  sql = "SELECT * FROM {}".format(nameC)
  mycursor.execute(sql)
  mydb.commit() 
  myresult = mycursor.fetchall()   #inte klart
  for x in myresult:
    return x

def insert_schema(A, B, C):
  mycursor = mydb.cursor()
  sql = "INSERT INTO {} (date, time, work) VALUES (%s, %s, %s)".format(nameC)
  val = (A, B, C)
  mycursor.execute(sql, val)
  mydb.commit()  
  









