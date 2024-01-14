# Movie-Recommender-Sytem

## Overview

This Movie Recommender System is designed to provide personalized movie recommendations based on user preferences. The system utilizes data from The Movie Database (TMDb) API, specifically the datasets `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. These datasets contain information about movies, including details, credits, cast, crew, and more.

## Tools and Technology Used

### Programming Language
   Python

### Libraries
   - **Pandas and NumPy:** Data manipulation and analysis.
   - **Scikit-learn:** Calculating cosine similarity for recommendations.
   - **NLTK (Natural Language Toolkit):** Natural Language Processing (NLP) for tokenization and stemming.
   
### Web Application Framework
   - **Streamlit:** Framework for the development of an interactive web application.
   
### Object Serialization
   - **Pickle module:** Used for object serialization.
   - **Plyer module:** Integrated for the notification feature.

## Phases of Project

### DATASET LOADING
### DATA CLEANING
### FEATURE SELECTION
### TEXT PROCESSING
### VECTORIZATION
### SIMILARITY CALCULATION
### RECOMMENDATION FUNCTION
### BUILDING THE INTERFACE

### Image for User Interface
![image](https://github.com/ishi-ag27/Movie-Recommender-Sytem/assets/120496566/5e756f45-456b-48d0-b909-cbe4cc31edd2)

## Discussion 

1. ### System Performance
   Users are provided a well-curated list of recommended movies based on content features, including cast, crew, genres, and keywords.

2. ### User Interactions
   The Streamlit web application provides an intuitive and user-friendly interface, allowing users to search for movie recommendations effortlessly. The drop-down menu simplifies the selection process, and movie posters make the recommendations more interesting.

3. ### Similarity Measure
   The cosine similarity metric effectively captures content-based relationships between movies, ensuring that recommended items...
