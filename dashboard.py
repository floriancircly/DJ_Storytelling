import streamlit as st
import pandas as pd
import numpy as np
import markdown
import plotly.express as px


##########################################################################################################################

# Daten

data = pd.read_csv("Data/GTX1080ti.csv", sep=",")

##########################################################################################################################

# Artikel

text = markdown.markdown('''

# 48 Minuten bis zum Identitätsdiebstahl
### Identitäten sind heute mit der digitalen Welt verbunden oder hängen sogar schon vollständig von ihr ab. Unsere Passwörter schützen sie vor unerwünschtem Zugriff, aber wie sicher sind sie? Über 30% der Accounts sind massiv gefährdet.
Von Andreas Braun, René Langschwert & Florian Voglauer
#### Überschrift 
* Auzählung
* Auzählung
* Auzählung
#### Überschrift 
Hallo das ist ein Beispieltext

''')
st.markdown(text, unsafe_allow_html=True)

# Show data
st.dataframe(data=data)

# Show plot
fig = px.line(data, x="id", y="loops", title='loop loop loop')
st.plotly_chart(fig, use_container_width=True)

##########################################################################################################################

# Extra

st.balloons()
st.image("https://c.tenor.com/p0gHiSC-xecAAAAi/rainbow-dance-pepe-jam.gif")
st.video("https://www.youtube.com/watch?v=WNeLUngb-Xg")
