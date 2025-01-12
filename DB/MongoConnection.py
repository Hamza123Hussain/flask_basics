# models/database.py

from pymongo import MongoClient

from config import MONGO_URI, DATABASE_NAME

# MongoDB client
# Create a MongoDB client and connect to the database
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]  # Access the database

# Function to get the database instance
def get_db():
    return db
