# MongoDB Movie Explorer

A learning project built with Python, PyMongo, and MongoDB Atlas,
using the `sample_mflix` dataset.

The goal is to build a movie explorer with a personal watchlist
while learning MongoDB queries, CRUD operations, relationships,
and aggregation pipelines.

## Current Features

- Connect to MongoDB Atlas using environment variables.
- Search movies by genre and minimum IMDb rating.
- Filter movies to exactly one genre from the requested list.
- Sort results by IMDb rating.
- Limit the number of results.
- Display movie titles, release years, ratings, and IDs.

For example, searching for `["Action", "Adventure"]` selects movies
whose genre array contains only `"Action"` or only `"Adventure"`.
Movies with additional genres are excluded.

## Technologies

- Python
- PyMongo
- MongoDB Atlas
- MongoDB Compass
- python-dotenv
- certifi

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd mongodb-movie-explorer
```

Replace `<repository-url>` with this repository's GitHub URL.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install pymongo python-dotenv certifi
```

### 4. Configure environment variables

Create a `.env` file in the project directory:

```env
MONGODB_USER=your_database_username
MONGODB_PWD=your_database_password
```

Use your MongoDB database user credentials, not your Atlas
website login.

Do not commit the `.env` file.

### 5. Configure MongoDB Atlas

- Load the sample dataset containing `sample_mflix`.
- Allow your current IP address in the project's IP access list.
- Give your database user read access to `sample_mflix`.
- Update the cluster hostname in the Python connection string
  to match your Atlas cluster.

Write access will be needed when watchlist and review features
are added.

### 6. Run the application

```bash
python main.py
```

Replace `main.py` if your Python file has a different name.

## Example Search

```python
results = search_movies(
    genres=["Action", "Adventure"],
    minimum_rating=7.0,
    limit=10
)

display_movies(results)
```

The search uses:

- `$in` to match one of the requested genres.
- `$size: 1` to exclude movies with additional genres.
- `$type` to select numeric IMDb ratings.
- `$gte` to apply the minimum rating.
- Projection to select the returned fields.
- Sorting and a result limit.

## Planned Features

- Add movies to a personal watchlist.
- View the watchlist with movie details using `$lookup`.
- Mark movies as watched.
- Remove movies from the watchlist.
- Add personal ratings and reviews.
- Build reports by genre, decade, and director.
- Add schema validation and unique indexes.
- Implement pagination and inspect queries with `explain()`.

## Learning Goals

- Understand MongoDB documents and collections.
- Write queries with PyMongo.
- Perform CRUD operations.
- Model relationships using references.
- Build aggregation pipelines.
- Understand validation and indexing.

## Project Status

Work in progress. Movie search is implemented.
Watchlist, reviews, and reporting are planned.
