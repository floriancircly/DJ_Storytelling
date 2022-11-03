import streamlit as st
import pandas as pd
import numpy as np
import markdown
import plotly.express as px
from PIL import Image

##########################################################################################################################

# Daten

data = pd.read_csv("Data/all_devices.csv", sep=",")
gpu = ['GTX980ti (2015)', 'GTX1080ti (2017)', 'GTX2080ti (2018)', 'GTX3090 (2020)', 'GTX4090 (2022)']
scores = [4981,  9421,  14621,  19977,  36529]
zip_hash =  [6212,12920,20577,955900,2699700]
gpu_scores = pd.DataFrame(list(zip(gpu, scores)), columns = ['GPU', 'scores'])
zip_scores = pd.DataFrame(list(zip(gpu, zip_hash)), columns = ['GPU', 'Hashes (H/s)'])
image = Image.open('Data/pass.png')


##########################################################################################################################

# Artikel

text = markdown.markdown('''

# 48 Minuten bis zum Identitätsdiebstahl
### Identitäten sind heutezutage eng mit der digitalen Welt verbunden. Unsere Passwörter schützen sie vor unerwünschtem Zugriff, aber wie sicher sind sie?
Von Andreas Braun, René Langschwert & Florian Voglauer

#### Deskriptiver Einstieg in den Text mit den Punkten: Wer? Was? Was ist euer Thema/eure Fragestellung?

Im Verlauf der letzten Jahre ist der Zeitaufwand, ein Passwort zu hacken, deutlich gesunken. Grund dafür sind die immer stärkeren Grafikkarten, die es ermöglichen,
Passwörter in kürzester Zeit zu knacken. Diese Performancesteigerung sorgt nicht nur bei Spielen für flüssigere Framerates und immer höhere Auflösungen, sondern hat auch gravierende Auswirkungen auf die Sicherheit von Passwörtern und damit auch auf die Sicherheit von gesamten Identitäten.

In diesem Artikel wird gezeigt, wie sehr sich die Annahme eines “sicheren” Passwortes in den letzten Jahren verschoben hat. Hierbei werden die unterschiedlichen Grafikkarten-Generationen der letzten Jahre verglichen, um zu verdeutlichen, wie sehr der Zeitaufwand, um ein Passwort zu hacken, geschrumpft ist.

(Annahme: Es verfügt über Klein- und Großbuchstaben, Zahlen sowie Sonderzeichen)
mit beispielsweise 8 Zeichen

In die letzten zehn Jahren ist die Leistung von Grafikkarten rapide angestiegen. Nachstehend zu sehen sind die Performance-Scores der letzten fünf High-End Grafikkarten von Nvidia.

''')

st.markdown(text, unsafe_allow_html=True)

# Show plot
fig = px.bar(gpu_scores, x="GPU", y="scores", title='Benchmark Scores unterschiedlicher GPU Modelle',
    labels={
    "GPU": "GPU Modell",
    "scores": "Benchmark Score"})
fig.add_annotation(dict(font=dict(color='black',size=10),
                                        x=0,
                                        y=-0.30,
                                        showarrow=False,
                                        text="Quelle: <a href='https://www.pcgameshardware.de/3DMark-Software-122260/Specials/Punkte-Tabelle-Time-Spy-Benchmark-1357989/'>www.pcgameshardware.de</a>",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

st.plotly_chart(fig, use_container_width=True)

text = markdown.markdown('''

Dieser Fortschritt hat zur Folge, dass IT-Sicherheitsmaßnahmen schneller entschärft werden können. 
Ein alltäglicher Anwendungsfall wäre das Erzeugen eines passwortgeschützten Zip-Archives (7-Zip), bei dem die Dateien nicht nur komprimiert, 
sondern auch gegen ungewollten Zugriff gesichert werden. Bei diesem Vorgang wird das gewählte Passwort mithilfe einer mathematischen Funktion 
in eine Zeichenkette übersetzt, den sogenannten Hash. Diese Umwandlung ist essentiell, weil das Klartext-Passwort nicht auf dem 
System gespeichert werden sollte, da ansonsten ein potenzieller Angreifer das originale Passwort zur Verfügung hätte. </br>

Will ein Angreifer nun an ein Passwort gelangen wäre der Ablauf wie folgt: </br>
Zunächst liest dieser den Hash der Ziel-Datei aus. In diesem steht nun der Hash als auch mit welchem Hash-Algorithmus die Datei geschützt ist.
Anschließend kann der Angreifer aus einer Vielzahl an Angriffsmethoden wählen. Die simpelste ist hierbei ein "Brute-Force-Attack", bei dem alle möglichen Kombinationen aus Buchstaben, Zahlen und Zeichen ausprobiert werden. 
Der Angreifer probiert nun etliche Kombinationen aus und sieht sich dabei den Hash der Hashfunktion an und vergleicht diesen mit der zuvor 
erlangten Ziel-Datei. Stimmen beide überein, ist der Angreifer an das Passwort gelangt und hat somit Zugriff auf die Ziel-Datei. </br>
</br>
''')

st.markdown(text, unsafe_allow_html=True)
st.image(image, caption='Illustration eines Passwort-Angriffes')

text = markdown.markdown('''
</br>
Die Anzahl an Hashes, die pro Sekunde berechnet werden können, hat in den vergangenen Jahren in beeindruckender Manier zugenommen. Nachstehend angeführt sieht man die Hashes pro Sekunde, die die jeweiligen GPUs rechnen können.

''')

st.markdown(text, unsafe_allow_html=True)

# Show plot
fig = px.bar(zip_scores, x="GPU", y="Hashes (H/s)", title="Hashes pro Sekunde verschiedener GPU Modelle (7-Zip Algorithmus)",
    labels={
    "GPU": "GPU Modell",
    "Hashes (H/s)": "Hashes (H/s)"})
fig.add_annotation(dict(font=dict(color='black',size=10),
                                        x=0,
                                        y=-0.30,
                                        showarrow=False,
                                        text="Hier gehört noch was hin",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

st.plotly_chart(fig, use_container_width=True)

text = markdown.markdown('''
</br>
Hier wird deutlich, dass nun eine enorme Anzahl an Passwörtern pro Sekunde ausprobiert werden kann. War es vor zehn Jahren noch vollkommen ausreichend, 
ein acht Zeichen langes Passwort mit Groß- und Kleinbuchstaben, 
Zahlen und Sonderzeichen zu verwenden, so könnte dieses Passwort mit der neuesten Hardware in unter einer Stunde geknackt werden.

<a href='https://www-statista-com.ezproxy.fhstp.ac.at:2443/statistics/744216/worldwide-distribution-of-password-length/'>Tests</a>
''')

st.markdown(text, unsafe_allow_html=True)


text = markdown.markdown('''
#### Fazit, ob Ausgangsthese be- oder widerlegt wurde
Abschließend lässt sich sagen, dass die Ausgangsthese "Im Verlauf der letzten Jahre ist es um einiges einfacher geworden, ein Passwort mit z.B. 8 Zeichen zu hacken", bestätigt wurde. 
Die Grafikkarten-Generationen haben sich in den letzten Jahren stark verbessert. Die Datenanalyse des Artikel unterstreicht diese drastische Entwicklung.

---

#### Expert:innen-Leitfaden
* 5-8 Fragen und Antworten zu den Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management. 
    * Welche konkreten Maßnahmen kann man selbst ergreifen, um seine Identität zu schützen?
    * Wie können Passwörter sicher gespeichert werden?
    * Wie sehen Sie die zukünftige Entwicklung der Passwortsicherheit?

* Warum haben wir genau diesen Experten ausgewählt? </br>
Der Experte ist IT-Sicherheitsexperte und hat sich auf die Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management spezialisiert.
Zudem forscht er an der Universität Wien an der IT-Security Fakultät und ist dort als Dozent tätig.
Daher ist er der richtige Ansprechpartner für die Fragen, die im Expert:innen-Leitfaden gestellt wurden.

#### Was habt ihr aus der Story gelernt?

#### Beantwortung der W-Fragen 
* Was ist die Geschichte? </br>
Durch eine Hashcat-Attacke ist es möglich, Passwörter in kürzester Zeit zu knacken.

* Woher sind die Daten? </br>
Dieser Artikel analysiert Benchmarkwerte unterschiedlicher Hardware-Generationen einer “Recovery” Software für Passwörter:
Um die Berechnungszeit der Passwortsuche zu messen, wird das Tool “Hashcat” verwendet ( https://hashcat.net/hashcat/ ).

* Wann & Wie wurden die Daten erhoben? </br>
Wann: November 2022 </br>
Wie: Durch Anwendung der Hashcat-Software auf verschiedene Hardware-Generationen

* Wo lassen sich Daten lokalisieren? </br>
Online

* Warum ist etwas passiert?

''')
st.markdown(text, unsafe_allow_html=True)

# Show data
st.dataframe(data=data)

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
