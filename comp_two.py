import streamlit as st 
import pandas as pd
import time
from PIL import Image

def app():
    st.write("""
    # Compare Two Villagers 
    Pick two from the dropdown menu!
    """)

    df = pd.read_csv("villagers.csv")

    #This is the drop down box for the villagers
    animal_name = df['Name']
    villager_one = st.selectbox('Choose your first villager!', options=animal_name, index = 0)
    villager_two = st.selectbox('Choose your second villager!', options=animal_name, index = 0)

    #Create wait time
    with st.spinner('Please wait...'):
        time.sleep(3)
    st.success('All set!')

    #Display data related to the villager (text)
    feature_df = df.drop(['Color 2','Filename','Furniture List','Unique Entry ID','Style 2'], axis = 1)
    st.write(feature_df.loc[feature_df['Name'] == villager_one])
    st.write(feature_df.loc[feature_df['Name'] == villager_two])
