import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\nagal\Downloads\managedfile.csv")

print(df.head())

# importing data from python to postgre
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection details
PUBLIC_IP = "18.132.73.146"  # Replace with your PostgreSQL server IP
USERNAME = "consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"  # Default PostgreSQL port

# Establish connection using psycopg2
try:
    connection = psycopg2.connect(
        host=PUBLIC_IP,
        database=DB_NAME,
        user=USERNAME,
        password=PASSWORD,
        port=PORT
    )
    print("Connected to the PostgreSQL database successfully!")
except Exception as e:
    print("Failed to connect to the PostgreSQL database!")
    print(e)
    #ok
