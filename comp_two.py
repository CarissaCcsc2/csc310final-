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
    feature_df = df.drop(['Color 2','Filename','Furniture List','Unique Entry ID','Style 2'], axis = 1)

    #This is the drop down box for the first villager
    animal_name = df['Name']
    villager_one = st.selectbox('Choose your first villager!', options=animal_name, index = 0)

    #Create wait time
    with st.spinner('Please wait...'):
        time.sleep(3)
    #st.success('All set!')
    st.write(feature_df.loc[feature_df['Name'] == villager_one])

    #This is the drop down box for the first villager
    villager_two = st.selectbox('Choose your second villager!', options=animal_name, index = 0)

    #Create wait time
    with st.spinner('Please wait...'):
        time.sleep(3)
    #st.success('All set!')
    st.balloons()
    st.write(feature_df.loc[feature_df['Name'] == villager_two])
  
    #Initialize variables to hold the index of our villagers
    count_v_1 = -1
    count_v_2 = -1

    #For loop to find the index for villager 1
    for x in range(393):
        count_v_1+=1
        if(feature_df.Name[x]== villager_one):
            break

    #For loop to find the index for villager 2
    for x in range(393):
        count_v_2+=1
        if(feature_df.Name[x]== villager_two):
            break

    #Variables to hold the species for each villager
    vill_one_spec = feature_df.iloc[count_v_1,1]
    vill_two_spec = feature_df.iloc[count_v_2,1]

    #Drop columns that aren't related to species and name
    second_feature = feature_df.drop(['Gender', 'Personality', 'Hobby', 'Birthday', 'Catchphrase','Favorite Song','Style 1', 'Color 1', 'Wallpaper', 'Flooring'], axis = 1)
    
    #Text Display
    st.title("Who else belongs to those species?")
    st.title("===========================")

    #Display all villagers of the same species for villager 1
    st.subheader("Here are all villagers of the "+vill_one_spec+" species:")
    st.dataframe(second_feature[df["Species"]==vill_one_spec])

    #Display all villagers of the same species for villager 2
    st.subheader("Here are all villagers of the "+vill_two_spec+" species:")
    st.dataframe(second_feature[df["Species"]==vill_two_spec])
