import streamlit as st
import pandas as pd
import pickle
import requests




def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distances=similarity[index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    movies_out=[]
    posters=[]
    for i in movie_list:
        movies_out.append(movies.iloc[i[0]].title)
      #  posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return movies_out,posters
        
movies_dict=pickle.load(open('datadict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommendor System')
option = st.selectbox('Choose Movie',movies['title'])
            
if st.button('Recommend'):
    names,poster=recommend(option)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        #st.text(poster[0])
    with col2:
        st.text(names[1])
        #st.text(poster[1])
    with col3:
        st.text(names[2])
        #st.image(poster[2])
    with col4:
        st.text(names[3])
        #st.image(poster[3])
    with col5:
        st.text(names[4])
        #st.image(poster[4])