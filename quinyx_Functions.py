import mysql.connector, re

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="proj2",
)

# mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE User_Account ADD COLUMN mail VARCHAR(255)")
# mycursor.execute("CREATE TABLE User_Account (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), workingplace VARCHAR(255), password VARCHAR(255))")

# mycursor.execute("CREATE TABLE Admin_Account (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), companyname VARCHAR(255), password VARCHAR(255))")


def new_user(A, B, C, D):
    insertname = A + "_" + B
    mycursor = mydb.cursor()
    sql = "INSERT INTO user_account (name, mail, password) VALUES (%s, %s, %s)"
    val = (insertname, D, C)
    mycursor.execute(sql, val)
    mydb.commit()

def check_mail(A):
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
  if(re.search(regex,A)):  
      MailOK = 1  
  else:  
      MailOK = 0
  return(MailOK)
      
  

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
  myresult = mycursor.fetchall()
  for x in myresult:
    return x

def insert_schema(A, B, C):
  mycursor = mydb.cursor()
  sql = "INSERT INTO {} (date, time, work) VALUES (%s, %s, %s)".format(nameC)
  val = (A, B, C)
  mycursor.execute(sql, val)
  mydb.commit()  
  
def find_user(A):
  mycursor = mydb.cursor()
  sql = "SELECT name FROM user_account WHERE id={}".format(A)
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    return x
  mydb.commit()

def add_user(A):
  mycursor = mydb.cursor()
  sql = "UPDATE user_account SET workingplace='{}'WHERE id='{}'".format(nameC, A) #inte klar
  mycursor.execute(sql)
  mydb.commit()












