# pip install google-genai
import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
from google import genai
from mysql import connector

connection=connector.connect(
    host="localhost",
    username="root",
    password="Password@123",
    database="customer_support_db"
)
cursor=connection.cursor()
query="select * from support_ticket where id=1;"
cursor.execute(query)
ticket=cursor.fetchone()
GEMINI_API_KEY="AQ.Ab8RN6KdQuhFkHsK3aciu_FVoC1kIos_4HMc5OIlGq5r4FQO2w"


client=genai.Client(api_key=GEMINI_API_KEY)
prompt= f"""
You are a customer support ticket analysis system.
Analyze the following support ticket.
Customer Name:
{ticket[1]}
Subject:
{ticket[3]}
Description:
{ticket[4]}
Provide the following information:
1. Category
2. Priority
3. Sentiment
4. Summary
5. Suggested response
Category must be one of:
payment
delivery
account
technical
refund
other
Priority must be one of:
low
medium
high
urgent
Sentiment must be one of:
positive
neutral
negative
Return the answer in a clear format.
"""

response=client.models.generate_content(
    model="5-flashgemini-3.",
    contents=prompt
    )
print(response)