mydb=mysql.connector.connect(
    host="localhost",
    user="yourusername",    
    password="yourpassword",
    database="alx_book_store"
)
mycursor=mydb.cursor()

mycursor.execute(""" 
CREATE TABLE IF NOT EXISTS alx_book_store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    
)
""")



