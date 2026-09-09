from mysql import connector

connection=connector.connect(

        user="root",
        password="Password@123",
        host="localhost",
        database="song_db"
    )
    
cursor=connection.cursor()


query = """
       insert into song (title,track_number,singer,movie) values (%s,%s,%s,%s)
"""

values = ("abc","01","abcd","singer1")
values = ("bca","02","dcba","singer2")

cursor.execute(query,values)

connection.commit()

connection.close()
print("recorded has been inserted...")