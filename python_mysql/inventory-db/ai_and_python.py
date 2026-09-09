import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
from google import genai
from mysql import connector

connection = connector.connect(

    user ="root",
    password = "Password@123",
    host = "localhost",
    database = "inventory_db"
)

cursor = connection.cursor()
query = "select * from inventory_ where id = 1"
cursor.execute(query)
record = cursor.fetchone()

GEMINI_API_KEY ="AQ.Ab8RN6LsScORwub4wxgXBAOXWvNOMPDTtmgCyXJJKkxr0QRWWQ"

client = genai.Client(api_key=GEMINI_API_KEY)

prompt = f""
