import streamlit as st
from model import recommend

st.set_page_config(page_title="Pandey Recommendations")

st.title("🎬 Pandey Movie Recommendation System")
st.write("Developed by Shetanshu Pandey")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name:
        results = recommend(movie_name)
        st.subheader("Recommended Movies:")
        for movie in results:
            st.write(movie)
    else:
        st.warning("Please enter a movie name.")
