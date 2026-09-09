from google import genai

from mysql import connector

connection = connector.connect(

    user = "root"
    password = "Password@123",
    host = "localhost",
    database ="hspital_db"
)
# Summary of patient complaints for doctor quick-review
# Automated follow-up reminder messages
# Priority tagging based on symptom description