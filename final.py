import streamlit as st 
import pandas as pd
import time
from PIL import Image

def app():
    img = Image.open('AC_icon.png')

    #st.set_page_config(
    #    page_title='Animal Crossing Ro.',
    #    page_icon = img,
    #    initial_sidebar_state="expanded",
    #)

    st.write("""
    # Animal Crossing Roledex 
    Welcome!
    """)

    df = pd.read_csv("villagers.csv")

    #This is the drop down box for the villagers
    animal_name = df['Name']

    #Button
    #if st.button('Click here to start!'):
    #Dropdown
    select_villagers = st.selectbox('Choose your animal crossing villager!', options=animal_name, index = 0)
    #Create wait time
    with st.spinner('Please wait...'):
        time.sleep(3)
    st.success('All set!')

    #Display data related to the villager (text)
    feature_df = df.drop(['Color 2'], axis = 1)
    st.write(feature_df.loc[feature_df['Name'] == select_villagers])

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




    #fun stuff
    #st.balloons()
    #audio
    #audio_file = open('AC_Theme.mp3', 'rb')
    #audio_bytes = audio_file.read()
    #st.audio(audio_file, format = 'audio/mp3', start_time = 0)