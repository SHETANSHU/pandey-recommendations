import streamlit as st
import pandas as pd
from model import recommend

hollywood = pd.read_csv("hollywood.csv")
bollywood = pd.read_csv("bollywood.csv")

movies = pd.concat([hollywood, bollywood])

st.title("🎬 Pandey Recommendations")
st.write("Bollywood + Hollywood Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)
