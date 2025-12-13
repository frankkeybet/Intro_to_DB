mycursor.execute("SELECT * FROM alx_bookstore")
myresult = mycursor.fetchall()
print(myresult)