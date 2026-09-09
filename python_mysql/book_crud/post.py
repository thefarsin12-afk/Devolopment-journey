from mysql import connector

connection = connector.connect(

    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "books_db"
)

cursor = connection.cursor()

query = """
      insert into book(title,author,price) values(%s,%s,%s)
"""
values = ("The Murder on the Links","Agatha Christie ","250")

cursor.execute(query,values)

connection.commit()

print("Record has been inserted")