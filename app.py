import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=aac0880394c07021c622ec904a5264f6&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


API_KEY = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

        return None

    except requests.exceptions.RequestException as e:
        print(f"TMDB API error: {e}")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances.tolist())), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Which movies would you like me to recommend?",
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])
        else:
            st.image("https://via.placeholder.com/500x750?text=No+Poster+Available")

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])
        else:
            st.image("https://via.placeholder.com/500x750?text=No+Poster+Available")

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])
        else:
            st.image("https://via.placeholder.com/500x750?text=No+Poster+Available")

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])
        else:
            st.image("https://via.placeholder.com/500x750?text=No+Poster+Available")

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
        else:
            st.image("https://via.placeholder.com/500x750?text=No+Poster+Available")
