import streamlit as st 
import pandas as pd
import time
import plotly.express as px
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
    #How to get unique values
    male = feature_df.Gender.value_counts().Male
    st.write(male)

   
    

    
        #------------------------------------------------------------
    #Code to display all of the images of the villagers
    if villager_one== 'Admiral': 
        image = Image.open('admiral.png')
        st.image(image, caption='Admiral', width = 200)
    elif villager_one== 'Agent S':
        image = Image.open('agents.png')
        st.image(image, caption='Agent S', width = 200)
    elif villager_one== 'Agnes':
        image = Image.open('agnes.jpg')
        st.image(image, caption='Agnes', width = 200)
    elif villager_one== 'Al':
        image = Image.open('al.png')
        st.image(image, caption='Al', width = 200)
    elif villager_one== 'Alfonso':
        image = Image.open('alfonso.png')
        st.image(image, caption='Alfonso', width = 200)
    elif villager_one== 'Alice':
        image = Image.open('alice.png')
        st.image(image, caption='Alice', width = 200)
    elif villager_one== 'Alli':
        image = Image.open('alli.png')
        st.image(image, caption='Alli', width = 200)
    elif villager_one== 'Amelia':
        image = Image.open('amelia.png')
        st.image(image, caption='Amelia', width = 200)
    elif villager_one== 'Anabelle':
        image = Image.open('anabelle.jpg')
        st.image(image, caption='Anabelle', width = 200)
    elif villager_one== 'Anchovy':
        image = Image.open('anchovy.jpg')
        st.image(image, caption='Anchovy', width = 200)
    elif villager_one== 'Angus':
        image = Image.open('angus.jpg')
        st.image(image, caption='Angus', width = 200)
    elif villager_one== 'Anicotti':
        image = Image.open('anicotti.png')
        st.image(image, caption='Anicotti', width = 200)
    elif villager_one== 'Ankha':
        image = Image.open('ankha.jpg')
        st.image(image, caption='Ankha', width = 200)
    elif villager_one== 'Annalisa':
        image = Image.open('annalisa.png')
        st.image(image, caption='Annalisa', width = 200)
    elif villager_one== 'Annalise':
        image = Image.open('annalise.jpg')
        st.image(image, caption='Annalise', width = 200)
    elif villager_one== 'Antonio':
        image = Image.open('antonio.png')
        st.image(image, caption='Antonio', width = 200)
    elif villager_one== 'Apollo':
        image = Image.open('apollo.jpg')
        st.image(image, caption='Apollo', width = 200)
    elif villager_one== 'Apple':
        image = Image.open('apple.jpg')
        st.image(image, caption='Apple', width = 200)
    elif villager_one== 'Astrid':
        image = Image.open('astrid.jpg')
        st.image(image, caption='Astrid', width = 200)
    elif villager_one== 'Audie':
        image = Image.open('audie.png')
        st.image(image, caption='Audie', width = 200)
    elif villager_one== 'Aurora':
        image = Image.open('aurora.png')
        st.image(image, caption='Aurora', width = 200)
    elif villager_one== 'Ava':
        image = Image.open('ava.jpg')
        st.image(image, caption='Ava', width = 200)
    elif villager_one== 'Avery':
        image = Image.open('avery.png')
        st.image(image, caption='Avery', width = 200)
    elif villager_one== 'Axel':
        image = Image.open('axel.png')
        st.image(image, caption='Axel', width = 200)
    #-----------------------------------------------
    #B's
    elif villager_one== 'Baabara':
        image = Image.open('baabra.jpg')
        st.image(image, caption='Baabra', width = 200)
    elif villager_one== 'Bam':
        image = Image.open('bam.jpg')
        st.image(image, caption='Bam', width = 200)
    elif villager_one== 'Bangle':
        image = Image.open('bangle.png')
        st.image(image, caption='Bangle', width = 200)
    elif villager_one== 'Barold':
        image = Image.open('barold.jpg')
        st.image(image, caption='Barold', width = 200)
    elif villager_one== 'Bea':
        image = Image.open('bea.png')
        st.image(image, caption='Bea', width = 200)
    elif villager_one== 'Beardo':
        image = Image.open('beardo.png')
        st.image(image, caption='Beardo', width = 200)
    elif villager_one== 'Beau':
        image = Image.open('beau.png')
        st.image(image, caption='Beau', width = 200)
    elif villager_one== 'Becky':
        image = Image.open('becky.jpg')
        st.image(image, caption='Becky', width = 200)
    elif villager_one== 'Bella':
        image = Image.open('bella.png')
        st.image(image, caption='Bella', width = 200)
    elif villager_one== 'Benedict':
        image = Image.open('benedict.png')
        st.image(image, caption='Benedict', width = 200)
    elif villager_one== 'Benjamin':
        image = Image.open('benjamin.png')
        st.image(image, caption='Benjamin', width = 200)
    elif villager_one== 'Bertha':
        image = Image.open('bertha.jpg')
        st.image(image, caption='Bertha', width = 200)
    elif villager_one== 'Bettina':
        image = Image.open('bettina.png')
        st.image(image, caption='Bettina', width = 200)
    elif villager_one== 'Bianca':
        image = Image.open('bianca.jpg')
        st.image(image, caption='Bianca', width = 200)
    elif villager_one== 'Biff':
        image = Image.open('biff.png')
        st.image(image, caption='Biff', width = 200)
    elif villager_one== 'Big Top':
        image = Image.open('bigtop.png')
        st.image(image, caption='Big Top', width = 200)
    elif villager_one== 'Bill':
        image = Image.open('bill.png')
        st.image(image, caption='Bill', width = 200)
    elif villager_one== 'Billy':
        image = Image.open('billy.jpg')
        st.image(image, caption='Billy', width = 200)
    elif villager_one== 'Biskit':
        image = Image.open('biskit.jpg')
        st.image(image, caption='Biskit', width = 200)
    elif villager_one== 'Bitty':
        image = Image.open('bitty.png')
        st.image(image, caption='Bitty', width = 200)
    elif villager_one== 'Blaire':
        image = Image.open('blaire.png')
        st.image(image, caption='Blaire', width = 200)
    elif villager_one== 'Blanche':
        image = Image.open('blanche.jpg')
        st.image(image, caption='Blanche', width = 200)
    elif villager_one== 'Bluebear':
        image = Image.open('bluebear.png')
        st.image(image, caption='Bluebear', width = 200)
    elif villager_one== 'Bob':
        image = Image.open('Bob.jpg')
        st.image(image, caption='Bob', width = 200)
    elif villager_one== 'Bonbon':
        image = Image.open('bonbon.png')
        st.image(image, caption='Bonbon', width = 200)
    elif villager_one== 'Bones':
        image = Image.open('bones.png')
        st.image(image, caption='Bones', width = 200)
    elif villager_one== 'Boomer':
        image = Image.open('boomer.jpg')
        st.image(image, caption='Boomer', width = 200)
    elif villager_one== 'Boone':
        image = Image.open('boone.jpg')
        st.image(image, caption='Boone', width = 200)
    elif villager_one== 'Boots':
        image = Image.open('boots.jpg')
        st.image(image, caption='Boots', width = 200)
    elif villager_one== 'Boris':
        image = Image.open('boris.png')
        st.image(image, caption='Boris', width = 200)
    elif villager_one== 'Boyd':
        image = Image.open('boyd.png')
        st.image(image, caption='Boyd', width = 200)
    elif villager_one== 'Bree':
        image = Image.open('bree.jpg')
        st.image(image, caption='Bree', width = 200)
    elif villager_one== 'Broccolo':
        image = Image.open('broccolo.png')
        st.image(image, caption='Brocollo', width = 200)
    elif villager_one== 'Broffina':
        image = Image.open('broffina.jpg')
        st.image(image, caption='Broffina', width = 200)
    elif villager_one== 'Bruce':
        image = Image.open('bruce.jpg')
        st.image(image, caption='Bruce', width = 200)
    elif villager_one== 'Bubbles':
        image = Image.open('bubbles.jpg')
        st.image(image, caption='Bubbles', width = 200)
    elif villager_one== 'Buck':
        image = Image.open('buck.jpg')
        st.image(image, caption='Buck', width = 200)
    elif villager_one== 'Bud':
        image = Image.open('bud.png')
        st.image(image, caption='Bud', width = 200)
    elif villager_one== 'Bunnie':
        image = Image.open('bunnie.png')
        st.image(image, caption='Bunnie', width = 200)
    elif villager_one== 'Butch':
        image = Image.open('butch.png')
        st.image(image, caption='Butch', width = 200)
    elif villager_one== 'Buzz':
        image = Image.open('buzz.png')
        st.image(image, caption='Buzz', width = 200)
    #-----------------------------------------------
    #C's
    elif villager_one== 'Cally':
        image = Image.open('cally.png')
        st.image(image, caption='Cally', width = 200)
    elif villager_one== 'Camofrog':
        image = Image.open('camofrog.png')
        st.image(image, caption='Camofrog', width = 200)
    elif villager_one== 'Canberra':
        image = Image.open('canberra.png')
        st.image(image, caption='Canberra', width = 200)
    elif villager_one== 'Candi':
        image = Image.open('candi.png')
        st.image(image, caption='Candi', width = 200)
    elif villager_one== 'Carmen':
        image = Image.open('carmen.jpg')
        st.image(image, caption='carmen', width = 200)
    elif villager_one== 'Caroline':
        image = Image.open('caroline.png')
        st.image(image, caption='Caroline', width = 200)
    elif villager_one== 'Carrie':
        image = Image.open('carrie.png')
        st.image(image, caption='Carrie', width = 200)
    elif villager_one== 'Cashmere':
        image = Image.open('cashmere.png')
        st.image(image, caption='Cashmere', width = 200)
    elif villager_one== 'Celia':
        image = Image.open('Celia.jpg')
        st.image(image, caption='Celia', width = 200)
    elif villager_one== 'Cesar':
        image = Image.open('cesar.png')
        st.image(image, caption='Cesar', width = 200)
    elif villager_one== 'Chadder':
        image = Image.open('chadder.jpg')
        st.image(image, caption='Chadder', width = 200)
    elif villager_one== 'Charlise':
        image = Image.open('charlise.png')
        st.image(image, caption='Charlise', width = 200)
    elif villager_one== 'Cheri':
        image = Image.open('cheri.png')
        st.image(image, caption='Cheri', width = 200)
    elif villager_one== 'Cherry':
        image = Image.open('cherry.jpg')
        st.image(image, caption='Cherry', width = 200)
    elif villager_one== 'Chester':
        image = Image.open('chester.jpg')
        st.image(image, caption='Chester', width = 200)
    elif villager_one== 'Chevre':
        image = Image.open('chevre.png')
        st.image(image, caption='Chevre', width = 200)
    elif villager_one== 'Chief':
        image = Image.open('chief.jpg')
        st.image(image, caption='Chief', width = 200)
    elif villager_one== 'Chops':
        image = Image.open('chops.png')
        st.image(image, caption='Chops', width = 200)
    elif villager_one== 'Chow':
        image = Image.open('chow.jpg')
        st.image(image, caption='Chow', width = 200)
    elif villager_one== 'Chrissy':
        image = Image.open('chrissy.jpg')
        st.image(image, caption='Chrissy', width = 200)
    elif villager_one== 'Claude':
        image = Image.open('claude.png')
        st.image(image, caption='Claude', width = 200)
    elif villager_one== 'Claudia':
        image = Image.open('claudia.jpg')
        st.image(image, caption='Claudia', width = 200)
    elif villager_one== 'Clay':
        image = Image.open('clay.png')
        st.image(image, caption='Clay', width = 200)
    elif villager_one== 'Cleo':
        image = Image.open('cleo.png')
        st.image(image, caption='Cleo', width = 200)
    elif villager_one== 'Clyde':
        image = Image.open('clyde.png')
        st.image(image, caption='Clyde', width = 200)
    elif villager_one== 'Coach':
        image = Image.open('coach.jpg')
        st.image(image, caption='Coach', width = 200)
    elif villager_one== 'Cobb':
        image = Image.open('cobb.png')
        st.image(image, caption='Cobb', width = 200)
    elif villager_one== 'Coco':
        image = Image.open('coco.jpg')
        st.image(image, caption='Coco', width = 200)
    elif villager_one== 'Cole':
        image = Image.open('cole.jpg')
        st.image(image, caption='Cole', width = 200)
    elif villager_one== 'Colton':
        image = Image.open('colton.jpg')
        st.image(image, caption='Colton', width = 200)
    elif villager_one== 'Cookie':
        image = Image.open('cookie.png')
        st.image(image, caption='Cookie', width = 200)
    elif villager_one== 'Cousteau':
        image = Image.open('cousteau.jpg')
        st.image(image, caption='Cousteau', width = 200)
    elif villager_one== 'Cranston':
        image = Image.open('cranston.jpg')
        st.image(image, caption='Cranston', width = 200)
    elif villager_one== 'Croque':
        image = Image.open('croque.jpg')
        st.image(image, caption='Croque', width = 200)
    elif villager_one== 'Cube':
        image = Image.open('cube.png')
        st.image(image, caption='Cube', width = 200)
    elif villager_one== 'Curlos':
        image = Image.open('curlose.jpg')
        st.image(image, caption='Curlose', width = 200)
    elif villager_one== 'Curly':
        image = Image.open('curly.jpg')
        st.image(image, caption='Curly', width = 200)
    elif villager_one== 'Curt':
        image = Image.open('curt.png')
        st.image(image, caption='Curt', width = 200)
    elif villager_one== 'Cyd':
        image = Image.open('cyd.jpg')
        st.image(image, caption='Cyd', width = 200)
    elif villager_one== 'Cyrano':
        image = Image.open('cyrano.png')
        st.image(image, caption='Cyrano', width = 200)
    #--------------------------------------------------
    #D's
    elif villager_one== 'Daisy':
        image = Image.open('daisy.jpg')
        st.image(image, caption='Daisy', width = 200)
    elif villager_one== 'Deena':
        image = Image.open('deena.png')
        st.image(image, caption='Deena', width = 200)
    elif villager_one== 'Deirdre':
        image = Image.open('deidre.jpg')
        st.image(image, caption='Deirdre', width = 200)
    elif villager_one== 'Del':
        image = Image.open('del.png')
        st.image(image, caption='Del', width = 200)
    elif villager_one== 'Deli':
        image = Image.open('deli.png')
        st.image(image, caption='Deli', width = 200)
    elif villager_one== 'Derwin':
        image = Image.open('derwin.jpg')
        st.image(image, caption='Derwin', width = 200)
    elif villager_one== 'Diana':
        image = Image.open('diana.jpg')
        st.image(image, caption='Diana', width = 200)
    elif villager_one== 'Diva':
        image = Image.open('diva.jpg')
        st.image(image, caption='Diva', width = 200)
    elif villager_one== 'Dizzy':
        image = Image.open('dizzy.jpg')
        st.image(image, caption='Dizzy', width = 200)
    elif villager_one== 'Dobie':
        image = Image.open('dobie.jpg')
        st.image(image, caption='Dobie', width = 200)
    elif villager_one== 'Doc':
        image = Image.open('Doc.png')
        st.image(image, caption='Doc', width = 200)
    elif villager_one== 'Dom':
        image = Image.open('dom.png')
        st.image(image, caption='Dom', width = 200)
    elif villager_one== 'Dora':
        image = Image.open('dora.jpg')
        st.image(image, caption='Dora', width = 200)
    elif villager_one== 'Dotty':
        image = Image.open('dotty.jpg')
        st.image(image, caption='Dotty', width = 200)
    elif villager_one== 'Drago':
        image = Image.open('drago.jpg')
        st.image(image, caption='Drago', width = 200)
    elif villager_one== 'Drake':
        image = Image.open('drake.png')
        st.image(image, caption='Drake', width = 200)
    elif villager_one== 'Drift':
        image = Image.open('drift.png')
        st.image(image, caption='Drift', width = 200)
    #----------------------------------------------------
    #E's
    elif villager_one== 'Ed':
        image = Image.open('ed.jpg')
        st.image(image, caption='Ed', width = 200)
    elif villager_one== 'Egbert':
        image = Image.open('egbert.png')
        st.image(image, caption='Egbert', width = 200)
    elif villager_one== 'Elise':
        image = Image.open('elise.png')
        st.image(image, caption='Elise', width = 200)
    elif villager_one== 'Ellie':
        image = Image.open('ellie.png')
        st.image(image, caption='Ellie', width = 200)
    elif villager_one== 'Elmer':
        image = Image.open('elmer.jpg')
        st.image(image, caption='Elmer', width = 200)
    elif villager_one== 'Eloise':
        image = Image.open('eloise.png')
        st.image(image, caption='Eloise', width = 200)
    elif villager_one== 'Elvis':
        image = Image.open('elvis.jpg')
        st.image(image, caption='Elvis', width = 200)
    elif villager_one== 'Erik':
        image = Image.open('erik.png')
        st.image(image, caption='Erik', width = 200)
    elif villager_one== 'Eugene':
        image = Image.open('eugene.png')
        st.image(image, caption='Eugene', width = 200)
    elif villager_one== 'Eunice':
        image = Image.open('eunice.png')
        st.image(image, caption='Eunice', width = 200)
    #-----------------------------------------------------
    #F's
    elif villager_one== 'Fang':
        image = Image.open('fang.jpg')
        st.image(image, caption='fang', width = 200)
    elif villager_one== 'Fauna':
        image = Image.open('fauna.png')
        st.image(image, caption='Fauna', width = 200)
    elif villager_one== 'Felicity':
        image = Image.open('felicity.jpg')
        st.image(image, caption='Felicity', width = 200)
    elif villager_one== 'Filbert':
        image = Image.open('filbert.jpg')
        st.image(image, caption='Filbert', width = 200)
    elif villager_one== 'Flip':
        image = Image.open('flip.png')
        st.image(image, caption='Flip', width = 200)
    elif villager_one== 'Flo':
        image = Image.open('flo.png')
        st.image(image, caption='Flo', width = 200)
    elif villager_one== 'Flora':
        image = Image.open('flora.jpg')
        st.image(image, caption='Flora', width = 200)
    elif villager_one== 'Flurry':
        image = Image.open('flurry.png')
        st.image(image, caption='Flurry', width = 200)
    elif villager_one== 'Francine':
        image = Image.open('francine.jpg')
        st.image(image, caption='Francine', width = 200)
    elif villager_one== 'Frank':
        image = Image.open('frank.png')
        st.image(image, caption='Frank', width = 200)
    elif villager_one== 'Freckles':
        image = Image.open('freckles.jpg')
        st.image(image, caption='Freckles', width = 200)
    elif villager_one== 'Freya':
        image = Image.open('freya.png')
        st.image(image, caption='Freya', width = 200)
    elif villager_one== 'Friga':
        image = Image.open('friga.jpg')
        st.image(image, caption='Friga', width = 200)
    elif villager_one== 'Frita':
        image = Image.open('frita.jpg')
        st.image(image, caption='Frita', width = 200)
    elif villager_one== 'Frobert':
        image = Image.open('frobert.png')
        st.image(image, caption='Frobert', width = 200)
    elif villager_one== 'Fuchsia':
        image = Image.open('fuchsia.jpg')
        st.image(image, caption='Fuchsia', width = 200)
    #-------------------------------------------------------
    #G's
    elif villager_one== 'Gabi':
        image = Image.open('gabi.png')
        st.image(image, caption='Gabi', width = 200)
    elif villager_one== 'Gala':
        image = Image.open('gala.jpg')
        st.image(image, caption='Gala', width = 200)
    elif villager_one== 'Gaston':
        image = Image.open('gaston.png')
        st.image(image, caption='Gaston', width = 200)
    elif villager_one== 'Gayle':
        image = Image.open('gayle.jpg')
        st.image(image, caption='Gayle', width = 200)
    elif villager_one== 'Genji':
        image = Image.open('genji.png')
        st.image(image, caption='Genji', width = 200)
    elif villager_one== 'Gigi':
        image = Image.open('gigi.jpg')
        st.image(image, caption='Gigi', width = 200)
    elif villager_one== 'Gladys':
        image = Image.open('gladys.png')
        st.image(image, caption='Gladys', width = 200)
    elif villager_one== 'Gloria':
        image = Image.open('gloria.png')
        st.image(image, caption='Gloria', width = 200)
    elif villager_one== 'Goldie':
        image = Image.open('goldie.png')
        st.image(image, caption='Goldie', width = 200)
    elif villager_one== 'Gonzo':
        image = Image.open('gonzo.png')
        st.image(image, caption='Gonzo', width = 200)
    elif villager_one== 'Goose':
        image = Image.open('goose.png')
        st.image(image, caption='Goose', width = 200)
    elif villager_one== 'Graham':
        image = Image.open('graham.jpg')
        st.image(image, caption='Graham', width = 200)
    elif villager_one== 'Greta':
        image = Image.open('greta.png')
        st.image(image, caption='Greta', width = 200)
    elif villager_one== 'Grizzly':
        image = Image.open('grizzly.png')
        st.image(image, caption='Grizzly', width = 200)
    elif villager_one== 'Groucho':
        image = Image.open('groucho.png')
        st.image(image, caption='Groucho', width = 200)
    elif villager_one== 'Gruff':
        image = Image.open('gruff.png')
        st.image(image, caption='Gruff', width = 200)
    elif villager_one== 'Gwen':
        image = Image.open('gwen.png')
        st.image(image, caption='Gwen', width = 200)
    #--------------------------------------------------------
    #H's
    elif villager_one== 'Hamlet
        image = Image.open('hamlet.png')
        st.image(image, caption='Hamlet', width = 200)
    elif villager_one== 'Hamphry':
        image = Image.open('hamphry.png')
        st.image(image, caption='Hamphry', width = 200)
    elif villager_one== 'Hans':
        image = Image.open('hans.png')
        st.image(image, caption='Hans', width = 200)
    elif villager_one== 'Harry':
        image = Image.open('harry.png')
        st.image(image, caption='Harry', width = 200)
    elif villager_one== 'Hazel':
        image = Image.open('hazel.jpg')
        st.image(image, caption='Hazel', width = 200)
    elif villager_one== 'Henry':
        image = Image.open('henry.png')
        st.image(image, caption='Henry', width = 200)
    elif villager_one== 'Hippeux':
        image = Image.open('hippeux.png')
        st.image(image, caption='Hippeux', width = 200)
    elif villager_one== 'Hopkins':
        image = Image.open('hopkins.jpg')
        st.image(image, caption='Hopkins', width = 200)
    elif villager_one== 'Hopper':
        image = Image.open('hopper.png')
        st.image(image, caption='Hopper', width = 200)
    elif villager_one== 'Hornsby':
        image = Image.open('hornsby.png')
        st.image(image, caption='Hornsby', width = 200)
    elif villager_one== 'Huck':
        image = Image.open('huck.png')
        st.image(image, caption='Huck', width = 200)
    elif villager_one== 'Hugh':
        image = Image.open('hugh.jpg')
        st.image(image, caption='Hugh', width = 200)
    #---------------------------------------------------------
    #I's
    elif villager_one== 'Iggly':
        image = Image.open('iggly.png')
        st.image(image, caption='Iggly', width = 200)
    elif villager_one== 'Ike':
        image = Image.open('ike.png')
        st.image(image, caption='Ike', width = 200)
    #---------------------------------------------------------
    #J's
    elif villager_one== 'Jacob':
        image = Image.open('jacob.jpg')
        st.image(image, caption='Jacob', width = 200)
    elif villager_one== 'Jacques':
        image = Image.open('jacques.jpg')
        st.image(image, caption='Jacques', width = 200)
    elif villager_one== 'Jambette':
        image = Image.open('jambette.png')
        st.image(image, caption='Jambette', width = 200)
    elif villager_one== 'Jay':
        image = Image.open('jay.jpg')
        st.image(image, caption='Jay', width = 200)
    elif villager_one== 'Jeremiah':
        image = Image.open('jeremiah.png')
        st.image(image, caption='Jeremiah', width = 200)
    elif villager_one== 'Jitters':
        image = Image.open('jitters.png')
        st.image(image, caption='Jitters', width = 200)
    elif villager_one== 'Joey':
        image = Image.open('joey.jpg')
        st.image(image, caption='Joey', width = 200)
    elif villager_one== 'Judy':
        image = Image.open('judy.png')
        st.image(image, caption='Judy', width = 200)
    elif villager_one== 'Julia':
        image = Image.open('julia.png')
        st.image(image, caption='Julia', width = 200)
    elif villager_one== 'Julian':
        image = Image.open('julian.png')
        st.image(image, caption='Julian', width = 200)
    elif villager_one== 'June':
        image = Image.open('june.jpg')
        st.image(image, caption='June', width = 200)
    #----------------------------------------------------
    #K's
    elif villager_one== 'Kabuki':
        image = Image.open('kabuki.jpg')
        st.image(image, caption='Kabuki', width = 200)
    elif villager_one== 'Katt':
        image = Image.open('katt.jpg')
        st.image(image, caption='Katt', width = 200)
    elif villager_one== 'keaton':
        image = Image.open('keaton.png')
        st.image(image, caption='Keaton', width = 200)
    elif villager_one== 'Ken':
        image = Image.open('ken.jpg')
        st.image(image, caption='Ken', width = 200)
    elif villager_one== 'Ketchup':
        image = Image.open('ketchup.png')
        st.image(image, caption='ketchup', width = 200)
    elif villager_one== 'Kevin':
        image = Image.open('kevin.png')
        st.image(image, caption='kevin', width = 200)
    elif villager_one== 'Kid Cat':
        image = Image.open('kid cat.png')
        st.image(image, caption='Kid Cat', width = 200)
    elif villager_one== 'Kidd':
        image = Image.open('kidd.jpg')
        st.image(image, caption='Kidd', width = 200)
    elif villager_one== 'Kiki':
        image = Image.open('kiki.png')
        st.image(image, caption='Kiki', width = 200)
    elif villager_one== 'Kitt':
        image = Image.open('kitt.png')
        st.image(image, caption='Kitt', width = 200)
    elif villager_one== 'Kitty':
        image = Image.open('kitty.png')
        st.image(image, caption='Kitty', width = 200)
    elif villager_one== 'Klaus':
        image = Image.open('klaus.png')
        st.image(image, caption='Klaus', width = 200)
    elif villager_one== 'Knox':
        image = Image.open('knox.png')
        st.image(image, caption='Knox', width = 200)
    elif villager_one== 'Kody':
        image = Image.open('kody.png')
        st.image(image, caption='Kody', width = 200)
    elif villager_one== 'Kyle':
        image = Image.open('kyle.jpg')
        st.image(image, caption='Kyle', width = 200)
    #-----------------------------------------------------
    #L's
    elif villager_one== 'Leonardo':
        image = Image.open('leonardo.png')
        st.image(image, caption='Leonardo', width = 200)
    elif villager_one== 'leopold':
        image = Image.open('leopold.png')
        st.image(image, caption='Leopold', width = 200)
    elif villager_one== 'Lily':
        image = Image.open('lily.jpg')
        st.image(image, caption='Lily', width = 200)
    elif villager_one== 'Linberg':
        image = Image.open('linberg.png')
        st.image(image, caption='Linberg', width = 200)
    elif villager_one== 'Lionel':
        image = Image.open('lionel.png')
        st.image(image, caption='Lionel', width = 200)
    elif villager_one== 'Lobo':
        image = Image.open('lobo.jpg')
        st.image(image, caption='Lobo', width = 200)
    elif villager_one== 'Lolly':
        image = Image.open('lolly.png')
        st.image(image, caption='Lolly', width = 200)
    elif villager_one== 'Lopez':
        image = Image.open('lopez.png')
        st.image(image, caption='Lopez', width = 200)
    elif villager_one== 'Louie':
        image = Image.open('louie.png')
        st.image(image, caption='Louie', width = 200)
    elif villager_one== 'Lucha':
        image = Image.open('lucha.png')
        st.image(image, caption='Lucha', width = 200)
    elif villager_one== 'Lucky':
        image = Image.open('lucky.png')
        st.image(image, caption='Lucky', width = 200)
    elif villager_one== 'Lucy':
        image = Image.open('lucy.png')
        st.image(image, caption='Lucy', width = 200)
    elif villager_one== 'Lyman':
        image = Image.open('lyman.jpg')
        st.image(image, caption='Lyman', width = 200)
    #-------------------------------------------------------
    #M's
    elif villager_one== 'Mac':
        image = Image.open('mac.png')
        st.image(image, caption='Mac', width = 200)
    elif villager_one== 'Maddie':
        image = Image.open('maddie.png')
        st.image(image, caption='Maddie', width = 200)
    elif villager_one== 'Maelle':
        image = Image.open('maella.jpg')
        st.image(image, caption='Maelle', width = 200)
    elif villager_one== 'Maggie':
        image = Image.open('maggie.png')
        st.image(image, caption='Maggie', width = 200)
    elif villager_one== 'Mallary':
        image = Image.open('mallary.png')
        st.image(image, caption='Mallary', width = 200)
    elif villager_one== 'Maple':
        image = Image.open('maple.jpg')
        st.image(image, caption='Maple', width = 200)
    elif villager_one== 'Marcel':
        image = Image.open('marcel.png')
        st.image(image, caption='Marcel', width = 200)
    elif villager_one== 'Marcie':
        image = Image.open('marcie.png')
        st.image(image, caption='Marcie', width = 200)
    elif villager_one== 'Margie':
        image = Image.open('margie.png')
        st.image(image, caption='Margie', width = 200)
    elif villager_one== 'Marina':
        image = Image.open('marina.jpg')
        st.image(image, caption='Marina', width = 200)
    elif villager_one== 'Marshal':
        image = Image.open('marshal.png')
        st.image(image, caption='marshal', width = 200)
    elif villager_one== 'Mathilda':
        image = Image.open('mathilda.png')
        st.image(image, caption='Mathilda', width = 200)
    elif villager_one== 'Megan':
        image = Image.open('megan.png')
        st.image(image, caption='Megan', width = 200)
    elif villager_one== 'Melba':
        image = Image.open('melba.jpg')
        st.image(image, caption='Melba', width = 200)
    elif villager_one== 'Merengue':
        image = Image.open('merengue.jpg')
        st.image(image, caption='Merengue', width = 200)
    elif villager_one== 'Merry':
        image = Image.open('merry.jpg')
        st.image(image, caption='Merry', width = 200)
    elif villager_one== 'Midge':
        image = Image.open('midge.png')
        st.image(image, caption='Midge', width = 200)
    elif villager_one== 'Mint':
        image = Image.open('mint.png')
        st.image(image, caption='Mint', width = 200)
    elif villager_one== 'Mira':
        image = Image.open('mira.png')
        st.image(image, caption='Mira', width = 200)
    elif villager_one== 'Miranda':
        image = Image.open('miranda.jpg')
        st.image(image, caption='Miranda', width = 200)
    elif villager_one== 'Mitzi':
        image = Image.open('mitzi.png')
        st.image(image, caption='Mitzi', width = 200)
    elif villager_one== 'Moe':
        image = Image.open('moe.png')
        st.image(image, caption='Moe', width = 200)
    elif villager_one== 'Molly':
        image = Image.open('molly.png')
        st.image(image, caption='Molly', width = 200)
    elif villager_one== 'Monique':
        image = Image.open('monique.jpg')
        st.image(image, caption='Monique', width = 200)
    elif villager_one== 'Monty':
        image = Image.open('monty.png')
        st.image(image, caption='Monty', width = 200)
    elif villager_one== 'Moose':
        image = Image.open('moose.jpg')
        st.image(image, caption='Moose', width = 200)
    elif villager_one== 'Mott':
        image = Image.open('mott.jpg')
        st.image(image, caption='Mott', width = 200)
    elif villager_one== 'Muffy':
        image = Image.open('muffy.png')
        st.image(image, caption='Muffy', width = 200)
    elif villager_one== 'Murphy':
        image = Image.open('murphy.png')
        st.image(image, caption='Murphy', width = 200)
    #-----------------------------------------------------
    #N's
    elif villager_one== 'Nan':
        image = Image.open('nan.png')
        st.image(image, caption='Nan', width = 200)
    elif villager_one== 'Nana':
        image = Image.open('Nana.png')
        st.image(image, caption='Nana', width = 200)
    elif villager_one== 'Naomi':
        image = Image.open('naomi.png')
        st.image(image, caption='Naomi', width = 200)
    elif villager_one== 'Nate':
        image = Image.open('nate.png')
        st.image(image, caption='Nate', width = 200)
    elif villager_one== 'Nibbles':
        image = Image.open('nibbles.png')
        st.image(image, caption='Nibbles', width = 200)
    elif villager_one== 'Norma':
        image = Image.open('norma.png')
        st.image(image, caption='Norma', width = 200)
    #---------------------------------------------------
    #O's
    elif villager_one== 'Octavian':
        image = Image.open('octavian.png')
        st.image(image, caption='Ocvtavian', width = 200)
    elif villager_one== 'Ohare':
        image = Image.open('ohare.jpg')
        st.image(image, caption='Ohare', width = 200)
    elif villager_one== 'Olaf':
        image = Image.open('olaf.png')
        st.image(image, caption='olaf', width = 200)
    elif villager_one== 'Olive':
        image = Image.open('olive.png')
        st.image(image, caption='Olive', width = 200)
    elif villager_one== 'Olivia':
        image = Image.open('olivia.png')
        st.image(image, caption='Olivia', width = 200)
    elif villager_one== 'Opal':
        image = Image.open('opal.png')
        st.image(image, caption='Opal', width = 200)
    elif villager_one== 'Ozzie':
        image = Image.open('ozzie.jpg')
        st.image(image, caption='Ozzie', width = 200)
    #---------------------------------------------------
    #P's
    elif villager_one== 'Pango':
        image = Image.open('pango.jpg')
        st.image(image, caption='Pango', width = 200)
    elif villager_one== 'Paolo':
        image = Image.open('paolo.png')
        st.image(image, caption='Paolo', width = 200)
    elif villager_one== 'Papi':
        image = Image.open('Papi.jpg')
        st.image(image, caption='Papi', width = 200)
    elif villager_one== 'Pashmina':
        image = Image.open('pashmina.jpg')
        st.image(image, caption='Pashmina', width = 200)
    elif villager_one== 'Pate':
        image = Image.open('pate.png')
        st.image(image, caption='Pate', width = 200)
    elif villager_one== 'Patty':
        image = Image.open('patty.png')
        st.image(image, caption='Patty', width = 200)
    elif villager_one== 'Paula':
        image = Image.open('paula.png')
        st.image(image, caption='Paula', width = 200)
    elif villager_one== 'Peaches':
        image = Image.open('peaches.jpg')
        st.image(image, caption='Peaches', width = 200)
    elif villager_one== 'Peanut':
        image = Image.open('peanut.jpg')
        st.image(image, caption='Peanut', width = 200)
    elif villager_one== 'Pecan':
        image = Image.open('pecan.png')
        st.image(image, caption='Pecan', width = 200)
    elif villager_one== 'Peck':
        image = Image.open('peck.png')
        st.image(image, caption='Peck', width = 200)
    elif villager_one== 'Peewee':
        image = Image.open('peewee.png')
        st.image(image, caption='Peewee', width = 200)
    elif villager_one== 'Peggy':
        image = Image.open('peggy.png')
        st.image(image, caption='Peggy', width = 200)
    elif villager_one== 'Pekoe':
        image = Image.open('pekoe.jpg')
        st.image(image, caption='Pekoe', width = 200)
    elif villager_one== 'Pencetti':
        image = Image.open('pencetti.png')
        st.image(image, caption='Pencetti', width = 200)
    elif villager_one== 'Penelope':
        image = Image.open('penelope.png')
        st.image(image, caption='Penelope', width = 200)
    elif villager_one== 'Phil':
        image = Image.open('phil.jpg')
        st.image(image, caption='Phil', width = 200)
    elif villager_one== 'Phoebe':
        image = Image.open('phoebe.png')
        st.image(image, caption='Phoebe', width = 200)
    elif villager_one== 'Pierce':
        image = Image.open('pierce.png')
        st.image(image, caption='Pierce', width = 200)
    elif villager_one== 'Pietro':
        image = Image.open('pietro.jpg')
        st.image(image, caption='Pierto', width = 200)
    elif villager_one== 'Pinky':
        image = Image.open('pinky.jpg')
        st.image(image, caption='Pinky', width = 200)
    elif villager_one== 'Piper':
        image = Image.open('piper.png')
        st.image(image, caption='Piper', width = 200)
    elif villager_one== 'Pippy':
        image = Image.open('pippy.jpg')
        st.image(image, caption='Pippy', width = 200)
    elif villager_one== 'Plucky':
        image = Image.open('plucky.png')
        st.image(image, caption='Plucky', width = 200)
    elif villager_one== 'Pompom':
        image = Image.open('pompom.png')
        st.image(image, caption='Pompom', width = 200)
    elif villager_one== 'Poncho':
        image = Image.open('poncho.jpg')
        st.image(image, caption='Poncho', width = 200)
    elif villager_one== 'Poppy':
        image = Image.open('poppy.jpg')
        st.image(image, caption='Poppy', width = 200)
    elif villager_one== 'Portia':
        image = Image.open('portia.png')
        st.image(image, caption='Portia', width = 200)
    elif villager_one== 'Prince':
        image = Image.open('prince.png')
        st.image(image, caption='Prince', width = 200)
    elif villager_one== 'Puck':
        image = Image.open('puck.png')
        st.image(image, caption='Puck', width = 200)
    elif villager_one== 'Puddles':
        image = Image.open('puddles.png')
        st.image(image, caption='Puddles', width = 200)
    elif villager_one== 'Pudge':
        image = Image.open('pudge.jpg')
        st.image(image, caption='Pudge', width = 200)
    elif villager_one== 'Punchy':
        image = Image.open('punchy.png')
        st.image(image, caption='Punchy', width = 200)
    elif villager_one== 'Purrl':
        image = Image.open('purrl.jpg')
        st.image(image, caption='Purrl', width = 200)
    #-----------------------------------------
    #Q's
    elif villager_one== 'Queenie':
        image = Image.open('queenie.png')
        st.image(image, caption='Queenie', width = 200)
    elif villager_one== 'Quillson':
        image = Image.open('quillson.png')
        st.image(image, caption='Quillson', width = 200)
    #-------------------------------------------
    #R's
    elif villager_one== 'Raddle':
        image = Image.open('raddle.png')
        st.image(image, caption='Raddle', width = 200)
    elif villager_one== 'Rasher':
        image = Image.open('rasher.png')
        st.image(image, caption='Rasher', width = 200)
    elif villager_one== 'Raymond':
        image = Image.open('raymond.jpg')
        st.image(image, caption='Raymond', width = 200)
    elif villager_one== 'Renee':
        image = Image.open('renee.png')
        st.image(image, caption='Renee', width = 200)
    elif villager_one== 'Reneigh':
        image = Image.open('reneigh.png')
        st.image(image, caption='Reneigh', width = 200)
    elif villager_one== 'Rex':
        image = Image.open('rex.png')
        st.image(image, caption='Rex', width = 200)
    elif villager_one== 'Rhonda':
        image = Image.open('rhonda.jpg')
        st.image(image, caption='Rhonda', width = 200)
    elif villager_one== 'Ribbot':
        image = Image.open('ribbot.jpg')
        st.image(image, caption='Ribbot', width = 200)
    elif villager_one== 'Ricky':
        image = Image.open('Ricky.jpg')
        st.image(image, caption='Ricky', width = 200)
    elif villager_one== 'Rizzo':
        image = Image.open('rizzo.png')
        st.image(image, caption='Rizzo', width = 200)
    elif villager_one== 'Roald':
        image = Image.open('roald.jpg')
        st.image(image, caption='Roald', width = 200)
    elif villager_one== 'Robin':
        image = Image.open('robin.jpg')
        st.image(image, caption='Robin', width = 200)
    elif villager_one== 'Rocco':
        image = Image.open('rocco.jpg')
        st.image(image, caption='Rocco', width = 200)
    elif villager_one== 'Rocket':
        image = Image.open('rocket.png')
        st.image(image, caption='Rocket', width = 200)
    elif villager_one== 'Rod':
        image = Image.open('Rod.png')
        st.image(image, caption='Rod', width = 200)
    elif villager_one== 'Rodeo':
        image = Image.open('rodeo.png')
        st.image(image, caption='rodeo', width = 200)
    elif villager_one== 'Rodney':
        image = Image.open('rodney.png')
        st.image(image, caption='Rodney', width = 200) 
    elif villager_one== 'Rolf':
        image = Image.open('rolf.jpg')
        st.image(image, caption='Rolf', width = 200)
    elif villager_one== 'Rooney':
        image = Image.open('rooney.png')
        st.image(image, caption='Rooney', width = 200)
    elif villager_one== 'Rory':
        image = Image.open('rory.jpg')
        st.image(image, caption='Rory', width = 200)
    elif villager_one== 'Roscoe':
        image = Image.open('roscoe.png')
        st.image(image, caption='Roscoe', width = 200)
    elif villager_one== 'Rosie':
        image = Image.open('Rosie.png')
        st.image(image, caption='Rosie', width = 200)
    elif villager_one== 'Rowan':
        image = Image.open('rowan.jpg')
        st.image(image, caption='Rowan', width = 200)
    elif villager_one== 'Ruby':
        image = Image.open('ruby.png')
        st.image(image, caption='Ruby', width = 200)
    elif villager_one== 'Rudy':
        image = Image.open('rudy.png')
        st.image(image, caption='Rudy', width = 200)
    #----------------------------------------------------
    #S's
    elif villager_one== 'Sally':
        image = Image.open('sally.png')
        st.image(image, caption='Sally', width = 200)
    elif villager_one== 'Samson':
        image = Image.open('samson.png')
        st.image(image, caption='Samson', width = 200)
    elif villager_one== 'Sandy':
        image = Image.open('sandy.png')
        st.image(image, caption='Sandy', width = 200)
    elif villager_one== 'Savannah':
        image = Image.open('Savannah.png')
        st.image(image, caption='Savannah', width = 200)
    elif villager_one== 'Scoot':
        image = Image.open('scoot.png')
        st.image(image, caption='Scoot', width = 200)
    elif villager_one== 'Shari':
        image = Image.open('shari.png')
        st.image(image, caption='Shari', width = 200)
    elif villager_one== 'Sheldon':
        image = Image.open('sheldon.png')
        st.image(image, caption='Sheldon', width = 200)
    elif villager_one== 'Shep':
        image = Image.open('shep.jpg')
        st.image(image, caption='Shep', width = 200)
    elif villager_one== 'Sherb':
        image = Image.open('sherb.png')
        st.image(image, caption='Sherb', width = 200)
    elif villager_one== 'Simon':
        image = Image.open('simon.jpg')
        st.image(image, caption='Simon', width = 200)
    elif villager_one== 'Skye':
        image = Image.open('skye.png')
        st.image(image, caption='Skye', width = 200)
    elif villager_one== 'Sly':
        image = Image.open('sly.png')
        st.image(image, caption='Sly', width = 200)
    elif villager_one== 'Snake':
        image = Image.open('snake.png')
        st.image(image, caption='snake', width = 200)
    elif villager_one== 'Snooty':
        image = Image.open('snooty.png')
        st.image(image, caption='Snooty', width = 200)
    elif villager_one== 'Soleil':
        image = Image.open('Soleil.png')
        st.image(image, caption='Soleil', width = 200)
    elif villager_one== 'Sparro':
        image = Image.open('Sparro.jpg')
        st.image(image, caption='Sparro', width = 200)
    elif villager_one== 'Spike':
        image = Image.open('spike.png')
        st.image(image, caption='Spike', width = 200)
    elif villager_one== 'Spork':
        image = Image.open('spork.png')
        st.image(image, caption='spork', width = 200)
    elif villager_one== 'Sprinkle':
        image = Image.open('sprinkle.png')
        st.image(image, caption='sprinkle', width = 200)
    elif villager_one== 'Sprocket':
        image = Image.open('sprocket.png')
        st.image(image, caption='sprocket', width = 200)
    elif villager_one== 'Static':
        image = Image.open('static.png')
        st.image(image, caption='Static', width = 200)
    elif villager_one== 'Stella':
        image = Image.open('stella.png')
        st.image(image, caption='stella', width = 200)
    elif villager_one== 'Sterling':
        image = Image.open('sterling.jpg')
        st.image(image, caption='sterling', width = 200)
    elif villager_one== 'Stinky':
        image = Image.open('stinky.png')
        st.image(image, caption='Stinky', width = 200)
    elif villager_one== 'Stitches':
        image = Image.open('stitches.png')
        st.image(image, caption='stitches', width = 200)
    elif villager_one== 'Stu':
        image = Image.open('stu.png')
        st.image(image, caption='Stu', width = 200)
    elif villager_one== 'Sydney':
        image = Image.open('sydney.png')
        st.image(image, caption='Sydney', width = 200)
    elif villager_one== 'Sylvia':
        image = Image.open('sylvia.jpg')
        st.image(image, caption='Sylvia', width = 200)
    #---------------------------------------------------------
    #T's
    elif villager_one== 'Tabby':
        image = Image.open('tabby.png')
        st.image(image, caption='Tabby', width = 200)
    elif villager_one== 'Tad':
        image = Image.open('tad.png')
        st.image(image, caption='Tad', width = 200)
    elif villager_one== 'Tammi':
        image = Image.open('tammi.png')
        st.image(image, caption='Tammi', width = 200)
    elif villager_one== 'Tammy':
        image = Image.open('tammy.jpg')
        st.image(image, caption='Tammy', width = 200)
    elif villager_one== 'Tangy':
        image = Image.open('tangy.jpg')
        st.image(image, caption='Tangy', width = 200)
    elif villager_one== 'Tank':
        image = Image.open('tank.png')
        st.image(image, caption='Tank', width = 200)
    elif villager_one== 'Tasha':
        image = Image.open('tasha.png')
        st.image(image, caption='Tasha', width = 200)
    elif villager_one== 'Tbone':
        image = Image.open('tbone.png')
        st.image(image, caption='Tbone', width = 200)
    elif villager_one== 'Teddy':
        image = Image.open('teddy.jpg')
        st.image(image, caption='Teddy', width = 200)
    elif villager_one== 'Tex':
        image = Image.open('tex.jpg')
        st.image(image, caption='Tex', width = 200)
    elif villager_one== 'Tia':
        image = Image.open('tia.png')
        st.image(image, caption='Tia', width = 200)
    elif villager_one== 'Tiffany':
        image = Image.open('tiffany.png')
        st.image(image, caption='Tiffany', width = 200)
    elif villager_one== 'Timbra':
        image = Image.open('timbra.png')
        st.image(image, caption='Timbra', width = 200)
    elif villager_one== 'Tipper':
        image = Image.open('tipper.png')
        st.image(image, caption='tipper', width = 200)
    elif villager_one== 'Tom':
        image = Image.open('tom.png')
        st.image(image, caption='Tom', width = 200)
    elif villager_one== 'Truffles':
        image = Image.open('truffles.jpg')
        st.image(image, caption='truffles', width = 200)
    elif villager_one== 'Tucker':
        image = Image.open('tucker.png')
        st.image(image, caption='Tucker', width = 200)
    elif villager_one== 'Tutu':
        image = Image.open('tutu.png')
        st.image(image, caption='Tutu', width = 200)
    elif villager_one== 'Twiggy':
        image = Image.open('twiggy/jpg')
        st.image(image, caption='Twiggy', width = 200)
    elif villager_one== 'Tybalt':
        image = Image.open('tybalt.png')
        st.image(image, caption='Tybalt', width = 200)
    #-------------------------------------------------
    #U's
    elif villager_one== 'Ursala':
        image = Image.open('ursala.png')
        st.image(image, caption='Ursala', width = 200)
    #--------------------------------------------------
    #V's
    elif villager_one== 'Velma':
        image = Image.open('velma.png')
        st.image(image, caption='Velma', width = 200)
    elif villager_one== 'Vesta':
        image = Image.open('vesta.jpg')
        st.image(image, caption='Vesta', width = 200)
    elif villager_one== 'Vic':
        image = Image.open('vic.png')
        st.image(image, caption='Vic', width = 200)
    elif villager_one== 'Victoria':
        image = Image.open('victoria.jpg')
        st.image(image, caption='Victoria', width = 200)
    elif villager_one== 'Violet':
        image = Image.open('violet.png')
        st.image(image, caption='Violet', width = 200)
    elif villager_one== 'Vivian':
        image = Image.open('vivian.png')
        st.image(image, caption='Vivian', width = 200)
    elif villager_one== 'Vladmir':
        image = Image.open('vladmir.jpg')
        st.image(image, caption='Vladmir', width = 200)
    #---------------------------------------------------
    #W's
    elif villager_one== 'Wade':
        image = Image.open('wade.png')
        st.image(image, caption='Wade', width = 200)
    elif villager_one== 'Walker':
        image = Image.open('walker.png')
        st.image(image, caption='Walker', width = 200)
    elif villager_one== 'Walt':
        image = Image.open('walt.jpg')
        st.image(image, caption='Walt', width = 200)
    elif villager_one== 'Wartjr':
        image = Image.open('wartjr.png')
        st.image(image, caption='WartJr', width = 200)
    elif villager_one== 'Weber':
        image = Image.open('weber.png')
        st.image(image, caption='Weber', width = 200)
    elif villager_one== 'Wendy':
        image = Image.open('wendy.png')
        st.image(image, caption='Wendy', width = 200)
    elif villager_one== 'Whitney':
        image = Image.open('whitney.jpg')
        st.image(image, caption='Whitney', width = 200)
    elif villager_one== 'Willow':
        image = Image.open('willow.png')
        st.image(image, caption='Willow', width = 200)
    elif villager_one== 'Winnie':
        image = Image.open('winnie.png')
        st.image(image, caption='Winnie', width = 200)
    elif villager_one== 'Wolfgang':
        image = Image.open('wolfgang.jpg')
        st.image(image, caption='Wolfgang', width = 200)
    #------------------------------------------------------
    #Y's
    elif villager_one== 'Yuka':
        image = Image.open('yuka.png')
        st.image(image, caption='Yuka', width = 200)
    #----------------------------------------------------
    #Z's
    elif villager_one== 'Zell':
        image = Image.open('zell.png')
        st.image(image, caption='Zell', width = 200)
    elif villager_one== 'Zucker':
        image = Image.open('zucker.jpg')
        st.image(image, caption='Zucker', width = 200)


        
        #------------------------------------------------------------
    #Code to display all of the images of the villagers
    if villager_two == 'Admiral': 
        image = Image.open('admiral.png')
        st.image(image, caption='Admiral', width = 200)
    elif villager_two == 'Agent S':
        image = Image.open('agents.png')
        st.image(image, caption='Agent S', width = 200)
    elif villager_two == 'Agnes':
        image = Image.open('agnes.jpg')
        st.image(image, caption='Agnes', width = 200)
    elif villager_two == 'Al':
        image = Image.open('al.png')
        st.image(image, caption='Al', width = 200)
    elif villager_two == 'Alfonso':
        image = Image.open('alfonso.png')
        st.image(image, caption='Alfonso', width = 200)
    elif villager_two == 'Alice':
        image = Image.open('alice.png')
        st.image(image, caption='Alice', width = 200)
    elif villager_two == 'Alli':
        image = Image.open('alli.png')
        st.image(image, caption='Alli', width = 200)
    elif villager_two == 'Amelia':
        image = Image.open('amelia.png')
        st.image(image, caption='Amelia', width = 200)
    elif villager_two == 'Anabelle':
        image = Image.open('anabelle.jpg')
        st.image(image, caption='Anabelle', width = 200)
    elif villager_two == 'Anchovy':
        image = Image.open('anchovy.jpg')
        st.image(image, caption='Anchovy', width = 200)
    elif villager_two == 'Angus':
        image = Image.open('angus.jpg')
        st.image(image, caption='Angus', width = 200)
    elif villager_two == 'Anicotti':
        image = Image.open('anicotti.png')
        st.image(image, caption='Anicotti', width = 200)
    elif villager_two == 'Ankha':
        image = Image.open('ankha.jpg')
        st.image(image, caption='Ankha', width = 200)
    elif villager_two == 'Annalisa':
        image = Image.open('annalisa.png')
        st.image(image, caption='Annalisa', width = 200)
    elif villager_two == 'Annalise':
        image = Image.open('annalise.jpg')
        st.image(image, caption='Annalise', width = 200)
    elif villager_two == 'Antonio':
        image = Image.open('antonio.png')
        st.image(image, caption='Antonio', width = 200)
    elif villager_two == 'Apollo':
        image = Image.open('apollo.jpg')
        st.image(image, caption='Apollo', width = 200)
    elif villager_two == 'Apple':
        image = Image.open('apple.jpg')
        st.image(image, caption='Apple', width = 200)
    elif villager_two == 'Astrid':
        image = Image.open('astrid.jpg')
        st.image(image, caption='Astrid', width = 200)
    elif villager_two == 'Audie':
        image = Image.open('audie.png')
        st.image(image, caption='Audie', width = 200)
    elif villager_two == 'Aurora':
        image = Image.open('aurora.png')
        st.image(image, caption='Aurora', width = 200)
    elif villager_two == 'Ava':
        image = Image.open('ava.jpg')
        st.image(image, caption='Ava', width = 200)
    elif villager_two == 'Avery':
        image = Image.open('avery.png')
        st.image(image, caption='Avery', width = 200)
    elif villager_two == 'Axel':
        image = Image.open('axel.png')
        st.image(image, caption='Axel', width = 200)
    #-----------------------------------------------
    #B's
    elif villager_two == 'Baabara':
        image = Image.open('baabra.jpg')
        st.image(image, caption='Baabra', width = 200)
    elif villager_two == 'Bam':
        image = Image.open('bam.jpg')
        st.image(image, caption='Bam', width = 200)
    elif villager_two == 'Bangle':
        image = Image.open('bangle.png')
        st.image(image, caption='Bangle', width = 200)
    elif villager_two == 'Barold':
        image = Image.open('barold.jpg')
        st.image(image, caption='Barold', width = 200)
    elif villager_two == 'Bea':
        image = Image.open('bea.png')
        st.image(image, caption='Bea', width = 200)
    elif villager_two == 'Beardo':
        image = Image.open('beardo.png')
        st.image(image, caption='Beardo', width = 200)
    elif villager_two == 'Beau':
        image = Image.open('beau.png')
        st.image(image, caption='Beau', width = 200)
    elif villager_two == 'Becky':
        image = Image.open('becky.jpg')
        st.image(image, caption='Becky', width = 200)
    elif villager_two == 'Bella':
        image = Image.open('bella.png')
        st.image(image, caption='Bella', width = 200)
    elif villager_two == 'Benedict':
        image = Image.open('benedict.png')
        st.image(image, caption='Benedict', width = 200)
    elif villager_two == 'Benjamin':
        image = Image.open('benjamin.png')
        st.image(image, caption='Benjamin', width = 200)
    elif villager_two == 'Bertha':
        image = Image.open('bertha.jpg')
        st.image(image, caption='Bertha', width = 200)
    elif villager_two == 'Bettina':
        image = Image.open('bettina.png')
        st.image(image, caption='Bettina', width = 200)
    elif villager_two == 'Bianca':
        image = Image.open('bianca.jpg')
        st.image(image, caption='Bianca', width = 200)
    elif villager_two == 'Biff':
        image = Image.open('biff.png')
        st.image(image, caption='Biff', width = 200)
    elif villager_two == 'Big Top':
        image = Image.open('bigtop.png')
        st.image(image, caption='Big Top', width = 200)
    elif villager_two == 'Bill':
        image = Image.open('bill.png')
        st.image(image, caption='Bill', width = 200)
    elif villager_two == 'Billy':
        image = Image.open('billy.jpg')
        st.image(image, caption='Billy', width = 200)
    elif villager_two == 'Biskit':
        image = Image.open('biskit.jpg')
        st.image(image, caption='Biskit', width = 200)
    elif villager_two == 'Bitty':
        image = Image.open('bitty.png')
        st.image(image, caption='Bitty', width = 200)
    elif villager_two == 'Blaire':
        image = Image.open('blaire.png')
        st.image(image, caption='Blaire', width = 200)
    elif villager_two == 'Blanche':
        image = Image.open('blanche.jpg')
        st.image(image, caption='Blanche', width = 200)
    elif villager_two == 'Bluebear':
        image = Image.open('bluebear.png')
        st.image(image, caption='Bluebear', width = 200)
    elif villager_two == 'Bob':
        image = Image.open('Bob.jpg')
        st.image(image, caption='Bob', width = 200)
    elif villager_two == 'Bonbon':
        image = Image.open('bonbon.png')
        st.image(image, caption='Bonbon', width = 200)
    elif villager_two == 'Bones':
        image = Image.open('bones.png')
        st.image(image, caption='Bones', width = 200)
    elif villager_two == 'Boomer':
        image = Image.open('boomer.jpg')
        st.image(image, caption='Boomer', width = 200)
    elif villager_two == 'Boone':
        image = Image.open('boone.jpg')
        st.image(image, caption='Boone', width = 200)
    elif villager_two == 'Boots':
        image = Image.open('boots.jpg')
        st.image(image, caption='Boots', width = 200)
    elif villager_two == 'Boris':
        image = Image.open('boris.png')
        st.image(image, caption='Boris', width = 200)
    elif villager_two == 'Boyd':
        image = Image.open('boyd.png')
        st.image(image, caption='Boyd', width = 200)
    elif villager_two == 'Bree':
        image = Image.open('bree.jpg')
        st.image(image, caption='Bree', width = 200)
    elif villager_two == 'Broccolo':
        image = Image.open('broccolo.png')
        st.image(image, caption='Brocollo', width = 200)
    elif villager_two == 'Broffina':
        image = Image.open('broffina.jpg')
        st.image(image, caption='Broffina', width = 200)
    elif villager_two == 'Bruce':
        image = Image.open('bruce.jpg')
        st.image(image, caption='Bruce', width = 200)
    elif villager_two == 'Bubbles':
        image = Image.open('bubbles.jpg')
        st.image(image, caption='Bubbles', width = 200)
    elif villager_two == 'Buck':
        image = Image.open('buck.jpg')
        st.image(image, caption='Buck', width = 200)
    elif villager_two == 'Bud':
        image = Image.open('bud.png')
        st.image(image, caption='Bud', width = 200)
    elif villager_two == 'Bunnie':
        image = Image.open('bunnie.png')
        st.image(image, caption='Bunnie', width = 200)
    elif villager_two == 'Butch':
        image = Image.open('butch.png')
        st.image(image, caption='Butch', width = 200)
    elif villager_two == 'Buzz':
        image = Image.open('buzz.png')
        st.image(image, caption='Buzz', width = 200)
    #-----------------------------------------------
    #C's
    elif villager_two == 'Cally':
        image = Image.open('cally.png')
        st.image(image, caption='Cally', width = 200)
    elif villager_two == 'Camofrog':
        image = Image.open('camofrog.png')
        st.image(image, caption='Camofrog', width = 200)
    elif villager_two == 'Canberra':
        image = Image.open('canberra.png')
        st.image(image, caption='Canberra', width = 200)
    elif villager_two == 'Candi':
        image = Image.open('candi.png')
        st.image(image, caption='Candi', width = 200)
    elif villager_two == 'Carmen':
        image = Image.open('carmen.jpg')
        st.image(image, caption='carmen', width = 200)
    elif villager_two == 'Caroline':
        image = Image.open('caroline.png')
        st.image(image, caption='Caroline', width = 200)
    elif villager_two == 'Carrie':
        image = Image.open('carrie.png')
        st.image(image, caption='Carrie', width = 200)
    elif villager_two == 'Cashmere':
        image = Image.open('cashmere.png')
        st.image(image, caption='Cashmere', width = 200)
    elif villager_two == 'Celia':
        image = Image.open('Celia.jpg')
        st.image(image, caption='Celia', width = 200)
    elif villager_two == 'Cesar':
        image = Image.open('cesar.png')
        st.image(image, caption='Cesar', width = 200)
    elif villager_two == 'Chadder':
        image = Image.open('chadder.jpg')
        st.image(image, caption='Chadder', width = 200)
    elif villager_two == 'Charlise':
        image = Image.open('charlise.png')
        st.image(image, caption='Charlise', width = 200)
    elif villager_two == 'Cheri':
        image = Image.open('cheri.png')
        st.image(image, caption='Cheri', width = 200)
    elif villager_two == 'Cherry':
        image = Image.open('cherry.jpg')
        st.image(image, caption='Cherry', width = 200)
    elif villager_two == 'Chester':
        image = Image.open('chester.jpg')
        st.image(image, caption='Chester', width = 200)
    elif villager_two == 'Chevre':
        image = Image.open('chevre.png')
        st.image(image, caption='Chevre', width = 200)
    elif villager_two == 'Chief':
        image = Image.open('chief.jpg')
        st.image(image, caption='Chief', width = 200)
    elif villager_two == 'Chops':
        image = Image.open('chops.png')
        st.image(image, caption='Chops', width = 200)
    elif villager_two == 'Chow':
        image = Image.open('chow.jpg')
        st.image(image, caption='Chow', width = 200)
    elif villager_two == 'Chrissy':
        image = Image.open('chrissy.jpg')
        st.image(image, caption='Chrissy', width = 200)
    elif villager_two == 'Claude':
        image = Image.open('claude.png')
        st.image(image, caption='Claude', width = 200)
    elif villager_two == 'Claudia':
        image = Image.open('claudia.jpg')
        st.image(image, caption='Claudia', width = 200)
    elif villager_two == 'Clay':
        image = Image.open('clay.png')
        st.image(image, caption='Clay', width = 200)
    elif villager_two == 'Cleo':
        image = Image.open('cleo.png')
        st.image(image, caption='Cleo', width = 200)
    elif villager_two == 'Clyde':
        image = Image.open('clyde.png')
        st.image(image, caption='Clyde', width = 200)
    elif villager_two == 'Coach':
        image = Image.open('coach.jpg')
        st.image(image, caption='Coach', width = 200)
    elif villager_two == 'Cobb':
        image = Image.open('cobb.png')
        st.image(image, caption='Cobb', width = 200)
    elif villager_two == 'Coco':
        image = Image.open('coco.jpg')
        st.image(image, caption='Coco', width = 200)
    elif villager_two == 'Cole':
        image = Image.open('cole.jpg')
        st.image(image, caption='Cole', width = 200)
    elif villager_two == 'Colton':
        image = Image.open('colton.jpg')
        st.image(image, caption='Colton', width = 200)
    elif villager_two == 'Cookie':
        image = Image.open('cookie.png')
        st.image(image, caption='Cookie', width = 200)
    elif villager_two == 'Cousteau':
        image = Image.open('cousteau.jpg')
        st.image(image, caption='Cousteau', width = 200)
    elif villager_two == 'Cranston':
        image = Image.open('cranston.jpg')
        st.image(image, caption='Cranston', width = 200)
    elif villager_two == 'Croque':
        image = Image.open('croque.jpg')
        st.image(image, caption='Croque', width = 200)
    elif villager_two == 'Cube':
        image = Image.open('cube.png')
        st.image(image, caption='Cube', width = 200)
    elif villager_two == 'Curlos':
        image = Image.open('curlose.jpg')
        st.image(image, caption='Curlose', width = 200)
    elif villager_two == 'Curly':
        image = Image.open('curly.jpg')
        st.image(image, caption='Curly', width = 200)
    elif villager_two == 'Curt':
        image = Image.open('curt.png')
        st.image(image, caption='Curt', width = 200)
    elif villager_two == 'Cyd':
        image = Image.open('cyd.jpg')
        st.image(image, caption='Cyd', width = 200)
    elif villager_two == 'Cyrano':
        image = Image.open('cyrano.png')
        st.image(image, caption='Cyrano', width = 200)
    #--------------------------------------------------
    #D's
    elif villager_two == 'Daisy':
        image = Image.open('daisy.jpg')
        st.image(image, caption='Daisy', width = 200)
    elif villager_two == 'Deena':
        image = Image.open('deena.png')
        st.image(image, caption='Deena', width = 200)
    elif villager_two == 'Deirdre':
        image = Image.open('deidre.jpg')
        st.image(image, caption='Deirdre', width = 200)
    elif villager_two == 'Del':
        image = Image.open('del.png')
        st.image(image, caption='Del', width = 200)
    elif villager_two == 'Deli':
        image = Image.open('deli.png')
        st.image(image, caption='Deli', width = 200)
    elif villager_two == 'Derwin':
        image = Image.open('derwin.jpg')
        st.image(image, caption='Derwin', width = 200)
    elif villager_two == 'Diana':
        image = Image.open('diana.jpg')
        st.image(image, caption='Diana', width = 200)
    elif villager_two == 'Diva':
        image = Image.open('diva.jpg')
        st.image(image, caption='Diva', width = 200)
    elif villager_two == 'Dizzy':
        image = Image.open('dizzy.jpg')
        st.image(image, caption='Dizzy', width = 200)
    elif villager_two == 'Dobie':
        image = Image.open('dobie.jpg')
        st.image(image, caption='Dobie', width = 200)
    elif villager_two == 'Doc':
        image = Image.open('Doc.png')
        st.image(image, caption='Doc', width = 200)
    elif villager_two == 'Dom':
        image = Image.open('dom.png')
        st.image(image, caption='Dom', width = 200)
    elif villager_two == 'Dora':
        image = Image.open('dora.jpg')
        st.image(image, caption='Dora', width = 200)
    elif villager_two == 'Dotty':
        image = Image.open('dotty.jpg')
        st.image(image, caption='Dotty', width = 200)
    elif villager_two == 'Drago':
        image = Image.open('drago.jpg')
        st.image(image, caption='Drago', width = 200)
    elif villager_two == 'Drake':
        image = Image.open('drake.png')
        st.image(image, caption='Drake', width = 200)
    elif villager_two == 'Drift':
        image = Image.open('drift.png')
        st.image(image, caption='Drift', width = 200)
    #----------------------------------------------------
    #E's
    elif villager_two == 'Ed':
        image = Image.open('ed.jpg')
        st.image(image, caption='Ed', width = 200)
    elif villager_two == 'Egbert':
        image = Image.open('egbert.png')
        st.image(image, caption='Egbert', width = 200)
    elif villager_two == 'Elise':
        image = Image.open('elise.png')
        st.image(image, caption='Elise', width = 200)
    elif villager_two == 'Ellie':
        image = Image.open('ellie.png')
        st.image(image, caption='Ellie', width = 200)
    elif villager_two == 'Elmer':
        image = Image.open('elmer.jpg')
        st.image(image, caption='Elmer', width = 200)
    elif villager_two == 'Eloise':
        image = Image.open('eloise.png')
        st.image(image, caption='Eloise', width = 200)
    elif villager_two == 'Elvis':
        image = Image.open('elvis.jpg')
        st.image(image, caption='Elvis', width = 200)
    elif villager_two == 'Erik':
        image = Image.open('erik.png')
        st.image(image, caption='Erik', width = 200)
    elif villager_two == 'Eugene':
        image = Image.open('eugene.png')
        st.image(image, caption='Eugene', width = 200)
    elif villager_two == 'Eunice':
        image = Image.open('eunice.png')
        st.image(image, caption='Eunice', width = 200)
    #-----------------------------------------------------
    #F's
    elif villager_two == 'Fang':
        image = Image.open('fang.jpg')
        st.image(image, caption='fang', width = 200)
    elif villager_two == 'Fauna':
        image = Image.open('fauna.png')
        st.image(image, caption='Fauna', width = 200)
    elif villager_two == 'Felicity':
        image = Image.open('felicity.jpg')
        st.image(image, caption='Felicity', width = 200)
    elif villager_two == 'Filbert':
        image = Image.open('filbert.jpg')
        st.image(image, caption='Filbert', width = 200)
    elif villager_two == 'Flip':
        image = Image.open('flip.png')
        st.image(image, caption='Flip', width = 200)
    elif villager_two == 'Flo':
        image = Image.open('flo.png')
        st.image(image, caption='Flo', width = 200)
    elif villager_two == 'Flora':
        image = Image.open('flora.jpg')
        st.image(image, caption='Flora', width = 200)
    elif villager_two == 'Flurry':
        image = Image.open('flurry.png')
        st.image(image, caption='Flurry', width = 200)
    elif villager_two == 'Francine':
        image = Image.open('francine.jpg')
        st.image(image, caption='Francine', width = 200)
    elif villager_two == 'Frank':
        image = Image.open('frank.png')
        st.image(image, caption='Frank', width = 200)
    elif villager_two == 'Freckles':
        image = Image.open('freckles.jpg')
        st.image(image, caption='Freckles', width = 200)
    elif villager_two == 'Freya':
        image = Image.open('freya.png')
        st.image(image, caption='Freya', width = 200)
    elif villager_two == 'Friga':
        image = Image.open('friga.jpg')
        st.image(image, caption='Friga', width = 200)
    elif villager_two == 'Frita':
        image = Image.open('frita.jpg')
        st.image(image, caption='Frita', width = 200)
    elif villager_two == 'Frobert':
        image = Image.open('frobert.png')
        st.image(image, caption='Frobert', width = 200)
    elif villager_two == 'Fuchsia':
        image = Image.open('fuchsia.jpg')
        st.image(image, caption='Fuchsia', width = 200)
    #-------------------------------------------------------
    #G's
    elif villager_two == 'Gabi':
        image = Image.open('gabi.png')
        st.image(image, caption='Gabi', width = 200)
    elif villager_two == 'Gala':
        image = Image.open('gala.jpg')
        st.image(image, caption='Gala', width = 200)
    elif villager_two == 'Gaston':
        image = Image.open('gaston.png')
        st.image(image, caption='Gaston', width = 200)
    elif villager_two == 'Gayle':
        image = Image.open('gayle.jpg')
        st.image(image, caption='Gayle', width = 200)
    elif villager_two == 'Genji':
        image = Image.open('genji.png')
        st.image(image, caption='Genji', width = 200)
    elif villager_two == 'Gigi':
        image = Image.open('gigi.jpg')
        st.image(image, caption='Gigi', width = 200)
    elif villager_two == 'Gladys':
        image = Image.open('gladys.png')
        st.image(image, caption='Gladys', width = 200)
    elif villager_two == 'Gloria':
        image = Image.open('gloria.png')
        st.image(image, caption='Gloria', width = 200)
    elif villager_two == 'Goldie':
        image = Image.open('goldie.png')
        st.image(image, caption='Goldie', width = 200)
    elif villager_two == 'Gonzo':
        image = Image.open('gonzo.png')
        st.image(image, caption='Gonzo', width = 200)
    elif villager_two == 'Goose':
        image = Image.open('goose.png')
        st.image(image, caption='Goose', width = 200)
    elif villager_two == 'Graham':
        image = Image.open('graham.jpg')
        st.image(image, caption='Graham', width = 200)
    elif villager_two == 'Greta':
        image = Image.open('greta.png')
        st.image(image, caption='Greta', width = 200)
    elif villager_two == 'Grizzly':
        image = Image.open('grizzly.png')
        st.image(image, caption='Grizzly', width = 200)
    elif villager_two == 'Groucho':
        image = Image.open('groucho.png')
        st.image(image, caption='Groucho', width = 200)
    elif villager_two == 'Gruff':
        image = Image.open('gruff.png')
        st.image(image, caption='Gruff', width = 200)
    elif villager_two == 'Gwen':
        image = Image.open('gwen.png')
        st.image(image, caption='Gwen', width = 200)
    #--------------------------------------------------------
    #H's
    elif villager_two == 'Hamlet
        image = Image.open('hamlet.png')
        st.image(image, caption='Hamlet', width = 200)
    elif villager_two == 'Hamphry':
        image = Image.open('hamphry.png')
        st.image(image, caption='Hamphry', width = 200)
    elif villager_two == 'Hans':
        image = Image.open('hans.png')
        st.image(image, caption='Hans', width = 200)
    elif villager_two == 'Harry':
        image = Image.open('harry.png')
        st.image(image, caption='Harry', width = 200)
    elif villager_two == 'Hazel':
        image = Image.open('hazel.jpg')
        st.image(image, caption='Hazel', width = 200)
    elif villager_two == 'Henry':
        image = Image.open('henry.png')
        st.image(image, caption='Henry', width = 200)
    elif villager_two == 'Hippeux':
        image = Image.open('hippeux.png')
        st.image(image, caption='Hippeux', width = 200)
    elif villager_two == 'Hopkins':
        image = Image.open('hopkins.jpg')
        st.image(image, caption='Hopkins', width = 200)
    elif villager_two == 'Hopper':
        image = Image.open('hopper.png')
        st.image(image, caption='Hopper', width = 200)
    elif villager_two == 'Hornsby':
        image = Image.open('hornsby.png')
        st.image(image, caption='Hornsby', width = 200)
    elif villager_two == 'Huck':
        image = Image.open('huck.png')
        st.image(image, caption='Huck', width = 200)
    elif villager_two == 'Hugh':
        image = Image.open('hugh.jpg')
        st.image(image, caption='Hugh', width = 200)
    #---------------------------------------------------------
    #I's
    elif villager_two == 'Iggly':
        image = Image.open('iggly.png')
        st.image(image, caption='Iggly', width = 200)
    elif villager_two == 'Ike':
        image = Image.open('ike.png')
        st.image(image, caption='Ike', width = 200)
    #---------------------------------------------------------
    #J's
    elif villager_two == 'Jacob':
        image = Image.open('jacob.jpg')
        st.image(image, caption='Jacob', width = 200)
    elif villager_two == 'Jacques':
        image = Image.open('jacques.jpg')
        st.image(image, caption='Jacques', width = 200)
    elif villager_two == 'Jambette':
        image = Image.open('jambette.png')
        st.image(image, caption='Jambette', width = 200)
    elif villager_two == 'Jay':
        image = Image.open('jay.jpg')
        st.image(image, caption='Jay', width = 200)
    elif villager_two == 'Jeremiah':
        image = Image.open('jeremiah.png')
        st.image(image, caption='Jeremiah', width = 200)
    elif villager_two == 'Jitters':
        image = Image.open('jitters.png')
        st.image(image, caption='Jitters', width = 200)
    elif villager_two == 'Joey':
        image = Image.open('joey.jpg')
        st.image(image, caption='Joey', width = 200)
    elif villager_two == 'Judy':
        image = Image.open('judy.png')
        st.image(image, caption='Judy', width = 200)
    elif villager_two == 'Julia':
        image = Image.open('julia.png')
        st.image(image, caption='Julia', width = 200)
    elif villager_two == 'Julian':
        image = Image.open('julian.png')
        st.image(image, caption='Julian', width = 200)
    elif villager_two == 'June':
        image = Image.open('june.jpg')
        st.image(image, caption='June', width = 200)
    #----------------------------------------------------
    #K's
    elif villager_two == 'Kabuki':
        image = Image.open('kabuki.jpg')
        st.image(image, caption='Kabuki', width = 200)
    elif villager_two == 'Katt':
        image = Image.open('katt.jpg')
        st.image(image, caption='Katt', width = 200)
    elif villager_two == 'keaton':
        image = Image.open('keaton.png')
        st.image(image, caption='Keaton', width = 200)
    elif villager_two == 'Ken':
        image = Image.open('ken.jpg')
        st.image(image, caption='Ken', width = 200)
    elif villager_two == 'Ketchup':
        image = Image.open('ketchup.png')
        st.image(image, caption='ketchup', width = 200)
    elif villager_two == 'Kevin':
        image = Image.open('kevin.png')
        st.image(image, caption='kevin', width = 200)
    elif villager_two == 'Kid Cat':
        image = Image.open('kid cat.png')
        st.image(image, caption='Kid Cat', width = 200)
    elif villager_two == 'Kidd':
        image = Image.open('kidd.jpg')
        st.image(image, caption='Kidd', width = 200)
    elif villager_two == 'Kiki':
        image = Image.open('kiki.png')
        st.image(image, caption='Kiki', width = 200)
    elif villager_two == 'Kitt':
        image = Image.open('kitt.png')
        st.image(image, caption='Kitt', width = 200)
    elif villager_two == 'Kitty':
        image = Image.open('kitty.png')
        st.image(image, caption='Kitty', width = 200)
    elif villager_two == 'Klaus':
        image = Image.open('klaus.png')
        st.image(image, caption='Klaus', width = 200)
    elif villager_two == 'Knox':
        image = Image.open('knox.png')
        st.image(image, caption='Knox', width = 200)
    elif villager_two == 'Kody':
        image = Image.open('kody.png')
        st.image(image, caption='Kody', width = 200)
    elif villager_two == 'Kyle':
        image = Image.open('kyle.jpg')
        st.image(image, caption='Kyle', width = 200)
    #-----------------------------------------------------
    #L's
    elif villager_two == 'Leonardo':
        image = Image.open('leonardo.png')
        st.image(image, caption='Leonardo', width = 200)
    elif villager_two == 'leopold':
        image = Image.open('leopold.png')
        st.image(image, caption='Leopold', width = 200)
    elif villager_two == 'Lily':
        image = Image.open('lily.jpg')
        st.image(image, caption='Lily', width = 200)
    elif villager_two == 'Linberg':
        image = Image.open('linberg.png')
        st.image(image, caption='Linberg', width = 200)
    elif villager_two == 'Lionel':
        image = Image.open('lionel.png')
        st.image(image, caption='Lionel', width = 200)
    elif villager_two == 'Lobo':
        image = Image.open('lobo.jpg')
        st.image(image, caption='Lobo', width = 200)
    elif villager_two == 'Lolly':
        image = Image.open('lolly.png')
        st.image(image, caption='Lolly', width = 200)
    elif villager_two == 'Lopez':
        image = Image.open('lopez.png')
        st.image(image, caption='Lopez', width = 200)
    elif villager_two == 'Louie':
        image = Image.open('louie.png')
        st.image(image, caption='Louie', width = 200)
    elif villager_two == 'Lucha':
        image = Image.open('lucha.png')
        st.image(image, caption='Lucha', width = 200)
    elif villager_two == 'Lucky':
        image = Image.open('lucky.png')
        st.image(image, caption='Lucky', width = 200)
    elif villager_two == 'Lucy':
        image = Image.open('lucy.png')
        st.image(image, caption='Lucy', width = 200)
    elif villager_two == 'Lyman':
        image = Image.open('lyman.jpg')
        st.image(image, caption='Lyman', width = 200)
    #-------------------------------------------------------
    #M's
    elif villager_two == 'Mac':
        image = Image.open('mac.png')
        st.image(image, caption='Mac', width = 200)
    elif villager_two == 'Maddie':
        image = Image.open('maddie.png')
        st.image(image, caption='Maddie', width = 200)
    elif villager_two == 'Maelle':
        image = Image.open('maella.jpg')
        st.image(image, caption='Maelle', width = 200)
    elif villager_two == 'Maggie':
        image = Image.open('maggie.png')
        st.image(image, caption='Maggie', width = 200)
    elif villager_two == 'Mallary':
        image = Image.open('mallary.png')
        st.image(image, caption='Mallary', width = 200)
    elif villager_two == 'Maple':
        image = Image.open('maple.jpg')
        st.image(image, caption='Maple', width = 200)
    elif villager_two == 'Marcel':
        image = Image.open('marcel.png')
        st.image(image, caption='Marcel', width = 200)
    elif villager_two == 'Marcie':
        image = Image.open('marcie.png')
        st.image(image, caption='Marcie', width = 200)
    elif villager_two == 'Margie':
        image = Image.open('margie.png')
        st.image(image, caption='Margie', width = 200)
    elif villager_two == 'Marina':
        image = Image.open('marina.jpg')
        st.image(image, caption='Marina', width = 200)
    elif villager_two == 'Marshal':
        image = Image.open('marshal.png')
        st.image(image, caption='marshal', width = 200)
    elif villager_two == 'Mathilda':
        image = Image.open('mathilda.png')
        st.image(image, caption='Mathilda', width = 200)
    elif villager_two == 'Megan':
        image = Image.open('megan.png')
        st.image(image, caption='Megan', width = 200)
    elif villager_two == 'Melba':
        image = Image.open('melba.jpg')
        st.image(image, caption='Melba', width = 200)
    elif villager_two == 'Merengue':
        image = Image.open('merengue.jpg')
        st.image(image, caption='Merengue', width = 200)
    elif villager_two == 'Merry':
        image = Image.open('merry.jpg')
        st.image(image, caption='Merry', width = 200)
    elif villager_two == 'Midge':
        image = Image.open('midge.png')
        st.image(image, caption='Midge', width = 200)
    elif villager_two == 'Mint':
        image = Image.open('mint.png')
        st.image(image, caption='Mint', width = 200)
    elif villager_two == 'Mira':
        image = Image.open('mira.png')
        st.image(image, caption='Mira', width = 200)
    elif villager_two == 'Miranda':
        image = Image.open('miranda.jpg')
        st.image(image, caption='Miranda', width = 200)
    elif villager_two == 'Mitzi':
        image = Image.open('mitzi.png')
        st.image(image, caption='Mitzi', width = 200)
    elif villager_two == 'Moe':
        image = Image.open('moe.png')
        st.image(image, caption='Moe', width = 200)
    elif villager_two == 'Molly':
        image = Image.open('molly.png')
        st.image(image, caption='Molly', width = 200)
    elif villager_two == 'Monique':
        image = Image.open('monique.jpg')
        st.image(image, caption='Monique', width = 200)
    elif villager_two == 'Monty':
        image = Image.open('monty.png')
        st.image(image, caption='Monty', width = 200)
    elif villager_two == 'Moose':
        image = Image.open('moose.jpg')
        st.image(image, caption='Moose', width = 200)
    elif villager_two == 'Mott':
        image = Image.open('mott.jpg')
        st.image(image, caption='Mott', width = 200)
    elif villager_two == 'Muffy':
        image = Image.open('muffy.png')
        st.image(image, caption='Muffy', width = 200)
    elif villager_two == 'Murphy':
        image = Image.open('murphy.png')
        st.image(image, caption='Murphy', width = 200)
    #-----------------------------------------------------
    #N's
    elif villager_two == 'Nan':
        image = Image.open('nan.png')
        st.image(image, caption='Nan', width = 200)
    elif villager_two == 'Nana':
        image = Image.open('Nana.png')
        st.image(image, caption='Nana', width = 200)
    elif villager_two == 'Naomi':
        image = Image.open('naomi.png')
        st.image(image, caption='Naomi', width = 200)
    elif villager_two == 'Nate':
        image = Image.open('nate.png')
        st.image(image, caption='Nate', width = 200)
    elif villager_two == 'Nibbles':
        image = Image.open('nibbles.png')
        st.image(image, caption='Nibbles', width = 200)
    elif villager_two == 'Norma':
        image = Image.open('norma.png')
        st.image(image, caption='Norma', width = 200)
    #---------------------------------------------------
    #O's
    elif villager_two == 'Octavian':
        image = Image.open('octavian.png')
        st.image(image, caption='Ocvtavian', width = 200)
    elif villager_two == 'Ohare':
        image = Image.open('ohare.jpg')
        st.image(image, caption='Ohare', width = 200)
    elif villager_two == 'Olaf':
        image = Image.open('olaf.png')
        st.image(image, caption='olaf', width = 200)
    elif villager_two == 'Olive':
        image = Image.open('olive.png')
        st.image(image, caption='Olive', width = 200)
    elif villager_two == 'Olivia':
        image = Image.open('olivia.png')
        st.image(image, caption='Olivia', width = 200)
    elif villager_two == 'Opal':
        image = Image.open('opal.png')
        st.image(image, caption='Opal', width = 200)
    elif villager_two == 'Ozzie':
        image = Image.open('ozzie.jpg')
        st.image(image, caption='Ozzie', width = 200)
    #---------------------------------------------------
    #P's
    elif villager_two == 'Pango':
        image = Image.open('pango.jpg')
        st.image(image, caption='Pango', width = 200)
    elif villager_two == 'Paolo':
        image = Image.open('paolo.png')
        st.image(image, caption='Paolo', width = 200)
    elif villager_two == 'Papi':
        image = Image.open('Papi.jpg')
        st.image(image, caption='Papi', width = 200)
    elif villager_two == 'Pashmina':
        image = Image.open('pashmina.jpg')
        st.image(image, caption='Pashmina', width = 200)
    elif villager_two == 'Pate':
        image = Image.open('pate.png')
        st.image(image, caption='Pate', width = 200)
    elif villager_two == 'Patty':
        image = Image.open('patty.png')
        st.image(image, caption='Patty', width = 200)
    elif villager_two == 'Paula':
        image = Image.open('paula.png')
        st.image(image, caption='Paula', width = 200)
    elif villager_two == 'Peaches':
        image = Image.open('peaches.jpg')
        st.image(image, caption='Peaches', width = 200)
    elif villager_two == 'Peanut':
        image = Image.open('peanut.jpg')
        st.image(image, caption='Peanut', width = 200)
    elif villager_two == 'Pecan':
        image = Image.open('pecan.png')
        st.image(image, caption='Pecan', width = 200)
    elif villager_two == 'Peck':
        image = Image.open('peck.png')
        st.image(image, caption='Peck', width = 200)
    elif villager_two == 'Peewee':
        image = Image.open('peewee.png')
        st.image(image, caption='Peewee', width = 200)
    elif villager_two == 'Peggy':
        image = Image.open('peggy.png')
        st.image(image, caption='Peggy', width = 200)
    elif villager_two == 'Pekoe':
        image = Image.open('pekoe.jpg')
        st.image(image, caption='Pekoe', width = 200)
    elif villager_two == 'Pencetti':
        image = Image.open('pencetti.png')
        st.image(image, caption='Pencetti', width = 200)
    elif villager_two == 'Penelope':
        image = Image.open('penelope.png')
        st.image(image, caption='Penelope', width = 200)
    elif villager_two == 'Phil':
        image = Image.open('phil.jpg')
        st.image(image, caption='Phil', width = 200)
    elif villager_two == 'Phoebe':
        image = Image.open('phoebe.png')
        st.image(image, caption='Phoebe', width = 200)
    elif villager_two == 'Pierce':
        image = Image.open('pierce.png')
        st.image(image, caption='Pierce', width = 200)
    elif villager_two == 'Pietro':
        image = Image.open('pietro.jpg')
        st.image(image, caption='Pierto', width = 200)
    elif villager_two == 'Pinky':
        image = Image.open('pinky.jpg')
        st.image(image, caption='Pinky', width = 200)
    elif villager_two == 'Piper':
        image = Image.open('piper.png')
        st.image(image, caption='Piper', width = 200)
    elif villager_two == 'Pippy':
        image = Image.open('pippy.jpg')
        st.image(image, caption='Pippy', width = 200)
    elif villager_two == 'Plucky':
        image = Image.open('plucky.png')
        st.image(image, caption='Plucky', width = 200)
    elif villager_two == 'Pompom':
        image = Image.open('pompom.png')
        st.image(image, caption='Pompom', width = 200)
    elif villager_two == 'Poncho':
        image = Image.open('poncho.jpg')
        st.image(image, caption='Poncho', width = 200)
    elif villager_two == 'Poppy':
        image = Image.open('poppy.jpg')
        st.image(image, caption='Poppy', width = 200)
    elif villager_two == 'Portia':
        image = Image.open('portia.png')
        st.image(image, caption='Portia', width = 200)
    elif villager_two == 'Prince':
        image = Image.open('prince.png')
        st.image(image, caption='Prince', width = 200)
    elif villager_two == 'Puck':
        image = Image.open('puck.png')
        st.image(image, caption='Puck', width = 200)
    elif villager_two == 'Puddles':
        image = Image.open('puddles.png')
        st.image(image, caption='Puddles', width = 200)
    elif villager_two == 'Pudge':
        image = Image.open('pudge.jpg')
        st.image(image, caption='Pudge', width = 200)
    elif villager_two == 'Punchy':
        image = Image.open('punchy.png')
        st.image(image, caption='Punchy', width = 200)
    elif villager_two == 'Purrl':
        image = Image.open('purrl.jpg')
        st.image(image, caption='Purrl', width = 200)
    #-----------------------------------------
    #Q's
    elif villager_two == 'Queenie':
        image = Image.open('queenie.png')
        st.image(image, caption='Queenie', width = 200)
    elif villager_two == 'Quillson':
        image = Image.open('quillson.png')
        st.image(image, caption='Quillson', width = 200)
    #-------------------------------------------
    #R's
    elif villager_two == 'Raddle':
        image = Image.open('raddle.png')
        st.image(image, caption='Raddle', width = 200)
    elif villager_two == 'Rasher':
        image = Image.open('rasher.png')
        st.image(image, caption='Rasher', width = 200)
    elif villager_two == 'Raymond':
        image = Image.open('raymond.jpg')
        st.image(image, caption='Raymond', width = 200)
    elif villager_two == 'Renee':
        image = Image.open('renee.png')
        st.image(image, caption='Renee', width = 200)
    elif villager_two == 'Reneigh':
        image = Image.open('reneigh.png')
        st.image(image, caption='Reneigh', width = 200)
    elif villager_two == 'Rex':
        image = Image.open('rex.png')
        st.image(image, caption='Rex', width = 200)
    elif villager_two == 'Rhonda':
        image = Image.open('rhonda.jpg')
        st.image(image, caption='Rhonda', width = 200)
    elif villager_two == 'Ribbot':
        image = Image.open('ribbot.jpg')
        st.image(image, caption='Ribbot', width = 200)
    elif villager_two == 'Ricky':
        image = Image.open('Ricky.jpg')
        st.image(image, caption='Ricky', width = 200)
    elif villager_two == 'Rizzo':
        image = Image.open('rizzo.png')
        st.image(image, caption='Rizzo', width = 200)
    elif villager_two == 'Roald':
        image = Image.open('roald.jpg')
        st.image(image, caption='Roald', width = 200)
    elif villager_two == 'Robin':
        image = Image.open('robin.jpg')
        st.image(image, caption='Robin', width = 200)
    elif villager_two == 'Rocco':
        image = Image.open('rocco.jpg')
        st.image(image, caption='Rocco', width = 200)
    elif villager_two == 'Rocket':
        image = Image.open('rocket.png')
        st.image(image, caption='Rocket', width = 200)
    elif villager_two == 'Rod':
        image = Image.open('Rod.png')
        st.image(image, caption='Rod', width = 200)
    elif villager_two == 'Rodeo':
        image = Image.open('rodeo.png')
        st.image(image, caption='rodeo', width = 200)
    elif villager_two == 'Rodney':
        image = Image.open('rodney.png')
        st.image(image, caption='Rodney', width = 200) 
    elif villager_two == 'Rolf':
        image = Image.open('rolf.jpg')
        st.image(image, caption='Rolf', width = 200)
    elif villager_two == 'Rooney':
        image = Image.open('rooney.png')
        st.image(image, caption='Rooney', width = 200)
    elif villager_two == 'Rory':
        image = Image.open('rory.jpg')
        st.image(image, caption='Rory', width = 200)
    elif villager_two == 'Roscoe':
        image = Image.open('roscoe.png')
        st.image(image, caption='Roscoe', width = 200)
    elif villager_two == 'Rosie':
        image = Image.open('Rosie.png')
        st.image(image, caption='Rosie', width = 200)
    elif villager_two == 'Rowan':
        image = Image.open('rowan.jpg')
        st.image(image, caption='Rowan', width = 200)
    elif villager_two == 'Ruby':
        image = Image.open('ruby.png')
        st.image(image, caption='Ruby', width = 200)
    elif villager_two == 'Rudy':
        image = Image.open('rudy.png')
        st.image(image, caption='Rudy', width = 200)
    #----------------------------------------------------
    #S's
    elif villager_two == 'Sally':
        image = Image.open('sally.png')
        st.image(image, caption='Sally', width = 200)
    elif villager_two == 'Samson':
        image = Image.open('samson.png')
        st.image(image, caption='Samson', width = 200)
    elif villager_two == 'Sandy':
        image = Image.open('sandy.png')
        st.image(image, caption='Sandy', width = 200)
    elif villager_two == 'Savannah':
        image = Image.open('Savannah.png')
        st.image(image, caption='Savannah', width = 200)
    elif villager_two == 'Scoot':
        image = Image.open('scoot.png')
        st.image(image, caption='Scoot', width = 200)
    elif villager_two == 'Shari':
        image = Image.open('shari.png')
        st.image(image, caption='Shari', width = 200)
    elif villager_two == 'Sheldon':
        image = Image.open('sheldon.png')
        st.image(image, caption='Sheldon', width = 200)
    elif villager_two == 'Shep':
        image = Image.open('shep.jpg')
        st.image(image, caption='Shep', width = 200)
    elif villager_two == 'Sherb':
        image = Image.open('sherb.png')
        st.image(image, caption='Sherb', width = 200)
    elif villager_two == 'Simon':
        image = Image.open('simon.jpg')
        st.image(image, caption='Simon', width = 200)
    elif villager_two == 'Skye':
        image = Image.open('skye.png')
        st.image(image, caption='Skye', width = 200)
    elif villager_two == 'Sly':
        image = Image.open('sly.png')
        st.image(image, caption='Sly', width = 200)
    elif villager_two == 'Snake':
        image = Image.open('snake.png')
        st.image(image, caption='snake', width = 200)
    elif villager_two == 'Snooty':
        image = Image.open('snooty.png')
        st.image(image, caption='Snooty', width = 200)
    elif villager_two == 'Soleil':
        image = Image.open('Soleil.png')
        st.image(image, caption='Soleil', width = 200)
    elif villager_two == 'Sparro':
        image = Image.open('Sparro.jpg')
        st.image(image, caption='Sparro', width = 200)
    elif villager_two == 'Spike':
        image = Image.open('spike.png')
        st.image(image, caption='Spike', width = 200)
    elif villager_two == 'Spork':
        image = Image.open('spork.png')
        st.image(image, caption='spork', width = 200)
    elif villager_two == 'Sprinkle':
        image = Image.open('sprinkle.png')
        st.image(image, caption='sprinkle', width = 200)
    elif villager_two == 'Sprocket':
        image = Image.open('sprocket.png')
        st.image(image, caption='sprocket', width = 200)
    elif villager_two == 'Static':
        image = Image.open('static.png')
        st.image(image, caption='Static', width = 200)
    elif villager_two == 'Stella':
        image = Image.open('stella.png')
        st.image(image, caption='stella', width = 200)
    elif villager_two == 'Sterling':
        image = Image.open('sterling.jpg')
        st.image(image, caption='sterling', width = 200)
    elif villager_two == 'Stinky':
        image = Image.open('stinky.png')
        st.image(image, caption='Stinky', width = 200)
    elif villager_two == 'Stitches':
        image = Image.open('stitches.png')
        st.image(image, caption='stitches', width = 200)
    elif villager_two == 'Stu':
        image = Image.open('stu.png')
        st.image(image, caption='Stu', width = 200)
    elif villager_two == 'Sydney':
        image = Image.open('sydney.png')
        st.image(image, caption='Sydney', width = 200)
    elif villager_two == 'Sylvia':
        image = Image.open('sylvia.jpg')
        st.image(image, caption='Sylvia', width = 200)
    #---------------------------------------------------------
    #T's
    elif villager_two == 'Tabby':
        image = Image.open('tabby.png')
        st.image(image, caption='Tabby', width = 200)
    elif villager_two == 'Tad':
        image = Image.open('tad.png')
        st.image(image, caption='Tad', width = 200)
    elif villager_two == 'Tammi':
        image = Image.open('tammi.png')
        st.image(image, caption='Tammi', width = 200)
    elif villager_two == 'Tammy':
        image = Image.open('tammy.jpg')
        st.image(image, caption='Tammy', width = 200)
    elif villager_two == 'Tangy':
        image = Image.open('tangy.jpg')
        st.image(image, caption='Tangy', width = 200)
    elif villager_two == 'Tank':
        image = Image.open('tank.png')
        st.image(image, caption='Tank', width = 200)
    elif villager_two == 'Tasha':
        image = Image.open('tasha.png')
        st.image(image, caption='Tasha', width = 200)
    elif villager_two == 'Tbone':
        image = Image.open('tbone.png')
        st.image(image, caption='Tbone', width = 200)
    elif villager_two == 'Teddy':
        image = Image.open('teddy.jpg')
        st.image(image, caption='Teddy', width = 200)
    elif villager_two == 'Tex':
        image = Image.open('tex.jpg')
        st.image(image, caption='Tex', width = 200)
    elif villager_two == 'Tia':
        image = Image.open('tia.png')
        st.image(image, caption='Tia', width = 200)
    elif villager_two == 'Tiffany':
        image = Image.open('tiffany.png')
        st.image(image, caption='Tiffany', width = 200)
    elif villager_two == 'Timbra':
        image = Image.open('timbra.png')
        st.image(image, caption='Timbra', width = 200)
    elif villager_two == 'Tipper':
        image = Image.open('tipper.png')
        st.image(image, caption='tipper', width = 200)
    elif villager_two == 'Tom':
        image = Image.open('tom.png')
        st.image(image, caption='Tom', width = 200)
    elif villager_two == 'Truffles':
        image = Image.open('truffles.jpg')
        st.image(image, caption='truffles', width = 200)
    elif villager_two == 'Tucker':
        image = Image.open('tucker.png')
        st.image(image, caption='Tucker', width = 200)
    elif villager_two == 'Tutu':
        image = Image.open('tutu.png')
        st.image(image, caption='Tutu', width = 200)
    elif villager_two == 'Twiggy':
        image = Image.open('twiggy/jpg')
        st.image(image, caption='Twiggy', width = 200)
    elif villager_two == 'Tybalt':
        image = Image.open('tybalt.png')
        st.image(image, caption='Tybalt', width = 200)
    #-------------------------------------------------
    #U's
    elif villager_two == 'Ursala':
        image = Image.open('ursala.png')
        st.image(image, caption='Ursala', width = 200)
    #--------------------------------------------------
    #V's
    elif villager_two == 'Velma':
        image = Image.open('velma.png')
        st.image(image, caption='Velma', width = 200)
    elif villager_two == 'Vesta':
        image = Image.open('vesta.jpg')
        st.image(image, caption='Vesta', width = 200)
    elif villager_two == 'Vic':
        image = Image.open('vic.png')
        st.image(image, caption='Vic', width = 200)
    elif villager_two == 'Victoria':
        image = Image.open('victoria.jpg')
        st.image(image, caption='Victoria', width = 200)
    elif villager_two == 'Violet':
        image = Image.open('violet.png')
        st.image(image, caption='Violet', width = 200)
    elif villager_two == 'Vivian':
        image = Image.open('vivian.png')
        st.image(image, caption='Vivian', width = 200)
    elif villager_two == 'Vladmir':
        image = Image.open('vladmir.jpg')
        st.image(image, caption='Vladmir', width = 200)
    #---------------------------------------------------
    #W's
    elif villager_two == 'Wade':
        image = Image.open('wade.png')
        st.image(image, caption='Wade', width = 200)
    elif villager_two == 'Walker':
        image = Image.open('walker.png')
        st.image(image, caption='Walker', width = 200)
    elif villager_two == 'Walt':
        image = Image.open('walt.jpg')
        st.image(image, caption='Walt', width = 200)
    elif villager_two == 'Wartjr':
        image = Image.open('wartjr.png')
        st.image(image, caption='WartJr', width = 200)
    elif villager_two == 'Weber':
        image = Image.open('weber.png')
        st.image(image, caption='Weber', width = 200)
    elif villager_two == 'Wendy':
        image = Image.open('wendy.png')
        st.image(image, caption='Wendy', width = 200)
    elif villager_two == 'Whitney':
        image = Image.open('whitney.jpg')
        st.image(image, caption='Whitney', width = 200)
    elif villager_two == 'Willow':
        image = Image.open('willow.png')
        st.image(image, caption='Willow', width = 200)
    elif villager_two == 'Winnie':
        image = Image.open('winnie.png')
        st.image(image, caption='Winnie', width = 200)
    elif villager_two == 'Wolfgang':
        image = Image.open('wolfgang.jpg')
        st.image(image, caption='Wolfgang', width = 200)
    #------------------------------------------------------
    #Y's
    elif villager_two == 'Yuka':
        image = Image.open('yuka.png')
        st.image(image, caption='Yuka', width = 200)
    #----------------------------------------------------
    #Z's
    elif villager_two == 'Zell':
        image = Image.open('zell.png')
        st.image(image, caption='Zell', width = 200)
    elif villager_two == 'Zucker':
        image = Image.open('zucker.jpg')
        st.image(image, caption='Zucker', width = 200)
