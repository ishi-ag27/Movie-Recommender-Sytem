import streamlit as st
import pickle
import pandas as pd
import requests
import plyer

# Function to fetch movie poster
def fetch_poster(movie_id):
     # Make a GET request to the movie database API with the provided movie_id
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=060f13bde6df8373b610452a2da47e80&language=en-US')
      # Parse the JSON response
    data = response.json()
     # Extract the poster path from the response data
    poster_path = data['poster_path']
     # Construct the full path to the movie poster image using the poster_path
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Function to process user rating
def process_rating(selected_movie_name, user_rating):
    # Process the rating here
    return f'You rated "{selected_movie_name}" as: {user_rating} stars'

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit styling
st.set_page_config(page_title="🎬 Movie Recommender System", page_icon="🍿", layout="wide")

# Main title
st.title('Discover Your Next Favorite Movie!')

# Select box for movie
selected_movie_name = st.selectbox('🎥 Select a Movie', movies['title'].values)

# Initialize names variable outside the button click scope
names = []

# Button for fetching recommendations
if st.button('🚀 Get Recommendations'):
    with st.spinner("Fetching Recommendations..."):
        # Update the names variable
        names, posters = recommend(selected_movie_name)

    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0], width=200)
    with col2:
        st.text(names[1])
        st.image(posters[1], width=200)
    with col3:
        st.text(names[2])
        st.image(posters[2], width=200)
    with col4:
        st.text(names[3])
        st.image(posters[3], width=200)
    with col5:
        st.text(names[4])
        st.image(posters[4], width=200)

# Dropdown for rating
user_rating = st.selectbox('🌟 Rate the movie:', [1, 2, 3, 4, 5], index=2)
result = process_rating(selected_movie_name, user_rating)
st.write(result)

# Send a notification
notification_title = "🎬 Movie Recommendations"
notification_message = f"Check out these movie recommendations: {', '.join(names)}"

try:
    plyer.notification.notify(
        title=notification_title,
        message=notification_message,
        app_name='Movie Recommender System',
        app_icon=None,
        timeout=10
    )
except Exception as e:
    print(f"Notification failed: {e}")
