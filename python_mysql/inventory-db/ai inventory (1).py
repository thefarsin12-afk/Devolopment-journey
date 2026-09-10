from google import genai
from mysql import connector

connection=connector.connect(
        username="root",
        password="Password@123",
        host="localhost",
        database="inventory_db"
)
cursor=connection.cursor()
query="select * from products_invent where Product_ID=1"
cursor.execute(query)
record=cursor.fetchone()



client=genai.Client()
prompt = f"""
You are an inventory management AI system.

Analyze the following product:

Product Name: 
{record[1]}
Category: 
{record[2]}
Quantity: 
{record[3]}
Price: 
{record[4]}

Provide:

1. Optimal reorder quantity
2. Category classification
3. Stock depletion risk
4. Summary report
5. Suggested supplier reorder email

"""

response = client.models.generate_content(
    model="gem-3.5-flash",
    contents=prompt
)

print(response)
