import streamlit as st
import pickle

# Load the movie data and similarity matrix
movies = pickle.load(open("movie_list.pkl", 'rb'))  # Ensure this is a DataFrame
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit app header
st.header("Movie Recommendation System")

# Dropdown for movie selection
selectvalue = st.selectbox("Select movie from dropdown:", movies_list)

# Recommendation function
def recommend(movie):
    # Find the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    # Get similarity scores for the selected movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # Get the top 5 recommended movies (excluding the selected movie itself)
    recommend_movie = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommend_movie

# Show recommendations on button click
if st.button("Show Recommend"):
    movie_names = recommend(selectvalue)
    # Display the recommended movies in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
    with col2:
        st.text(movie_names[1])
    with col3:
        st.text(movie_names[2])
    with col4:
        st.text(movie_names[3])
    with col5:
        st.text(movie_names[4])
