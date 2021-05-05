import streamlit as st 
import pandas as pd
import time
from PIL import Image

def app():
    img = Image.open('AC_icon.png')

    st.image(img, width=200)
    st.write("""
    # Animal Crossing Roledex 
    """)
    st.write("""CSC 310 Project by Lily, Carissa, and Sophia!""")
    df = pd.read_csv("villagers.csv")

    #This is the drop down box for the villagers
    animal_name = df['Name']

    #Button
    #if st.button('Click here to start!'):
    #Dropdown
    select_villagers = st.selectbox('Choose your animal crossing villager to find out more info about them!', options=animal_name, index = 0)
    #Create wait time
    with st.spinner('Please wait...'):
        time.sleep(3)
    st.balloons()
    st.write("Info about "+select_villagers+":")
    #st.success('All set!')

    #Display data related to the villager (text)
    feature_df = df.drop(['Color 2'], axis = 1)
    st.write(feature_df.loc[feature_df['Name'] == select_villagers])

    #Counting how many of each gender there is
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


    #-----------------------------------------------------------
    #Display some graphs for the main page:
    #st.subheader("For more information about the villagers keep reading!")
    st.subheader("--------------------------------------------------------")
    st.write("Below you will find different charts and graphs highlighting a few traits from all villagers")
    st.subheader("--------------------------------------------------------")
    #bar charts
    st.subheader("""Data describing the genders of the villagers""")
    st.bar_chart(gender_count)
    st.subheader("""Data describing the different species within the vilagers""")
    st.bar_chart(species_count)
    st.subheader("""Data describing the various hobbies of the villagers""")
    st.bar_chart(hobby_count)
    st.subheader("""Data describing the styles of the villagers""")
    st.bar_chart(style_count)
    #line charts
    st.subheader("""Data describing each villager's favorite color""")
    st.line_chart(color_count)
    #area charts
    st.subheader("""Data describing different personalities of the villagers""")
    st.area_chart(personality_count)
  
    #------------------------------------------------------------------------------
    
    #audio
    audio_file = open('AC_Theme.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_file, format = 'audio/mp3', start_time = 0)
