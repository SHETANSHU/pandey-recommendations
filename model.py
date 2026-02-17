import pandas as pd

# Load datasets
hollywood = pd.read_csv("hollywood.csv")
bollywood = pd.read_csv("bollywood.csv")

# Rename columns so both datasets match
hollywood = hollywood.rename(columns={
    "Film": "Title",
    "Genre": "Genre"
})

bollywood = bollywood.rename(columns={
    "Movie Name": "Title",
    "Genre": "Genre"
})

# Keep only needed columns
hollywood = hollywood[["Title", "Genre"]]
bollywood = bollywood[["Title", "Genre"]]

# Combine datasets
movies = pd.concat([hollywood, bollywood])

# Clean data
movies["Title"] = movies["Title"].astype(str)
movies["Genre"] = movies["Genre"].astype(str)

def recommend(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in movies["Title"].str.lower().values:
        return ["Movie not found in database."]

    genre = movies[movies["Title"].str.lower() == movie_name]["Genre"].values[0]

    recommendations = movies[movies["Genre"] == genre]["Title"].values
    recommendations = [m for m in recommendations if m.lower() != movie_name]

    return recommendations[:5]
