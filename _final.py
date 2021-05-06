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
    #------------------------------
    #------------------------------------------------------------------
    #changes:
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
    elif select_villagers == 'Amelia':
        image = Image.open('amelia.png')
        st.image(image, caption='Amelia', width = 200)
    elif select_villagers == 'Anabelle':
        image = Image.open('anabelle.jpg')
        st.image(image, caption='Anabelle', width = 200)
    elif select_villagers == 'Anchovy':
        image = Image.open('anchovy.jpg')
        st.image(image, caption='Anchovy', width = 200)
    elif select_villagers == 'Angus':
        image = Image.open('angus.jpg')
        st.image(image, caption='Angus', width = 200)
    elif select_villagers == 'Anicotti':
        image = Image.open('anicotti.png')
        st.image(image, caption='Anicotti', width = 200)
    elif select_villagers == 'Ankha':
        image = Image.open('ankha.jpg')
        st.image(image, caption='Ankha', width = 200)
    elif select_villagers == 'Annalisa':
        image = Image.open('annalisa.png')
        st.image(image, caption='Annalisa', width = 200)
    elif select_villagers == 'Annalise':
        image = Image.open('annalise.jpg')
        st.image(image, caption='Annalise', width = 200)
    elif select_villagers == 'Antonio':
        image = Image.open('antonio.png')
        st.image(image, caption='Antonio', width = 200)
    elif select_villagers == 'Apollo':
        image = Image.open('apollo.jpg')
        st.image(image, caption='Apollo', width = 200)
    elif select_villagers == 'Apple':
        image = Image.open('apple.jpg')
        st.image(image, caption='Apple', width = 200)
    elif select_villagers == 'Astrid':
        image = Image.open('astrid.jpg')
        st.image(image, caption='Astrid', width = 200)
    elif select_villagers == 'Audie':
        image = Image.open('audie.png')
        st.image(image, caption='Audie', width = 200)
    elif select_villagers == 'Aurora':
        image = Image.open('aurora.png')
        st.image(image, caption='Aurora', width = 200)
    elif select_villagers == 'Ava':
        image = Image.open('ava.jpg')
        st.image(image, caption='Ava', width = 200)
    elif select_villagers == 'Avery':
        image = Image.open('avery.png')
        st.image(image, caption='Avery', width = 200)
    elif select_villagers == 'Axel':
        image = Image.open('axel.png')
        st.image(image, caption='Axel', width = 200)
    #-----------------------------------------------
    #B's
    elif select_villagers == 'Baabara':
        image = Image.open('baabra.jpg')
        st.image(image, caption='Baabra', width = 200)
    elif select_villagers == 'Bam':
        image = Image.open('bam.jpg')
        st.image(image, caption='Bam', width = 200)
    elif select_villagers == 'Bangle':
        image = Image.open('bangle.png')
        st.image(image, caption='Bangle', width = 200)
    elif select_villagers == 'Barold':
        image = Image.open('barold.jpg')
        st.image(image, caption='Barold', width = 200)
    elif select_villagers == 'Bea':
        image = Image.open('bea.png')
        st.image(image, caption='Bea', width = 200)
    elif select_villagers == 'Beardo':
        image = Image.open('beardo.png')
        st.image(image, caption='Beardo', width = 200)
    elif select_villagers == 'Beau':
        image = Image.open('beau.png')
        st.image(image, caption='Beau', width = 200)
    elif select_villagers == 'Becky':
        image = Image.open('becky.jpg')
        st.image(image, caption='Becky', width = 200)
    elif select_villagers == 'Bella':
        image = Image.open('bella.png')
        st.image(image, caption='Bella', width = 200)
    elif select_villagers == 'Benedict':
        image = Image.open('benedict.png')
        st.image(image, caption='Benedict', width = 200)
    elif select_villagers == 'Benjamin':
        image = Image.open('benjamin.png')
        st.image(image, caption='Benjamin', width = 200)
    elif select_villagers == 'Bertha':
        image = Image.open('bertha.jpg')
        st.image(image, caption='Bertha', width = 200)
    elif select_villagers == 'Bettina':
        image = Image.open('bettina.png')
        st.image(image, caption='Bettina', width = 200)
    elif select_villagers == 'Bianca':
        image = Image.open('bianca.jpg')
        st.image(image, caption='Bianca', width = 200)
    elif select_villagers == 'Biff':
        image = Image.open('biff.png')
        st.image(image, caption='Biff', width = 200)
    elif select_villagers == 'Big Top':
        image = Image.open('bigtop.png')
        st.image(image, caption='Big Top', width = 200)
    elif select_villagers == 'Bill':
        image = Image.open('bill.png')
        st.image(image, caption='Bill', width = 200)
    elif select_villagers == 'Billy':
        image = Image.open('billy.jpg')
        st.image(image, caption='Billy', width = 200)
    elif select_villagers == 'Biskit':
        image = Image.open('biskit.jpg')
        st.image(image, caption='Biskit', width = 200)
    elif select_villagers == 'Bitty':
        image = Image.open('bitty.png')
        st.image(image, caption='Bitty', width = 200)
    elif select_villagers == 'Blaire':
        image = Image.open('blaire.png')
        st.image(image, caption='Blaire', width = 200)
    elif select_villagers == 'Blanche':
        image = Image.open('blanche.jpg')
        st.image(image, caption='Blanche', width = 200)
    elif select_villagers == 'Bluebear':
        image = Image.open('bluebear.png')
        st.image(image, caption='Bluebear', width = 200)
    elif select_villagers == 'Bob':
        image = Image.open('Bob.jpg')
        st.image(image, caption='Bob', width = 200)
    elif select_villagers == 'Bonbon':
        image = Image.open('bonbon.png')
        st.image(image, caption='Bonbon', width = 200)
    elif select_villagers == 'Bones':
        image = Image.open('bones.png')
        st.image(image, caption='Bones', width = 200)
    elif select_villagers == 'Boomer':
        image = Image.open('boomer.jpg')
        st.image(image, caption='Boomer', width = 200)
    elif select_villagers == 'Boone':
        image = Image.open('boone.jpg')
        st.image(image, caption='Boone', width = 200)
    elif select_villagers == 'Boots':
        image = Image.open('boots.jpg')
        st.image(image, caption='Boots', width = 200)
    elif select_villagers == 'Boris':
        image = Image.open('boris.png')
        st.image(image, caption='Boris', width = 200)
    elif select_villagers == 'Boyd':
        image = Image.open('boyd.png')
        st.image(image, caption='Boyd', width = 200)
    elif select_villagers == 'Bree':
        image = Image.open('bree.jpg')
        st.image(image, caption='Bree', width = 200)
    elif select_villagers == 'Broccolo':
        image = Image.open('broccolo.png')
        st.image(image, caption='Brocollo', width = 200)
    elif select_villagers == 'Broffina':
        image = Image.open('broffina.jpg')
        st.image(image, caption='Broffina', width = 200)
    elif select_villagers == 'Bruce':
        image = Image.open('bruce.jpg')
        st.image(image, caption='Bruce', width = 200)
    elif select_villagers == 'Bubbles':
        image = Image.open('bubbles.jpg')
        st.image(image, caption='Bubbles', width = 200)
    elif select_villagers == 'Buck':
        image = Image.open('buck.jpg')
        st.image(image, caption='Buck', width = 200)
    elif select_villagers == 'Bud':
        image = Image.open('bud.png')
        st.image(image, caption='Bud', width = 200)
    elif select_villagers == 'Bunnie':
        image = Image.open('bunnie.png')
        st.image(image, caption='Bunnie', width = 200)
    elif select_villagers == 'Butch':
        image = Image.open('butch.png')
        st.image(image, caption='Butch', width = 200)
    elif select_villagers == 'Buzz':
        image = Image.open('buzz.png')
        st.image(image, caption='Buzz', width = 200)
    #-----------------------------------------------
    #C's
    elif select_villagers == 'Cally':
        image = Image.open('cally.png')
        st.image(image, caption='Cally', width = 200)
    elif select_villagers == 'Camofrog':
        image = Image.open('camofrog.png')
        st.image(image, caption='Camofrog', width = 200)
    elif select_villagers == 'Canberra':
        image = Image.open('canberra.png')
        st.image(image, caption='Canberra', width = 200)
    elif select_villagers == 'Candi':
        image = Image.open('candi.png')
        st.image(image, caption='Candi', width = 200)
    elif select_villagers == 'Carmen':
        image = Image.open('carmen.jpg')
        st.image(image, caption='carmen', width = 200)
    elif select_villagers == 'Caroline':
        image = Image.open('caroline.png')
        st.image(image, caption='Caroline', width = 200)
    elif select_villagers == 'Carrie':
        image = Image.open('carrie.png')
        st.image(image, caption='Carrie', width = 200)
    elif select_villagers == 'Cashmere':
        image = Image.open('cashmere.png')
        st.image(image, caption='Cashmere', width = 200)
    elif select_villagers == 'Celia':
        image = Image.open('Celia.jpg')
        st.image(image, caption='Celia', width = 200)
    elif select_villagers == 'Cesar':
        image = Image.open('cesar.png')
        st.image(image, caption='Cesar', width = 200)
    elif select_villagers == 'Chadder':
        image = Image.open('chadder.jpg')
        st.image(image, caption='Chadder', width = 200)
    elif select_villagers == 'Charlise':
        image = Image.open('charlise.png')
        st.image(image, caption='Charlise', width = 200)
    elif select_villagers == 'Cheri':
        image = Image.open('cheri.png')
        st.image(image, caption='Cheri', width = 200)
    elif select_villagers == 'Cherry':
        image = Image.open('cherry.jpg')
        st.image(image, caption='Cherry', width = 200)
    elif select_villagers == 'Chester':
        image = Image.open('chester.jpg')
        st.image(image, caption='Chester', width = 200)
    elif select_villagers == 'Chevre':
        image = Image.open('chevre.png')
        st.image(image, caption='Chevre', width = 200)
    elif select_villagers == 'Chief':
        image = Image.open('chief.jpg')
        st.image(image, caption='Chief', width = 200)
    elif select_villagers == 'Chops':
        image = Image.open('chops.png')
        st.image(image, caption='Chops', width = 200)
    elif select_villagers == 'Chow':
        image = Image.open('chow.jpg')
        st.image(image, caption='Chow', width = 200)
    elif select_villagers == 'Chrissy':
        image = Image.open('chrissy.jpg')
        st.image(image, caption='Chrissy', width = 200)
    elif select_villagers == 'Claude':
        image = Image.open('claude.png')
        st.image(image, caption='Claude', width = 200)
    elif select_villagers == 'Claudia':
        image = Image.open('claudia.jpg')
        st.image(image, caption='Claudia', width = 200)
    elif select_villagers == 'Clay':
        image = Image.open('clay.png')
        st.image(image, caption='Clay', width = 200)
    elif select_villagers == 'Cleo':
        image = Image.open('cleo.png')
        st.image(image, caption='Cleo', width = 200)
    elif select_villagers == 'Clyde':
        image = Image.open('clyde.png')
        st.image(image, caption='Clyde', width = 200)
    elif select_villagers == 'Coach':
        image = Image.open('coach.jpg')
        st.image(image, caption='Coach', width = 200)
    elif select_villagers == 'Cobb':
        image = Image.open('cobb.png')
        st.image(image, caption='Cobb', width = 200)
    elif select_villagers == 'Coco':
        image = Image.open('coco.jpg')
        st.image(image, caption='Coco', width = 200)
    elif select_villagers == 'Cole':
        image = Image.open('cole.jpg')
        st.image(image, caption='Cole', width = 200)
    elif select_villagers == 'Colton':
        image = Image.open('colton.jpg')
        st.image(image, caption='Colton', width = 200)
    elif select_villagers == 'Cookie':
        image = Image.open('cookie.png')
        st.image(image, caption='Cookie', width = 200)
    elif select_villagers == 'Cousteau':
        image = Image.open('cousteau.jpg')
        st.image(image, caption='Cousteau', width = 200)
    elif select_villagers == 'Cranston':
        image = Image.open('cranston.jpg')
        st.image(image, caption='Cranston', width = 200)
    elif select_villagers == 'Croque':
        image = Image.open('croque.jpg')
        st.image(image, caption='Croque', width = 200)
    elif select_villagers == 'Cube':
        image = Image.open('cube.png')
        st.image(image, caption='Cube', width = 200)
    elif select_villagers == 'Curlos':
        image = Image.open('curlos.jpg')
        st.image(image, caption='Curlos', width = 200)
    elif select_villagers == 'Curly':
        image = Image.open('curly.jpg')
        st.image(image, caption='Curly', width = 200)
    elif select_villagers == 'Curt':
        image = Image.open('curtt.jpg')
        st.image(image, caption='Curt', width = 200)
    elif select_villagers == 'Cyd':
        image = Image.open('cyd.jpg')
        st.image(image, caption='Cyd', width = 200)
    elif select_villagers == 'Cyrano':
        image = Image.open('cyrano.png')
        st.image(image, caption='Cyrano', width = 200)
    #--------------------------------------------------
    #D's
    elif select_villagers == 'Daisy':
        image = Image.open('daisy.jpg')
        st.image(image, caption='Daisy', width = 200)
    elif select_villagers == 'Deena':
        image = Image.open('deena.png')
        st.image(image, caption='Deena', width = 200)
    elif select_villagers == 'Deirdre':
        image = Image.open('deidre.jpg')
        st.image(image, caption='Deirdre', width = 200)
    elif select_villagers == 'Del':
        image = Image.open('del.png')
        st.image(image, caption='Del', width = 200)
    elif select_villagers == 'Deli':
        image = Image.open('deli.png')
        st.image(image, caption='Deli', width = 200)
    elif select_villagers == 'Derwin':
        image = Image.open('derwin.jpg')
        st.image(image, caption='Derwin', width = 200)
    elif select_villagers == 'Diana':
        image = Image.open('diana.jpg')
        st.image(image, caption='Diana', width = 200)
    elif select_villagers == 'Diva':
        image = Image.open('diva.jpg')
        st.image(image, caption='Diva', width = 200)
    elif select_villagers == 'Dizzy':
        image = Image.open('dizzy.jpg')
        st.image(image, caption='Dizzy', width = 200)
    elif select_villagers == 'Dobie':
        image = Image.open('dobie.jpg')
        st.image(image, caption='Dobie', width = 200)
    elif select_villagers == 'Doc':
        image = Image.open('Doc.png')
        st.image(image, caption='Doc', width = 200)
    elif select_villagers == 'Dom':
        image = Image.open('dom.png')
        st.image(image, caption='Dom', width = 200)
    elif select_villagers == 'Dora':
        image = Image.open('dora.jpg')
        st.image(image, caption='Dora', width = 200)
    elif select_villagers == 'Dotty':
        image = Image.open('dotty.jpg')
        st.image(image, caption='Dotty', width = 200)
    elif select_villagers == 'Drago':
        image = Image.open('drago.jpg')
        st.image(image, caption='Drago', width = 200)
    elif select_villagers == 'Drake':
        image = Image.open('drake.png')
        st.image(image, caption='Drake', width = 200)
    elif select_villagers == 'Drift':
        image = Image.open('drift.png')
        st.image(image, caption='Drift', width = 200)
    #----------------------------------------------------
    #E's
    elif select_villagers == 'Ed':
        image = Image.open('ed.jpg')
        st.image(image, caption='Ed', width = 200)
    elif select_villagers == 'Egbert':
        image = Image.open('egbert.png')
        st.image(image, caption='Egbert', width = 200)
    elif select_villagers == 'Elise':
        image = Image.open('elise.png')
        st.image(image, caption='Elise', width = 200)
    elif select_villagers == 'Ellie':
        image = Image.open('ellie.png')
        st.image(image, caption='Ellie', width = 200)
    elif select_villagers == 'Elmer':
        image = Image.open('elmer.jpg')
        st.image(image, caption='Elmer', width = 200)
    elif select_villagers == 'Eloise':
        image = Image.open('eloise.png')
        st.image(image, caption='Eloise', width = 200)
    elif select_villagers == 'Elvis':
        image = Image.open('elvis.jpg')
        st.image(image, caption='Elvis', width = 200)
    elif select_villagers == 'Erik':
        image = Image.open('erik.png')
        st.image(image, caption='Erik', width = 200)
    elif select_villagers == 'Eugene':
        image = Image.open('eugene.png')
        st.image(image, caption='Eugene', width = 200)
    elif select_villagers == 'Eunice':
        image = Image.open('eunice.png')
        st.image(image, caption='Eunice', width = 200)
    #-----------------------------------------------------
    #F's
    elif select_villagers == 'Fang':
        image = Image.open('fang.jpg')
        st.image(image, caption='fang', width = 200)
    elif select_villagers == 'Fauna':
        image = Image.open('fauna.png')
        st.image(image, caption='Fauna', width = 200)
    elif select_villagers == 'Felicity':
        image = Image.open('felicity.jpg')
        st.image(image, caption='Felicity', width = 200)
    elif select_villagers == 'Filbert':
        image = Image.open('filbert.jpg')
        st.image(image, caption='Filbert', width = 200)
    elif select_villagers == 'Flip':
        image = Image.open('flip.png')
        st.image(image, caption='Flip', width = 200)
    elif select_villagers == 'Flo':
        image = Image.open('flo.png')
        st.image(image, caption='Flo', width = 200)
    elif select_villagers == 'Flora':
        image = Image.open('flora.jpg')
        st.image(image, caption='Flora', width = 200)
    elif select_villagers == 'Flurry':
        image = Image.open('flurry.png')
        st.image(image, caption='Flurry', width = 200)
    elif select_villagers == 'Francine':
        image = Image.open('francine.jpg')
        st.image(image, caption='Francine', width = 200)
    elif select_villagers == 'Frank':
        image = Image.open('frank.png')
        st.image(image, caption='Frank', width = 200)
    elif select_villagers == 'Freckles':
        image = Image.open('freckles.jpg')
        st.image(image, caption='Freckles', width = 200)
    elif select_villagers == 'Freya':
        image = Image.open('freya.png')
        st.image(image, caption='Freya', width = 200)
    elif select_villagers == 'Friga':
        image = Image.open('friga.jpg')
        st.image(image, caption='Friga', width = 200)
    elif select_villagers == 'Frita':
        image = Image.open('frita.jpg')
        st.image(image, caption='Frita', width = 200)
    elif select_villagers == 'Frobert':
        image = Image.open('frobert.png')
        st.image(image, caption='Frobert', width = 200)
    elif select_villagers == 'Fuchsia':
        image = Image.open('fuchsia.jpg')
        st.image(image, caption='Fuchsia', width = 200)
    #-------------------------------------------------------
    #G's
    elif select_villagers == 'Gabi':
        image = Image.open('gabi.png')
        st.image(image, caption='Gabi', width = 200)
    elif select_villagers == 'Gala':
        image = Image.open('gala.jpg')
        st.image(image, caption='Gala', width = 200)
    elif select_villagers == 'Gaston':
        image = Image.open('gaston.png')
        st.image(image, caption='Gaston', width = 200)
    elif select_villagers == 'Gayle':
        image = Image.open('gayle.jpg')
        st.image(image, caption='Gayle', width = 200)
    elif select_villagers == 'Genji':
        image = Image.open('genji.png')
        st.image(image, caption='Genji', width = 200)
    elif select_villagers == 'Gigi':
        image = Image.open('gigi.jpg')
        st.image(image, caption='Gigi', width = 200)
    elif select_villagers == 'Gladys':
        image = Image.open('gladys.png')
        st.image(image, caption='Gladys', width = 200)
    elif select_villagers == 'Gloria':
        image = Image.open('gloria.png')
        st.image(image, caption='Gloria', width = 200)
    elif select_villagers == 'Goldie':
        image = Image.open('goldie.png')
        st.image(image, caption='Goldie', width = 200)
    elif select_villagers == 'Gonzo':
        image = Image.open('gonzo.png')
        st.image(image, caption='Gonzo', width = 200)
    elif select_villagers == 'Goose':
        image = Image.open('goose.png')
        st.image(image, caption='Goose', width = 200)
    elif select_villagers == 'Graham':
        image = Image.open('graham.jpg')
        st.image(image, caption='Graham', width = 200)
    elif select_villagers == 'Greta':
        image = Image.open('greta.png')
        st.image(image, caption='Greta', width = 200)
    elif select_villagers == 'Grizzly':
        image = Image.open('grizzly.png')
        st.image(image, caption='Grizzly', width = 200)
    elif select_villagers == 'Groucho':
        image = Image.open('groucho.png')
        st.image(image, caption='Groucho', width = 200)
    elif select_villagers == 'Gruff':
        image = Image.open('gruff.png')
        st.image(image, caption='Gruff', width = 200)
    elif select_villagers == 'Gwen':
        image = Image.open('gwen.png')
        st.image(image, caption='Gwen', width = 200)
    #--------------------------------------------------------
    #H's
    elif select_villagers == 'Hamlet':
        image = Image.open('hamlet.png')
        st.image(image, caption='Hamlet', width = 200)
    elif select_villagers == 'Hamphrey':
        image = Image.open('hamphrey.png')
        st.image(image, caption='Hamphrey', width = 200)
    elif select_villagers == 'Hans':
        image = Image.open('hans.png')
        st.image(image, caption='Hans', width = 200)
    elif select_villagers == 'Harry':
        image = Image.open('harry.png')
        st.image(image, caption='Harry', width = 200)
    elif select_villagers == 'Hazel':
        image = Image.open('hazel.jpg')
        st.image(image, caption='Hazel', width = 200)
    elif select_villagers == 'Henry':
        image = Image.open('henry.png')
        st.image(image, caption='Henry', width = 200)
    elif select_villagers == 'Hippeux':
        image = Image.open('hippeux.png')
        st.image(image, caption='Hippeux', width = 200)
    elif select_villagers == 'Hopkins':
        image = Image.open('hopkins.jpg')
        st.image(image, caption='Hopkins', width = 200)
    elif select_villagers == 'Hopper':
        image = Image.open('hopper.png')
        st.image(image, caption='Hopper', width = 200)
    elif select_villagers == 'Hornsby':
        image = Image.open('hornsby.png')
        st.image(image, caption='Hornsby', width = 200)
    elif select_villagers == 'Huck':
        image = Image.open('huck.png')
        st.image(image, caption='Huck', width = 200)
    elif select_villagers == 'Hugh':
        image = Image.open('hugh.jpg')
        st.image(image, caption='Hugh', width = 200)
    #---------------------------------------------------------
    #I's
    elif select_villagers == 'Iggly':
        image = Image.open('iggly.jpg')
        st.image(image, caption='Iggly', width = 200)
    elif select_villagers == 'Ike':
        image = Image.open('ike.png')
        st.image(image, caption='Ike', width = 200)
    #---------------------------------------------------------
    #J's
    elif select_villagers == 'Jacob':
        image = Image.open('jacob.jpg')
        st.image(image, caption='Jacob', width = 200)
    elif select_villagers == 'Jacques':
        image = Image.open('jacques.jpg')
        st.image(image, caption='Jacques', width = 200)
    elif select_villagers == 'Jambette':
        image = Image.open('jambette.png')
        st.image(image, caption='Jambette', width = 200)
    elif select_villagers == 'Jay':
        image = Image.open('jay.jpg')
        st.image(image, caption='Jay', width = 200)
    elif select_villagers == 'Jeremiah':
        image = Image.open('jeremiah.png')
        st.image(image, caption='Jeremiah', width = 200)
    elif select_villagers == 'Jitters':
        image = Image.open('jitters.png')
        st.image(image, caption='Jitters', width = 200)
    elif select_villagers == 'Joey':
        image = Image.open('joey.jpg')
        st.image(image, caption='Joey', width = 200)
    elif select_villagers == 'Judy':
        image = Image.open('judy.png')
        st.image(image, caption='Judy', width = 200)
    elif select_villagers == 'Julia':
        image = Image.open('julia.png')
        st.image(image, caption='Julia', width = 200)
    elif select_villagers == 'Julian':
        image = Image.open('julian.png')
        st.image(image, caption='Julian', width = 200)
    elif select_villagers == 'June':
        image = Image.open('june.jpg')
        st.image(image, caption='June', width = 200)
    #----------------------------------------------------
    #K's
    elif select_villagers == 'Kabuki':
        image = Image.open('kabuki.jpg')
        st.image(image, caption='Kabuki', width = 200)
    elif select_villagers == 'Katt':
        image = Image.open('katt.jpg')
        st.image(image, caption='Katt', width = 200)
    elif select_villagers == 'Keaton':
        image = Image.open('keaton.png')
        st.image(image, caption='Keaton', width = 200)
    elif select_villagers == 'Ken':
        image = Image.open('ken.jpg')
        st.image(image, caption='Ken', width = 200)
    elif select_villagers == 'Ketchup':
        image = Image.open('ketchup.png')
        st.image(image, caption='ketchup', width = 200)
    elif select_villagers == 'Kevin':
        image = Image.open('kevin.png')
        st.image(image, caption='kevin', width = 200)
    elif select_villagers == 'Kid Cat':
        image = Image.open('kid cat.png')
        st.image(image, caption='Kid Cat', width = 200)
    elif select_villagers == 'Kidd':
        image = Image.open('kidd.jpg')
        st.image(image, caption='Kidd', width = 200)
    elif select_villagers == 'Kiki':
        image = Image.open('kiki.png')
        st.image(image, caption='Kiki', width = 200)
    elif select_villagers == 'Kitt':
        image = Image.open('kitt.png')
        st.image(image, caption='Kitt', width = 200)
    elif select_villagers == 'Kitty':
        image = Image.open('kitty.png')
        st.image(image, caption='Kitty', width = 200)
    elif select_villagers == 'Klaus':
        image = Image.open('klaus.png')
        st.image(image, caption='Klaus', width = 200)
    elif select_villagers == 'Knox':
        image = Image.open('knox.png')
        st.image(image, caption='Knox', width = 200)
    elif select_villagers == 'Kody':
        image = Image.open('kody.png')
        st.image(image, caption='Kody', width = 200)
    elif select_villagers == 'Kyle':
        image = Image.open('kyle.jpg')
        st.image(image, caption='Kyle', width = 200)
    #-----------------------------------------------------
    #L's
    elif select_villagers == 'Leonardo':
        image = Image.open('leonardo.png')
        st.image(image, caption='Leonardo', width = 200)
    elif select_villagers == 'Leopold':
        image = Image.open('leopold.png')
        st.image(image, caption='Leopold', width = 200)
    elif select_villagers == 'Lily':
        image = Image.open('lily.jpg')
        st.image(image, caption='Lily', width = 200)
    elif select_villagers == 'Limberg':
        image = Image.open('linberg.png')
        st.image(image, caption='Linberg', width = 200)
    elif select_villagers == 'Lionel':
        image = Image.open('lionel.png')
        st.image(image, caption='Lionel', width = 200)
    elif select_villagers == 'Lobo':
        image = Image.open('lobo.jpg')
        st.image(image, caption='Lobo', width = 200)
    elif select_villagers == 'Lolly':
        image = Image.open('lolly.png')
        st.image(image, caption='Lolly', width = 200)
    elif select_villagers == 'Lopez':
        image = Image.open('lopez.png')
        st.image(image, caption='Lopez', width = 200)
    elif select_villagers == 'Louie':
        image = Image.open('louie.png')
        st.image(image, caption='Louie', width = 200)
    elif select_villagers == 'Lucha':
        image = Image.open('lucha.png')
        st.image(image, caption='Lucha', width = 200)
    elif select_villagers == 'Lucky':
        image = Image.open('lucky.png')
        st.image(image, caption='Lucky', width = 200)
    elif select_villagers == 'Lucy':
        image = Image.open('lucy.png')
        st.image(image, caption='Lucy', width = 200)
    elif select_villagers == 'Lyman':
        image = Image.open('lyman.jpg')
        st.image(image, caption='Lyman', width = 200)
    #-------------------------------------------------------
    #M's
    elif select_villagers == 'Mac':
        image = Image.open('mac.png')
        st.image(image, caption='Mac', width = 200)
    elif select_villagers == 'Maddie':
        image = Image.open('maddie.png')
        st.image(image, caption='Maddie', width = 200)
    elif select_villagers == 'Maelle':
        image = Image.open('maelle.jpg')
        st.image(image, caption='Maelle', width = 200)
    elif select_villagers == 'Maggie':
        image = Image.open('maggie.png')
        st.image(image, caption='Maggie', width = 200)
    elif select_villagers == 'Mallary':
        image = Image.open('mallary.png')
        st.image(image, caption='Mallary', width = 200)
    elif select_villagers == 'Maple':
        image = Image.open('maple.jpg')
        st.image(image, caption='Maple', width = 200)
    elif select_villagers == 'Marcel':
        image = Image.open('marcel.png')
        st.image(image, caption='Marcel', width = 200)
    elif select_villagers == 'Marcie':
        image = Image.open('marcie.jpeg')
        st.image(image, caption='Marcie', width = 200)
    elif select_villagers == 'Margie':
        image = Image.open('margie.png')
        st.image(image, caption='Margie', width = 200)
    elif select_villagers == 'Marina':
        image = Image.open('marina.jpg')
        st.image(image, caption='Marina', width = 200)
    elif select_villagers == 'Marshal':
        image = Image.open('marshal.png')
        st.image(image, caption='marshal', width = 200)
    elif select_villagers == 'Mathilda':
        image = Image.open('mathilda.png')
        st.image(image, caption='Mathilda', width = 200)
    elif select_villagers == 'Megan':
        image = Image.open('megan.png')
        st.image(image, caption='Megan', width = 200)
    elif select_villagers == 'Melba':
        image = Image.open('melba.jpg')
        st.image(image, caption='Melba', width = 200)
    elif select_villagers == 'Merengue':
        image = Image.open('merengue.jpg')
        st.image(image, caption='Merengue', width = 200)
    elif select_villagers == 'Merry':
        image = Image.open('merry.jpg')
        st.image(image, caption='Merry', width = 200)
    elif select_villagers == 'Midge':
        image = Image.open('midge.png')
        st.image(image, caption='Midge', width = 200)
    elif select_villagers == 'Mint':
        image = Image.open('mint.png')
        st.image(image, caption='Mint', width = 200)
    elif select_villagers == 'Mira':
        image = Image.open('mira.png')
        st.image(image, caption='Mira', width = 200)
    elif select_villagers == 'Miranda':
        image = Image.open('miranda.jpg')
        st.image(image, caption='Miranda', width = 200)
    elif select_villagers == 'Mitzi':
        image = Image.open('mitzi.png')
        st.image(image, caption='Mitzi', width = 200)
    elif select_villagers == 'Moe':
        image = Image.open('moe.png')
        st.image(image, caption='Moe', width = 200)
    elif select_villagers == 'Molly':
        image = Image.open('molly.png')
        st.image(image, caption='Molly', width = 200)
    elif select_villagers == 'Monique':
        image = Image.open('monique.jpg')
        st.image(image, caption='Monique', width = 200)
    elif select_villagers == 'Monty':
        image = Image.open('monty.png')
        st.image(image, caption='Monty', width = 200)
    elif select_villagers == 'Moose':
        image = Image.open('moose.jpg')
        st.image(image, caption='Moose', width = 200)
    elif select_villagers == 'Mott':
        image = Image.open('mott.jpg')
        st.image(image, caption='Mott', width = 200)
    elif select_villagers == 'Muffy':
        image = Image.open('muffy.png')
        st.image(image, caption='Muffy', width = 200)
    elif select_villagers == 'Murphy':
        image = Image.open('murphy.png')
        st.image(image, caption='Murphy', width = 200)
    #-----------------------------------------------------
    #N's
    elif select_villagers == 'Nan':
        image = Image.open('nan.png')
        st.image(image, caption='Nan', width = 200)
    elif select_villagers == 'Nana':
        image = Image.open('Nana.png')
        st.image(image, caption='Nana', width = 200)
    elif select_villagers == 'Naomi':
        image = Image.open('naomi.png')
        st.image(image, caption='Naomi', width = 200)
    elif select_villagers == 'Nate':
        image = Image.open('nate.png')
        st.image(image, caption='Nate', width = 200)
    elif select_villagers == 'Nibbles':
        image = Image.open('nibbles.png')
        st.image(image, caption='Nibbles', width = 200)
    elif select_villagers == 'Norma':
        image = Image.open('norma.png')
        st.image(image, caption='Norma', width = 200)
    #---------------------------------------------------
    #O's
    elif select_villagers == 'Octavian':
        image = Image.open('octavian.png')
        st.image(image, caption='Ocvtavian', width = 200)
    elif select_villagers == '''O'Hare''':
        image = Image.open('ohare.jpg')
        st.image(image, caption='Ohare', width = 200)
    elif select_villagers == 'Olaf':
        image = Image.open('olaf.png')
        st.image(image, caption='olaf', width = 200)
    elif select_villagers == 'Olive':
        image = Image.open('olive.png')
        st.image(image, caption='Olive', width = 200)
    elif select_villagers == 'Olivia':
        image = Image.open('olivia.png')
        st.image(image, caption='Olivia', width = 200)
    elif select_villagers == 'Opal':
        image = Image.open('opal.png')
        st.image(image, caption='Opal', width = 200)
    elif select_villagers == 'Ozzie':
        image = Image.open('ozzie.jpg')
        st.image(image, caption='Ozzie', width = 200)
    #---------------------------------------------------
    #P's
    elif select_villagers == 'Pango':
        image = Image.open('pango.jpg')
        st.image(image, caption='Pango', width = 200)
    elif select_villagers == 'Paolo':
        image = Image.open('paolo.png')
        st.image(image, caption='Paolo', width = 200)
    elif select_villagers == 'Papi':
        image = Image.open('Papi.jpg')
        st.image(image, caption='Papi', width = 200)
    elif select_villagers == 'Pashmina':
        image = Image.open('pashmina.jpg')
        st.image(image, caption='Pashmina', width = 200)
    elif select_villagers == 'Pate':
        image = Image.open('pate.png')
        st.image(image, caption='Pate', width = 200)
    elif select_villagers == 'Patty':
        image = Image.open('patty.png')
        st.image(image, caption='Patty', width = 200)
    elif select_villagers == 'Paula':
        image = Image.open('paula.png')
        st.image(image, caption='Paula', width = 200)
    elif select_villagers == 'Peaches':
        image = Image.open('peaches.jpg')
        st.image(image, caption='Peaches', width = 200)
    elif select_villagers == 'Peanut':
        image = Image.open('peanut.jpg')
        st.image(image, caption='Peanut', width = 200)
    elif select_villagers == 'Pecan':
        image = Image.open('pecan.png')
        st.image(image, caption='Pecan', width = 200)
    elif select_villagers == 'Peck':
        image = Image.open('peck.png')
        st.image(image, caption='Peck', width = 200)
    elif select_villagers == 'Peewee':
        image = Image.open('peewee.png')
        st.image(image, caption='Peewee', width = 200)
    elif select_villagers == 'Peggy':
        image = Image.open('peggy.png')
        st.image(image, caption='Peggy', width = 200)
    elif select_villagers == 'Pekoe':
        image = Image.open('pekoe.jpg')
        st.image(image, caption='Pekoe', width = 200)
    elif select_villagers == 'Pancetti':
        image = Image.open('pencetti.png')
        st.image(image, caption='Pancetti', width = 200)
    elif select_villagers == 'Penelope':
        image = Image.open('penelope.png')
        st.image(image, caption='Penelope', width = 200)
    elif select_villagers == 'Phil':
        image = Image.open('phil.jpg')
        st.image(image, caption='Phil', width = 200)
    elif select_villagers == 'Phoebe':
        image = Image.open('phoebe.png')
        st.image(image, caption='Phoebe', width = 200)
    elif select_villagers == 'Pierce':
        image = Image.open('pierce.png')
        st.image(image, caption='Pierce', width = 200)
    elif select_villagers == 'Pietro':
        image = Image.open('pietro.jpg')
        st.image(image, caption='Pierto', width = 200)
    elif select_villagers == 'Pinky':
        image = Image.open('pinky.jpg')
        st.image(image, caption='Pinky', width = 200)
    elif select_villagers == 'Piper':
        image = Image.open('piper.png')
        st.image(image, caption='Piper', width = 200)
    elif select_villagers == 'Pippy':
        image = Image.open('pippy.jpg')
        st.image(image, caption='Pippy', width = 200)
    elif select_villagers == 'Plucky':
        image = Image.open('plucky.png')
        st.image(image, caption='Plucky', width = 200)
    elif select_villagers == 'Pompom':
        image = Image.open('pompom.png')
        st.image(image, caption='Pompom', width = 200)
    elif select_villagers == 'Poncho':
        image = Image.open('poncho.jpg')
        st.image(image, caption='Poncho', width = 200)
    elif select_villagers == 'Poppy':
        image = Image.open('poppy.jpg')
        st.image(image, caption='Poppy', width = 200)
    elif select_villagers == 'Portia':
        image = Image.open('portia.png')
        st.image(image, caption='Portia', width = 200)
    elif select_villagers == 'Prince':
        image = Image.open('prince.png')
        st.image(image, caption='Prince', width = 200)
    elif select_villagers == 'Puck':
        image = Image.open('puck.png')
        st.image(image, caption='Puck', width = 200)
    elif select_villagers == 'Puddles':
        image = Image.open('puddles.png')
        st.image(image, caption='Puddles', width = 200)
    elif select_villagers == 'Pudge':
        image = Image.open('pudge.jpg')
        st.image(image, caption='Pudge', width = 200)
    elif select_villagers == 'Punchy':
        image = Image.open('punchy.png')
        st.image(image, caption='Punchy', width = 200)
    elif select_villagers == 'Purrl':
        image = Image.open('purrl.jpg')
        st.image(image, caption='Purrl', width = 200)
    #-----------------------------------------
    #Q's
    elif select_villagers == 'Queenie':
        image = Image.open('queenie.png')
        st.image(image, caption='Queenie', width = 200)
    elif select_villagers == 'Quillson':
        image = Image.open('quillson.png')
        st.image(image, caption='Quillson', width = 200)
    #-------------------------------------------
    #R's
    elif select_villagers == 'Raddle':
        image = Image.open('raddle.png')
        st.image(image, caption='Raddle', width = 200)
    elif select_villagers == 'Rasher':
        image = Image.open('rasher.png')
        st.image(image, caption='Rasher', width = 200)
    elif select_villagers == 'Raymond':
        image = Image.open('raymond.jpg')
        st.image(image, caption='Raymond', width = 200)
    elif select_villagers == 'Renée':
        image = Image.open('renee.png')
        st.image(image, caption='Renee', width = 200)
    elif select_villagers == 'Reneigh':
        image = Image.open('reneigh.png')
        st.image(image, caption='Reneigh', width = 200)
    elif select_villagers == 'Rex':
        image = Image.open('rex.png')
        st.image(image, caption='Rex', width = 200)
    elif select_villagers == 'Rhonda':
        image = Image.open('rhonda.jpg')
        st.image(image, caption='Rhonda', width = 200)
    elif select_villagers == 'Ribbot':
        image = Image.open('ribbot.jpg')
        st.image(image, caption='Ribbot', width = 200)
    elif select_villagers == 'Ricky':
        image = Image.open('Ricky.jpg')
        st.image(image, caption='Ricky', width = 200)
    elif select_villagers == 'Rizzo':
        image = Image.open('rizzo.png')
        st.image(image, caption='Rizzo', width = 200)
    elif select_villagers == 'Roald':
        image = Image.open('roald.jpg')
        st.image(image, caption='Roald', width = 200)
    elif select_villagers == 'Robin':
        image = Image.open('robin.jpg')
        st.image(image, caption='Robin', width = 200)
    elif select_villagers == 'Rocco':
        image = Image.open('rocco.jpg')
        st.image(image, caption='Rocco', width = 200)
    elif select_villagers == 'Rocket':
        image = Image.open('rocket.png')
        st.image(image, caption='Rocket', width = 200)
    elif select_villagers == 'Rod':
        image = Image.open('Rod.png')
        st.image(image, caption='Rod', width = 200)
    elif select_villagers == 'Rodeo':
        image = Image.open('rodeo.png')
        st.image(image, caption='rodeo', width = 200)
    elif select_villagers == 'Rodney':
        image = Image.open('rodney.png')
        st.image(image, caption='Rodney', width = 200) 
    elif select_villagers == 'Rolf':
        image = Image.open('rolf.jpg')
        st.image(image, caption='Rolf', width = 200)
    elif select_villagers == 'Rooney':
        image = Image.open('rooney.png')
        st.image(image, caption='Rooney', width = 200)
    elif select_villagers == 'Rory':
        image = Image.open('rory.jpg')
        st.image(image, caption='Rory', width = 200)
    elif select_villagers == 'Roscoe':
        image = Image.open('roscoe.png')
        st.image(image, caption='Roscoe', width = 200)
    elif select_villagers == 'Rosie':
        image = Image.open('Rosie.png')
        st.image(image, caption='Rosie', width = 200)
    elif select_villagers == 'Rowan':
        image = Image.open('rowan.jpg')
        st.image(image, caption='Rowan', width = 200)
    elif select_villagers == 'Ruby':
        image = Image.open('ruby.png')
        st.image(image, caption='Ruby', width = 200)
    elif select_villagers == 'Rudy':
        image = Image.open('rudy.png')
        st.image(image, caption='Rudy', width = 200)
    #----------------------------------------------------
    #S's
    elif select_villagers == 'Sally':
        image = Image.open('sally.png')
        st.image(image, caption='Sally', width = 200)
    elif select_villagers == 'Samson':
        image = Image.open('samson.png')
        st.image(image, caption='Samson', width = 200)
    elif select_villagers == 'Sandy':
        image = Image.open('sandy.png')
        st.image(image, caption='Sandy', width = 200)
    elif select_villagers == 'Savannah':
        image = Image.open('Savannah.png')
        st.image(image, caption='Savannah', width = 200)
    elif select_villagers == 'Scoot':
        image = Image.open('scoot.png')
        st.image(image, caption='Scoot', width = 200)
    elif select_villagers == 'Shari':
        image = Image.open('shari.png')
        st.image(image, caption='Shari', width = 200)
    elif select_villagers == 'Sheldon':
        image = Image.open('sheldon.png')
        st.image(image, caption='Sheldon', width = 200)
    elif select_villagers == 'Shep':
        image = Image.open('shep.jpg')
        st.image(image, caption='Shep', width = 200)
    elif select_villagers == 'Sherb':
        image = Image.open('sherb.png')
        st.image(image, caption='Sherb', width = 200)
    elif select_villagers == 'Simon':
        image = Image.open('simon.jpg')
        st.image(image, caption='Simon', width = 200)
    elif select_villagers == 'Skye':
        image = Image.open('skye.png')
        st.image(image, caption='Skye', width = 200)
    elif select_villagers == 'Sly':
        image = Image.open('sly.png')
        st.image(image, caption='Sly', width = 200)
    elif select_villagers == 'Snake':
        image = Image.open('snake.png')
        st.image(image, caption='snake', width = 200)
    elif select_villagers == 'Snooty':
        image = Image.open('snooty.png')
        st.image(image, caption='Snooty', width = 200)
    elif select_villagers == 'Soleil':
        image = Image.open('Soleil.png')
        st.image(image, caption='Soleil', width = 200)
    elif select_villagers == 'Sparro':
        image = Image.open('Sparro.jpg')
        st.image(image, caption='Sparro', width = 200)
    elif select_villagers == 'Spike':
        image = Image.open('spike.png')
        st.image(image, caption='Spike', width = 200)
    elif select_villagers == 'Spork':
        image = Image.open('spork.png')
        st.image(image, caption='spork', width = 200)
    elif select_villagers == 'Sprinkle':
        image = Image.open('sprinkle.png')
        st.image(image, caption='sprinkle', width = 200)
    elif select_villagers == 'Sprocket':
        image = Image.open('sprocket.png')
        st.image(image, caption='sprocket', width = 200)
    elif select_villagers == 'Static':
        image = Image.open('static.png')
        st.image(image, caption='Static', width = 200)
    elif select_villagers == 'Stella':
        image = Image.open('stella.png')
        st.image(image, caption='stella', width = 200)
    elif select_villagers == 'Sterling':
        image = Image.open('sterling.jpg')
        st.image(image, caption='sterling', width = 200)
    elif select_villagers == 'Stinky':
        image = Image.open('stinky.png')
        st.image(image, caption='Stinky', width = 200)
    elif select_villagers == 'Stitches':
        image = Image.open('stitches.png')
        st.image(image, caption='stitches', width = 200)
    elif select_villagers == 'Stu':
        image = Image.open('stu.png')
        st.image(image, caption='Stu', width = 200)
    elif select_villagers == 'Sydney':
        image = Image.open('sydney.png')
        st.image(image, caption='Sydney', width = 200)
    elif select_villagers == 'Sylvia':
        image = Image.open('sylvia.jpg')
        st.image(image, caption='Sylvia', width = 200)
    elif select_villagers == 'Sylvana':
        image = Image.open('sylvana.png')
        st.image(image, caption='Sylvana', width = 200)
    #---------------------------------------------------------
    #T's
    elif select_villagers == 'Tabby':
        image = Image.open('tabby.png')
        st.image(image, caption='Tabby', width = 200)
    elif select_villagers == 'Tad':
        image = Image.open('tad.png')
        st.image(image, caption='Tad', width = 200)
    elif select_villagers == 'Tammi':
        image = Image.open('tammi.png')
        st.image(image, caption='Tammi', width = 200)
    elif select_villagers == 'Tammy':
        image = Image.open('tammy.jpg')
        st.image(image, caption='Tammy', width = 200)
    elif select_villagers == 'Tangy':
        image = Image.open('tangy.jpg')
        st.image(image, caption='Tangy', width = 200)
    elif select_villagers == 'Tank':
        image = Image.open('tank.png')
        st.image(image, caption='Tank', width = 200)
    elif select_villagers == 'Tasha':
        image = Image.open('tasha.png')
        st.image(image, caption='Tasha', width = 200)
    elif select_villagers == 'T-Bone':
        image = Image.open('tbone.png')
        st.image(image, caption='Tbone', width = 200)
    elif select_villagers == 'Teddy':
        image = Image.open('teddy.jpg')
        st.image(image, caption='Teddy', width = 200)
    elif select_villagers == 'Tex':
        image = Image.open('tex.jpg')
        st.image(image, caption='Tex', width = 200)
    elif select_villagers == 'Tia':
        image = Image.open('tia.png')
        st.image(image, caption='Tia', width = 200)
    elif select_villagers == 'Tiffany':
        image = Image.open('tiffany.png')
        st.image(image, caption='Tiffany', width = 200)
    elif select_villagers == 'Timbra':
        image = Image.open('timbra.png')
        st.image(image, caption='Timbra', width = 200)
    elif select_villagers == 'Tipper':
        image = Image.open('tipper.png')
        st.image(image, caption='tipper', width = 200)
    elif select_villagers == 'Tom':
        image = Image.open('tom.png')
        st.image(image, caption='Tom', width = 200)
    elif select_villagers == 'Truffles':
        image = Image.open('truffles.jpg')
        st.image(image, caption='truffles', width = 200)
    elif select_villagers == 'Tucker':
        image = Image.open('tucker.png')
        st.image(image, caption='Tucker', width = 200)
    elif select_villagers == 'Tutu':
        image = Image.open('tutu.png')
        st.image(image, caption='Tutu', width = 200)
    elif select_villagers == 'Twiggy':
        image = Image.open('twiggy.jpg')
        st.image(image, caption='Twiggy', width = 200)
    elif select_villagers == 'Tybalt':
        image = Image.open('tybalt.png')
        st.image(image, caption='Tybalt', width = 200)
    #-------------------------------------------------
    #U's
    elif select_villagers == 'Ursala':
        image = Image.open('ursala.png')
        st.image(image, caption='Ursala', width = 200)
    #--------------------------------------------------
    #V's
    elif select_villagers == 'Velma':
        image = Image.open('velma.png')
        st.image(image, caption='Velma', width = 200)
    elif select_villagers == 'Vesta':
        image = Image.open('vesta.jpg')
        st.image(image, caption='Vesta', width = 200)
    elif select_villagers == 'Vic':
        image = Image.open('vic.png')
        st.image(image, caption='Vic', width = 200)
    elif select_villagers == 'Victoria':
        image = Image.open('victoria.jpg')
        st.image(image, caption='Victoria', width = 200)
    elif select_villagers == 'Violet':
        image = Image.open('violet.png')
        st.image(image, caption='Violet', width = 200)
    elif select_villagers == 'Vivian':
        image = Image.open('vivian.png')
        st.image(image, caption='Vivian', width = 200)
    elif select_villagers == 'Vladimir':
        image = Image.open('vladmir.jpg')
        st.image(image, caption='Vladimir', width = 200)
    #---------------------------------------------------
    #W's
    elif select_villagers == 'Wade':
        image = Image.open('wade.png')
        st.image(image, caption='Wade', width = 200)
    elif select_villagers == 'Walker':
        image = Image.open('walker.png')
        st.image(image, caption='Walker', width = 200)
    elif select_villagers == 'Walt':
        image = Image.open('walt.jpg')
        st.image(image, caption='Walt', width = 200)
    elif select_villagers == 'Wart Jr.':
        image = Image.open('wartjr.png')
        st.image(image, caption='WartJr', width = 200)
    elif select_villagers == 'Weber':
        image = Image.open('weber.png')
        st.image(image, caption='Weber', width = 200)
    elif select_villagers == 'Wendy':
        image = Image.open('wendy.png')
        st.image(image, caption='Wendy', width = 200)
    elif select_villagers == 'Whitney':
        image = Image.open('whitney.jpg')
        st.image(image, caption='Whitney', width = 200)
    elif select_villagers == 'Willow':
        image = Image.open('willow.png')
        st.image(image, caption='Willow', width = 200)
    elif select_villagers == 'Winnie':
        image = Image.open('winnie.png')
        st.image(image, caption='Winnie', width = 200)
    elif select_villagers == 'Wolfgang':
        image = Image.open('wolfgang.jpg')
        st.image(image, caption='Wolfgang', width = 200)
    #------------------------------------------------------
    #Y's
    elif select_villagers == 'Yuka':
        image = Image.open('yuka.png')
        st.image(image, caption='Yuka', width = 200)
    #----------------------------------------------------
    #Z's
    elif select_villagers == 'Zell':
        image = Image.open('zell.png')
        st.image(image, caption='Zell', width = 200)
    elif select_villagers == 'Zucker':
        image = Image.open('zucker.jpg')
        st.image(image, caption='Zucker', width = 200)






    
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
     #audio
    audio_file = open('AC_Theme.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_file, format = 'audio/mp3', start_time = 0)
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
    #audio_file = open('AC_Theme.mp3', 'rb')
    #audio_bytes = audio_file.read()
    #st.audio(audio_file, format = 'audio/mp3', start_time = 0)
