# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:06:58 2024

@author: tarun
"""

import numpy as np
import pandas as pd
import difflib
import pickle
import streamlit as st

with open('C:/Users/tarun/Documents/MachineLearning/MovieReccomendataionSystem/movie_dataset.pkl', 'rb') as f:
    movies_dataset = pickle.load(f)

with open('C:/Users/tarun/Documents/MachineLearning/MovieReccomendataionSystem/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)


movie_name = st.text_input('enter movie name : ')
n = 10

if st.button('Get Reccomendation'):
    list_of_all_titles = movies_dataset['title']
    close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    try:
      closest_match = close_match[0]
      index_of_the_movie = movies_dataset[movies_dataset.title == closest_match]['index'].values[0]
      
      similarity_score = list(enumerate(similarity[index_of_the_movie]))
      sorted_similar_movies = sorted(similarity_score, key = lambda x : x[1], reverse = True)
      
      i = 1
      
      st.success('Movie sugggestion for you : \n')
      
      for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_dataset[movies_dataset.index == index]['title'].values[0]
        st.success(title_from_index)
        i += 1
        if(i > n):
          break
    except Exception as e:
        st.success("The movie is not present currently try some diffrent movies")
