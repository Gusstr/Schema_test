import mysql.connector, quinyx_Functions

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="",
  database="proj2",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_account")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


Do = input("ny användare /nyanv, login /login: ")

if Do == "/nyanv":
    newfirstname = input("Förnamnamn: ")
    newlastname = input("Efternamn: ")
    newpassword = input("nytt password: ")
    quinyx_Functions.new_user(newfirstname, newlastname, newpassword)