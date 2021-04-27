import streamlit as st 
import pandas as pd

st.write("""
# Animal Crossing Roledex 
 Welcome!
""")

df = pd.read_csv("villagers.csv")

#This is the drop down box for the villagers
animal_name = df['Name']
select_villagers = st.selectbox('Choose your animal crossing villager!', options=animal_name, index = 0)

#Display data related to the villager (text)
feature_df = df.drop(['Color 2'], axis = 1)
st.write(feature_df.loc[feature_df['Name'] == select_villagers])
