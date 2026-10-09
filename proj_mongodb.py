import os
import pprint
import certifi  
from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient, collection
from pymongo.errors import ConnectionFailure


load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
user = os.environ.get("MONGODB_USER")

connection = f"mongodb+srv://{user}:{password}@cluster0.svd711w.mongodb.net/"

try:
    client = MongoClient(
        connection, serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where()
    )

    client.admin.command("ping")
    print("Connected successfully to MongoDB Atlas!")

    dbs = client.list_database_names()
    pprint.pprint(dbs)

except ConnectionFailure as e:
    print(f"Could not connect to server: {e}")


research_db = client.Research

collections = research_db.list_collection_names()
pprint.pprint(collections)

def insert_research_doc():
    collections = research_db.Research
    research_document = {
        "name" : "Panagiotis",
        "type": "Research and Asian Buddies"
    }

    inserted_id = collections.insert_one(research_document).inserted_id
    print(f"Document inserted with ID: {inserted_id}")


insert_research_doc()
