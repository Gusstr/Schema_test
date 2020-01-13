import mysql.connector, quinyx_Functions

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="proj2",
)

mycursor = mydb.cursor()
#sql = "DELETE FROM admin_account WHERE password = 'xam'"
#mycursor.execute(sql)
mydb.commit()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM admin_account")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


Do = input("ny användare /nyanv, login /login, ny admin /nyadmin: ")

if Do == "/nyanv":
  newfirstname = input("Förnamnamn: ")
  newlastname = input("Efternamn: ")
  newpassword = input("nytt password: ")
  quinyx_Functions.new_user(newfirstname, newlastname, newpassword)
elif Do == "/nyadmin":
  newadminfirstname = input("Förnamnamn: ")
  newadminlastname = input("Efternamn: ")
  newadminpassword = input("nytt password: ")
  newcompanyname = input("Företagsnamn: ")
  quinyx_Functions.new_admin(newadminfirstname, newadminlastname, newadminpassword, newcompanyname)
elif Do == "/loginadmin":
  adminCname = input("Företagsnamn: ")
  adminpassword = input("lösenord: ")
  Result = quinyx_Functions.loginadmin(adminCname, adminpassword)
  if Result == 0:
    print("fel lösenord")
  elif Result == 1:
    print ("inloggad")
    print(quinyx_Functions.show_schema(adminCname))
    Do1 = input("lägg till /till: ")
    if Do1 == "/till":
      Ldag = input("dag: ")
      Ltid = input("tid: ")
      Ljobb = input("vad ska göras: ")
      quinyx_Functions.insert_schema(Ldag, Ltid, Ljobb)
    


  
  