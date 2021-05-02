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

#-----------------------------------------------------------------------
    #changes:
    #------------------------------------------------------------
    #Code to display all of the images of the villagers
    if villager_one == 'Admiral': 
        image = Image.open('admiral.png')
        st.image(image, caption='Admiral', width = 200)
    elif villager_one == 'Agent S':
        image = Image.open('agents.png')
        st.image(image, caption='Agent S', width = 200)
    elif villager_one == 'Agnes':
        image = Image.open('agnes.jpg')
        st.image(image, caption='Agnes', width = 200)
    elif villager_one == 'Al':
        image = Image.open('al.png')
        st.image(image, caption='Al', width = 200)
    elif villager_one == 'Alfonso':
        image = Image.open('alfonso.png')
        st.image(image, caption='Alfonso', width = 200)
    elif villager_one == 'Alice':
        image = Image.open('alice.png')
        st.image(image, caption='Alice', width = 200)
    elif villager_one == 'Alli':
        image = Image.open('alli.png')
        st.image(image, caption='Alli', width = 200)

        
    #Code to display the image of the second villager 
    if villager_two == 'Agent S':
        image = Image.open('agents.png')
        st.image(image, caption='Agent S', width = 200)
