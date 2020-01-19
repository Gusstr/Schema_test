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
  newmailuser = input("Mail: ")
  newpassword = input("nytt password: ")
  Mailresult = quinyx_Functions.check_mail(newmailuser)
  if Mailresult == 1:
    quinyx_Functions.new_user(newfirstname, newlastname, newpassword, newmailuser)
  else:
    print("ogiltig mail")
elif Do == "/nyadmin":
  newadminfirstname = input("Förnamnamn: ")
  newadminlastname = input("Efternamn: ")
  newadminpassword = input("nytt password: ")
  newcompanyname = input("Företagsnamn: ")
  quinyx_Functions.new_admin(newadminfirstname, newadminlastname, newadminpassword, newcompanyname)
elif Do == "/login":
  loginusermail = input("mail adress: ") 
  loginuserpassword = input("lösenord: ")
  resultUser = quinyx_Functions.loginuser(loginusermail, loginuserpassword)
  if resultUser == 0:
    print("fel inloggning")
  elif resultUser == 1:
    print("inloggad")
    print(quinyx_Functions.show_schemaU(loginusermail))
elif Do == "/loginadmin":
  adminCname = input("Företagsnamn: ")
  adminpassword = input("lösenord: ")
  Result = quinyx_Functions.loginadmin(adminCname, adminpassword)
  if Result == 0:
    print("fel lösenord")
  elif Result == 1:
    print ("inloggad")
    print(quinyx_Functions.show_schema(adminCname))
    Do1 = input("lägg till /till, lägg till arbetare /ny: ")
    if Do1 == "/till":
      Ldag = input("dag: ")
      Ltid = input("tid: ")
      Ljobb = input("vad ska göras: ")
      quinyx_Functions.insert_schema(Ldag, Ltid, Ljobb)
    elif Do1 == "/ny":
      FindP = input("sök efter id: ")
      print(quinyx_Functions.find_user(FindP))
      Ans = input("lägg till /ok: ")
      if Ans == "/ok":
        quinyx_Functions.add_user(FindP)


  
  