from mysql import connector

connection = connector.connect(

    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "books_db"
)

cursor = connection.cursor()

query ="select * from book"

cursor.execute(query)

record = cursor

for book in record:
    print(book)
