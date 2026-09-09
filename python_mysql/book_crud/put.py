from mysql import connector

connection = connector.connect(

    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "books_db"
)

cursor = connection.cursor()

query = """update book set title=%s, author=%s, price=%s"""
values = "The Valley of Fear","Conan Doyle","260"

cursor.execute(query,values)
connection.commit()
print("record has been updated")