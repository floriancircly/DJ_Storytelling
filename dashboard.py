import streamlit as st
import pandas as pd
import numpy as np
import markdown
import plotly.express as px
from PIL import Image
import plotly.figure_factory as ff

##########################################################################################################################

# Daten

data = pd.read_csv("Data/all_devices.csv", sep=",")
gpu = ['GTX980ti (2015)', 'GTX1080ti (2017)', 'RTX2080ti (2018)', 'RTX3090 (2020)', 'RTX4090 (2022)']
scores = [4981,  9421,  14621,  19977,  36529]
zip_hash =  [6212,12920,20577,955900,2699700]
gpu_scores = pd.DataFrame(list(zip(gpu, scores)), columns = ['GPU', 'scores'])
zip_scores = pd.DataFrame(list(zip(gpu, zip_hash)), columns = ['GPU', 'Hashes (H/s)'])
image = Image.open('Data/pass.png')

z = [[.1, .3, .4, .7],
    [.2, .4, .5, .8],
    [.3, .5, .6, .9]]

z_text = [[.1, .3, .4, .7],
    [.2, .4, .5, .8],
    [.3, .5, .6, .9]]

x = ['Passwortlänge (5 Z.)', 'Passwortlänge (8 Z.)','Passwortlänge (10 Z.)','Passwortlänge (14 Z.)']
y = ['GTX980ti (2015)', 'GTX1080ti (2017)', 'RTX2080ti (2018)']

scores_vergleich = [6707,  12920,  20577,  955900,  2699700]
zip_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
zip_df["hash_mode"] = "7-Zip"

scores_vergleich = [13944,  20945,  26544,  96662,  184000]
SHA_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
SHA_df["hash_mode"] = "bcrypt"

scores_vergleich = [33066000000,  58138500000,  73602400000,  121200000000,  288500000000]
third_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
third_df["hash_mode"] = "NTLM"

data_vergleich = pd.concat([zip_df, SHA_df, third_df], ignore_index=True)

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
Zunächst liest dieser den Hash der Ziel-Datei aus. In diesem steht nun der Hash als auch mit welchem Hash-Algorithmus die Datei geschützt ist. Unterschiedliche
Anwendungen verwenden auch unterschiedliche Hash-Algorithmen, also andere Methoden, um das Passwort in eine bedeutungslose Zeichenkette umzuwandeln. 
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
                                        text="Quelle: Hashcat Berechnung",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

st.plotly_chart(fig, use_container_width=True)

text = markdown.markdown('''
</br>
Hier wird deutlich, dass nun eine enorme Anzahl an Passwörtern pro Sekunde ausprobiert werden kann. War es vor zehn Jahren noch vollkommen ausreichend, ein acht Zeichen 
langes Passwort mit Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen zu verwenden, so könnte dieses Passwort mit der neuesten Hardware - 
abhängig vom Hash-Algorithmus - in unter einer Stunde geknackt werden. Laut einer <a href='https://www-statista-com.ezproxy.fhstp.ac.at:2443/statistics/744216/worldwide-distribution-of-password-length/'>Erhebung</a> sind über 50% der Passwörter genau oder unter 8 Zeichen lang und 
daher gefährdet.

In der nachstehenden Grafik ist es möglich, für unterschiedliche Hash-Algorithmen die Dauer bis zum Knacken von Passwörtern mit verschiedenen Längen zu analysieren.

''')

st.markdown(text, unsafe_allow_html=True)

algorithmus = st.radio(
    "Wähle einen Hash-Algorithmus aus",
    ('7-Zip', 'Skype', 'Word'))


fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text,colorscale='Cividis')
fig.update_layout(title="Vergleich unterschiedlicher Passwortlänge (Worst Case Szenario)")
fig.add_annotation(dict(font=dict(color='black',size=10),
                                        x=0,
                                        y=-0.30,
                                        showarrow=False,
                                        text="Quelle: Hashcat Berechnung",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))
st.plotly_chart(fig, use_container_width=True)

text = markdown.markdown('''
</br>
Dabei gilt es zu beachten, dass hier ein 

''')
st.markdown(text, unsafe_allow_html=True)


# Berechnung personalisierter Hack-Zeit
options = st.multiselect(
    'Passwort enthält:',
    ["Sonderzeichen","Zahlen", "Kleinbuchstaben", "Großbuchstaben"])

number = st.number_input('Länge des Passworts:',step=1, min_value = 3, max_value = 20)

algorithmus = st.radio(
    "Wähle einen Hash-Algorithmus aus",
    ("7-Zip", "bcrypt", "NTLM"),key="second")

zahlen = 10 if "Zahlen" in options else 0
buchstaben_groß = 26 if "Großbuchstaben" in options else 0
buchstaben_klein = 26 if "Kleinbuchstaben" in options else 0
sonderzeichen = 32 if "Sonderzeichen" in options else 0

alles = zahlen + buchstaben_groß + buchstaben_klein + sonderzeichen

laenge = number
kombinationen = alles**laenge

data_vergleich = data_vergleich[(data_vergleich["GPU"]=="RTX4090 (2022)") & (data_vergleich["hash_mode"]==algorithmus)]

minuten = 60
stunden = 60
tage = 24
#anzahl_gpus = 8
anzahl_gpus = st.slider('Anzhal der Grafikkarten', 1, 10, 8)

dauer_tag = kombinationen / data_vergleich["speed (H/s)"].item() / minuten / stunden / tage / anzahl_gpus # WARUM ACHT ERKLÄREN
dauer_stund = kombinationen / data_vergleich["speed (H/s)"].item() / minuten / stunden / anzahl_gpus # WARUM ACHT ERKLÄREN
dauer_min = kombinationen / data_vergleich["speed (H/s)"].item() / minuten / anzahl_gpus # WARUM ACHT ERKLÄREN
st.write("Benötigte Tage: ", np.round(dauer_tag,2))
st.write("Benötigte Stunden: ", np.round(dauer_stund,2))
st.write("Benötigte Minuten: ", np.round(dauer_min,2))

# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# st.write("Tage:Stunden:Minuten:Sekunden-> %d:%d:%d:%d" % (day, hour, minutes, seconds))



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
#st.balloons()
st.image("https://c.tenor.com/p0gHiSC-xecAAAAi/rainbow-dance-pepe-jam.gif")
st.video("https://www.youtube.com/watch?v=WNeLUngb-Xg")
