import pandas as pd
import streamlit as st
import pickle
import pandas


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox('Select a movie', movies['title'].values)
#
# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)

# Function to set page configuration
# Function to set page configuration
st.set_page_config(page_title="Movie Recommender System", page_icon=":clapper:", layout="wide")

# Function to get CSS based on mode
def get_css(theme):
    if theme == "Dark":
        return """
        <style>
        .main {
            background-color: #000;
            color: #fff;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #ff4500;
            text-align: center;
        }
        .sub-title {
            font-size: 1.5em;
            color: #ff6347;
            text-align: center;
            margin-bottom: 40px;
        }
        .recommendations {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .recommendation {
            background-color: #333;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(255, 69, 0, 0.5), 0 6px 20px rgba(0, 0, 0, 0.19);
            padding: 20px;
            text-align: center;
            font-size: 1.2em;
            color: #fff;
            transition: transform 0.3s;
        }
        .recommendation:hover {
            transform: translateY(-10px);
        }
        .stButton>button {
            background-color: #ff4500;
            color: #fff;
            border: None;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #ff6347;
        }
        </style>
        """
    else:
        return """
        <style>
        .main {
            background-color: #fff;
            color: #000;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #d32f2f;
            text-align: center;
        }
        .sub-title {
            font-size: 1.5em;
            color: #e57373;
            text-align: center;
            margin-bottom: 40px;
        }
        .recommendations {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .recommendation {
            background-color: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(211, 47, 47, 0.5), 0 6px 20px rgba(0, 0, 0, 0.19);
            padding: 20px;
            text-align: center;
            font-size: 1.2em;
            color: #000;
            transition: transform 0.3s;
        }
        .recommendation:hover {
            transform: translateY(-10px);
        }
        .stButton>button {
            background-color: #d32f2f;
            color: #fff;
            border: None;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #e57373;
        }
        </style>
        """

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = "Light"

# Toggle theme button
if st.button('Toggle Theme'):
    st.session_state.theme = "Dark" if st.session_state.theme == "Light" else "Light"

# Apply CSS based on selected theme
st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<div class="title">Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Discover your next favorite movie</div>', unsafe_allow_html=True)

# Movie selection
selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown('<div class="recommendations">', unsafe_allow_html=True)
    for i in recommendations:
        st.markdown(f'<div class="recommendation">{i}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)