import streamlit as st 
import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
#import seaborn as sns
st.write("""
# Animal Crossing Roledex 
 Welcome!
""")

df = pd.read_csv("villagers.csv")

#This is the drop down box for the villagers
animal_name = df['Name']
select_villagers = st.selectbox('Choose your animal crossing villager!', options=animal_name, index = 0)

#Display data related to the villager (text)
feature_df = df.drop(['Color 2','Filename','Furniture List','Unique Entry ID','Style 2'], axis = 1)
st.write(feature_df.loc[feature_df['Name'] == select_villagers])


#Since the dataset represents qualitative data and not quantitative data
#We have to get the numerically values in order to properly display charts
#Coutning how many of each gender there is
gender_count = feature_df.value_counts("Gender")
#Counting how many of each species there is
species_count = feature_df.value_counts("Species")
#Counting how many of each personality there is 
personality_count = feature_df.value_counts("Personality")
#Counting how many of each hobby there is 
hobby_count = feature_df.value_counts("Hobby")
#Counting how many of the same style there is 
style_count = feature_df.value_counts("Style 1")
#Counting how many of the same color there is 
color_count = feature_df.value_counts("Color 1")


#------------------------------------------------------------
#Code to display all of the images of the villagers
if select_villagers == 'Admiral': 
    image = Image.open('admiral.png')
    st.image(image, caption='Admiral', width = 200)
elif select_villagers == 'Agent S':
    image = Image.open('agents.png')
    st.image(image, caption='Agent S', width = 200)
elif select_villagers == 'Agnes':
    image = Image.open('agnes.jpg')
    st.image(image, caption='Agnes', width = 200)
elif select_villagers == 'Al':
    image = Image.open('al.png')
    st.image(image, caption='Al', width = 200)
elif select_villagers == 'Alfonso':
    image = Image.open('alfonso.png')
    st.image(image, caption='Alfonso', width = 200)
elif select_villagers == 'Alice':
    image = Image.open('alice.png')
    st.image(image, caption='Alice', width = 200)
elif select_villagers == 'Alli':
    image = Image.open('alli.png')
    st.image(image, caption='Alli', width = 200)



