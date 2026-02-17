import pandas as pd

# Load datasets
hollywood = pd.read_csv("hollywood.csv")
bollywood = pd.read_csv("bollywood.csv")

# Combine both datasets
movies = pd.concat([hollywood, bollywood])

# Reset index
movies = movies.reset_index(drop=True)


def recommend(movie_name):
    movie_name = movie_name.lower()

    # Check if movie exists
    if movie_name not in movies["title"].str.lower().values:
        return ["Movie not found in database."]

    # Simple recommendation logic:
    # Recommend movies from same genre
    genre = movies[movies["title"].str.lower() == movie_name]["genre"].values[0]

    recommendations = movies[movies["genre"] == genre]["title"].values

    # Remove the searched movie from recommendations
    recommendations = [m for m in recommendations if m.lower() != movie_name]

    # Return top 5
    return recommendations[:5]
