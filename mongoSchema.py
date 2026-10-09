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

def search_movies(genres, minimum_rating, limit=10):
   query = {
      "genres": {"$in": genres }, 
      "imdb.rating": {"$type": "number" ,
      "$gte": minimum_rating 
      } 
   }

   projection = { 
      "_id": 1, 
      "title": 1, 
      "year": 1, 
      "imdb.rating":1
   }

   results = list(movies.find(query, projection).sort("imdb.rating", -1).limit(limit))
   
   
   """found = False
   for movie in results: 
      found = True
      pprint.pprint(movie)

   if not found:
      print("no movie tonight") """
    
   return results   


def display_movies(results):
    if not results:
      print("no movie tonight")

    for position, movie in enumerate(results, start=1):
         title = movie.get("title", "N/A")
         year = movie.get("year", "N/A")
         rating = movie.get("imdb", {}).get("rating", "?")
         
         print(f"{position}. {title} ({year}) [ IMDb: {rating}]")
         print(f" ID: {movie['_id']} ")

if __name__ == "__main__":
   results = search_movies(
      genres = ["Action", "Adventure"], minimum_rating = 7.0, limit = 10
   )

   display_movies(results)