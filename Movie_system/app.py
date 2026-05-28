# app.py


import streamlit as st

from search import search_movie
from recommender import recommend_movies


# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# ====================================
# TITLE
# ====================================

st.title("🎬 AI Movie Recommendation System")
st.write("Get movie recommendations using NLP + TF-IDF + Cosine Similarity")


# ====================================
# USER INPUT
# ====================================

movie_name = st.text_input(
    "Enter a movie name"
)


# ====================================
# SEARCH + RECOMMEND
# ====================================

if st.button("Get Recommendations"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        matches = search_movie(movie_name)

        if len(matches) == 0:
            st.error("No movie found.")

        else:

            # Create dropdown list
            movie_options = matches["title"].tolist()

            selected_movie = st.selectbox(
                "Select the correct movie",
                movie_options
            )

            if st.button("Recommend"):

                selected_index = matches[
                    matches["title"] == selected_movie
                ].index[0]

                recommendations = recommend_movies(selected_index)

                st.subheader("Recommended Movies")

                for i, row in recommendations.iterrows():

                    st.write(
                        f"🎥 {row['title']}  | ⭐ {row['avg_rating']:.2f}"
                    )
