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

# insert 
def insert_research_doc():
    collections = research_db.Research
    research_document = {
        "name" : "Panagiotis",
        "type": "Research and Asian Buddies"
    }

    inserted_id = collections.insert_one(research_document).inserted_id
    print(f"Document inserted with ID: {inserted_id}")


insert_research_doc()

# read 
def find_research_doc():
    research_collections = research_db.Research

    documents = research_collections.find({
        "name": "Panagiotis"
    })

    for document in documents:
        pprint.pprint(document)

find_research_doc()

# create doc 
def create_research_doc():
    research_collections = research_db.Research

    first_names = ["Mei" , "Hana", "Yuki"]
    last_names = ["Ruscica", "tanaka", "Batsuko"]
    ages = [25 , 27, 26]

    docs = []
    for first_names, last_names, ages in zip(first_names, last_names, ages):
        doc = {
            "first_names": first_names, "last_names": last_names, "ages": ages
        }
        docs.append(doc)

    person_collection = research_collections.insert_many(docs)

create_research_doc()    
