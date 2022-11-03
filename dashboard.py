import streamlit as st
import pandas as pd
import numpy as np
import markdown
import plotly.express as px


##########################################################################################################################

# Daten

data = pd.read_csv("Data/all_devices.csv", sep=",")

##########################################################################################################################

# Artikel

text = markdown.markdown('''

# 48 Minuten bis zum Identitätsdiebstahl
### Identitäten sind heutezutage eng mit der digitalen Welt verbunden. Unsere Passwörter schützen sie vor unerwünschtem Zugriff, aber wie sicher sind sie?
Von Andreas Braun, René Langschwert & Florian Voglauer

#### Ausgangsthese
Im Verlauf der letzten Jahre ist es um einiges einfacher geworden, ein Passwort mit z.B. 8 Zeichen zu hacken. Grund dafür sind die immer stärkeren Grafikkarten, die es ermöglichen,
Passwörter in kürzester Zeit zu knacken. Diese Performancesteigerung hat gravierende Auswirkungen auf die Sicherheit von Passwörtern und damit auch auf die Sicherheit von gesamten Identitäten.
Ziel des Artikels ist es, die unterschiedlichen Grafikkarten-Generationen zu vergleichen, um zu verdeutlichen wie sehr die Zeit, um ein Passwort zu hacken, gesunken ist.

#### Textanalyse oder Reportage
Über 30% der Accounts sind massiv gefährdet.

#### Fazit, ob Ausgangsthese be- oder widerlegt wurde
Abschließend lässt sich sagen, dass die Ausgangsthese "Im Verlauf der letzten Jahre ist es um einiges einfacher geworden, ein Passwort mit z.B. 8 Zeichen zu hacken", bestätigt wurde. 
Die Grafikkarten-Generationen haben sich in den letzten Jahren stark verbessert die Datenanalyse des Artikel unterstreicht diese drastische Entwicklung.

#### Expert:innen-Leitfaden
5-8 Fragen und Antworten zu den Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management. </br>
* Welche konkreten Maßnahmen kann man selbst ergreifen, um seine Identität zu schützen?
* Wie können Passwörter sicher gespeichert werden?
* Wie sehen Sie die zukünftige Entwicklung der Passwortsicherheit?

</br>
Warum haben wir genau diesen Experten ausgewählt? </br>
Der Experte ist IT-Sicherheitsexperte und hat sich auf die Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management spezialisiert.
Zudem forscht er an der Universität Wien an der IT-Security Fakultät und ist dort als Dozent tätig.
Daher ist er der richtige Ansprechpartner für die Fragen, die im Expert:innen-Leitfaden gestellt wurden.

#### Was habt ihr aus der Story gelernt?

#### Beantwortung der W-Fragen
* Was ist die Geschichte?
Durch eine Hashcat-Attacke ist es möglich, Passwörter in kürzester Zeit zu knacken.

* Woher sind die Daten? </br>
Dieser Artikel analysiert Benchmarkwerte unterschiedlicher Hardware-Generationen einer “Recovery” Software für Passwörter:
Um die Berechnungszeit der Passwortsuche zu messen, wird das Tool “Hashcat” verwendet ( https://hashcat.net/hashcat/ ).

* Wann & Wie wurden die Daten erhoben?
Wann: November 2022 </br>
Wie: Durch Anwendung der Hashcat-Software auf verschiedene Hardware-Generationen

* Wo lassen sich Daten lokalisieren?
Online

* Warum ist etwas passiert?

#### Darstellung der Relevanz
Doch warum ist diese Thematik außer dem Identitätsdiebstahl noch relevant? Die Antwort ist wie so oft: Geld. Aud dem Gray/Dark Market steht ein großes Business dahinter, 
Email-Accounts zu hacken und anschließend den E-Mail-Verlauf zu tracken. Solche Emails werden oftmals verkauft inkl. z.B. Kreditkarten-Informationen. 
Dabei hervorzuheben ist wie einfach es ist damit zu beginnen Passwörter zu hacken. Mit ein bisschen Recherche ist es im Prinzip jedem etwas technik-affinen mit einem Computer möglich.

''')
st.markdown(text, unsafe_allow_html=True)

# Show data
st.dataframe(data=data)

# Show plot
fig = px.line(data, x="id", y="loops", title='loop loop loop', color='GPU')
st.plotly_chart(fig, use_container_width=True)

text = markdown.markdown('''

#### Notizen Visualisierungen
* Quellenangabe
* Deskriptiver Titel, Beschreibung, Annotations
* Passende Verknüpfung mit Text
Sinnvolle Stelle im Text, keine unerklärten Begriffe, die nicht im Text erwähnt werden

''')
st.markdown(text, unsafe_allow_html=True)

##########################################################################################################################

# Extra
st.balloons()
st.image("https://c.tenor.com/p0gHiSC-xecAAAAi/rainbow-dance-pepe-jam.gif")
st.video("https://www.youtube.com/watch?v=WNeLUngb-Xg")
