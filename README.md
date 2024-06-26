# Content-Based Movie Recommendation System (TASK 4 CODSOFT)

This repository contains a simple content-based movie recommendation system implemented using machine learning techniques. The system recommends 5 movies similar to the user's choice based on textual features.

## Steps Involved

1. **Importing Dataset:** 
   - The dataset was sourced from Kaggle's TMDB dataset.
   
2. **Understanding the Data:** 
   - Analyzed and explored the structure and content of the dataset.
   
3. **Preprocessing Data:** 
   - Cleaned and prepared the dataset for modeling.
   
4. **Data Formatting:** 
   - Organized the dataset into a suitable format for building the recommendation system.
   
5. **Text Vectorization (Bag of Words):** 
   - Converted text data (movie descriptions) into numerical vectors using the Bag of Words technique.
   
6. **Cosine Distance Calculation:** 
   - Computed cosine distances between movies based on their vectorized descriptions to measure similarity.
   
7. **Main Recommendation Function:** 
   - Developed the core function to recommend 5 most similar movies for any given user choice.
   
8. **Deployment:** 
   - Deployed the recommendation system using Streamlit.
   
## Website Link

Check out the deployed recommendation system [here](https://movie-recommender-system-bms.streamlit.app/).

## Tools and Environment

- **IDE:** PyCharm Community Edition
- **Frontend Language:** Python
- **Deployment:** Streamlit
