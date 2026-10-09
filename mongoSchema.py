from dotenv import load_dotenv, find_dotenv
import os
import pprint
import certifi
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

#production_db = client.production
db = client["sample_mflix"]
movies = db["movies"]

def show_sample_movie():
 movie = movies.find_one()
 pprint.pprint(movie)

 if __name__ == "__main__":
    show_sample_movie()
