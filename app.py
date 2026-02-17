import streamlit as st
from model import recommend

st.title("🎬 Movie Recommendation System")

st.write("Get movie recommendations based on genre.")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        results = recommend(movie_name)

        st.subheader("Recommended Movies:")
        for movie in results:
            st.write("•", movie)

