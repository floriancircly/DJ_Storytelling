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

scores_vergleich = [6707,  12920,  20577,  955900,  2699700]
zip_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
zip_df["hash_mode"] = "7-Zip"

scores_vergleich = [13944,  20945,  26544,  96662,  184000]
SHA_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
SHA_df["hash_mode"] = "bcrypt"

scores_vergleich = [33066000000,  58138500000,  73602400000,  121200000000,  288500000000]
third_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
third_df["hash_mode"] = "NTLM"

scores_vergleich = [4404800000, 114781000000, 159246000000, 227576000000, 506387000000]
fourth_df = pd.DataFrame(list(zip(gpu, scores_vergleich)), columns = ['GPU', 'speed (H/s)'])
fourth_df["hash_mode"] = "SHA-1"

data_vergleich = pd.concat([zip_df, SHA_df, third_df, fourth_df], ignore_index=True)
data_vergleich_personal = pd.concat([zip_df, SHA_df, third_df, fourth_df], ignore_index=True)

##########################################################################################################################

# Artikel

text = markdown.markdown('''

# 48 Minuten bis zum Identitätsdiebstahl
### Identitäten sind heutezutage eng mit der digitalen Welt verbunden. Unsere Passwörter schützen sie vor unerwünschtem Zugriff, aber wie sicher sind sie?
Von Andreas Braun, René Langschwert & Florian Voglauer

Im Verlauf der letzten Jahre ist der Zeitaufwand, ein Passwort zu hacken, deutlich gesunken. Grund dafür sind die immer stärkeren Grafikkarten, die es ermöglichen,
Passwörter in kürzester Zeit zu knacken. Diese Performancesteigerung sorgt nicht nur bei Spielen für flüssigere Framerates und immer höhere Auflösungen, sondern hat auch gravierende Auswirkungen auf die Sicherheit von Passwörtern und damit auch auf die Sicherheit von gesamten Identitäten.

In diesem Artikel wird gezeigt, wie sehr sich die Annahme eines “sicheren” Passwortes in den letzten Jahren verschoben hat. Hierbei werden die unterschiedlichen Grafikkarten-Generationen der letzten Jahre verglichen, um zu verdeutlichen, wie sehr der Zeitaufwand, um ein Passwort zu hacken, geschrumpft ist.

In den letzten zehn Jahren ist die Leistung von Grafikkarten rapide angestiegen. Nachstehend zu sehen sind die Performance-Scores der letzten fünf High-End Grafikkarten von Nvidia.

''')

st.markdown(text, unsafe_allow_html=True)

# Show plot
fig = px.bar(gpu_scores, x="GPU", y="scores", title='Benchmark Scores unterschiedlicher GPU Modelle',
    labels={
    "GPU": "GPU Modell",
    "scores": "Gaming Benchmark Score"})
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
fig = px.bar(zip_scores, x="GPU", y="Hashes (H/s)", title="Hashes pro Sekunde verschiedener GPU Modelle (Passwortgeschütztes 7-Zip Archiv)",
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
    ("7-Zip", "bcrypt", "NTLM", "SHA-1"),key="first")

zahlen = 10
buchstaben_groß = 26 
buchstaben_klein = 26
sonderzeichen = 32
alles = zahlen + buchstaben_groß + buchstaben_klein + sonderzeichen

laenge7 = 7
laenge8 = 8
laenge9 = 9
laenge10 = 10
laenge11 = 11
laenge12 = 12
laenge15 = 15
laenge20 = 20
kombinationen7 = alles**laenge7
kombinationen8 = alles**laenge8
kombinationen9 = alles**laenge9
kombinationen10 = alles**laenge10
kombinationen11 = alles**laenge11
kombinationen12 = alles**laenge12
kombinationen15 = alles**laenge15
kombinationen20 = alles**laenge20

minuten = 60
stunden = 60
tage = 24
anzahl_gpus = 8

data_vergleich = data_vergleich[data_vergleich["hash_mode"]==algorithmus]

####test
def timerequired(kombinationen, gpu, anzahl_gpus):
    my_time = kombinationen / data_vergleich[data_vergleich["GPU"]==gpu]["speed (H/s)"].item() / anzahl_gpus
    my_day = my_time // (24 * 3600)
    my_time = my_time % (24 * 3600)
    my_hour = my_time // 3600
    my_time %= 3600
    my_minutes = my_time // 60
    my_time %= 60
    my_seconds = my_time
    #mystring = str(my_day) + ":" + str(my_hour) + ":" + str(my_minutes) + ":" + str(my_seconds)
    mystring = str("%d:%d:%d:%d" % (my_day, my_hour, my_minutes, my_seconds))
    return mystring

def pretty_time(kombinationen, gpu, anzahl_gpus):
    time_str = timerequired(kombinationen, gpu, anzahl_gpus)
    time_list = time_str.split(':')
    
    days, hours, minutes, seconds = [int(x) for x in time_list] 
    weeks = days // 7
    months = days // 30
    years = days // 365
    txt_years = "{:,} yrs"
    txt_months = "{:,} mths"
    txt_weeks = "{:,} wk"
    txt_days = "{:,} days"
    txt_hours = "{:,} hrs"
    txt_minutes = "{:,} min"
    txt_seconds = "{:,} sec"
    if years:
        return txt_years.format(years)
    if months:
        return txt_months.format(months)
    if weeks:
        return txt_weeks.format(weeks)
    if days:
        return txt_days.format(days)
    if hours:
        return txt_hours.format(hours)
    if minutes:
        return txt_minutes.format(minutes)
    return txt_seconds.format(seconds)
   



# 'GTX980ti (2015)'
dauer_stunden_7_2015 = np.log(kombinationen7 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_8_2015 = np.log(kombinationen8 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_9_2015 = np.log(kombinationen9 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_10_2015 = np.log(kombinationen10 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_11_2015 = np.log(kombinationen11 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_12_2015 = np.log(kombinationen12 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_15_2015 = np.log(kombinationen15 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_20_2015 = np.log(kombinationen20 / data_vergleich[data_vergleich["GPU"]=='GTX980ti (2015)']["speed (H/s)"].item()  / anzahl_gpus)

# 'GTX1080ti (2017)'
dauer_stunden_7_2017 = np.log(kombinationen7 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_8_2017 = np.log(kombinationen8 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_9_2017 = np.log(kombinationen9 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_10_2017 = np.log(kombinationen10 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_11_2017 = np.log(kombinationen11 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_12_2017 = np.log(kombinationen12 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_15_2017 = np.log(kombinationen15 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_20_2017 = np.log(kombinationen20 / data_vergleich[data_vergleich["GPU"]=='GTX1080ti (2017)']["speed (H/s)"].item()  / anzahl_gpus)

# 'RTX2080ti (2018)'
dauer_stunden_7_2018 = np.log(kombinationen7 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_8_2018 = np.log(kombinationen8 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_9_2018 = np.log(kombinationen9 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_10_2018 = np.log(kombinationen10 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_11_2018 = np.log(kombinationen11 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_12_2018 = np.log(kombinationen12 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_15_2018 = np.log(kombinationen15 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_20_2018 = np.log(kombinationen20 / data_vergleich[data_vergleich["GPU"]=='RTX2080ti (2018)']["speed (H/s)"].item()  / anzahl_gpus)

# 'RTX3090 (2020)'
dauer_stunden_7_2020 = np.log(kombinationen7 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_8_2020 = np.log(kombinationen8 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_9_2020 = np.log(kombinationen9 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_10_2020 = np.log(kombinationen10 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_11_2020 = np.log(kombinationen11 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_12_2020 = np.log(kombinationen12 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_15_2020 = np.log(kombinationen15 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_20_2020 = np.log(kombinationen20 / data_vergleich[data_vergleich["GPU"]=='RTX3090 (2020)']["speed (H/s)"].item()  / anzahl_gpus)

# 'RTX4090 (2022)'
dauer_stunden_7_2022 = np.log(kombinationen7 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_8_2022 = np.log(kombinationen8 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_9_2022 = np.log(kombinationen9 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_10_2022 = np.log(kombinationen10 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_11_2022 = np.log(kombinationen11 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_12_2022 = np.log(kombinationen12 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_15_2022 = np.log(kombinationen15 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)
dauer_stunden_20_2022 = np.log(kombinationen20 / data_vergleich[data_vergleich["GPU"]=='RTX4090 (2022)']["speed (H/s)"].item()  / anzahl_gpus)


z = [
    [dauer_stunden_7_2022, dauer_stunden_8_2022, dauer_stunden_9_2022, dauer_stunden_10_2022,dauer_stunden_11_2022,dauer_stunden_12_2022,dauer_stunden_15_2022,dauer_stunden_20_2022],
    [dauer_stunden_7_2020, dauer_stunden_8_2020, dauer_stunden_9_2020, dauer_stunden_10_2020,dauer_stunden_11_2020,dauer_stunden_12_2020,dauer_stunden_15_2020,dauer_stunden_20_2020],
    [dauer_stunden_7_2018, dauer_stunden_8_2018, dauer_stunden_9_2018, dauer_stunden_10_2018,dauer_stunden_11_2018,dauer_stunden_12_2018,dauer_stunden_15_2018,dauer_stunden_20_2018],
    [dauer_stunden_7_2017, dauer_stunden_8_2017, dauer_stunden_9_2017, dauer_stunden_10_2017,dauer_stunden_11_2017,dauer_stunden_12_2017,dauer_stunden_15_2017,dauer_stunden_20_2017],
    [dauer_stunden_7_2015, dauer_stunden_8_2015, dauer_stunden_9_2015, dauer_stunden_10_2015,dauer_stunden_11_2015,dauer_stunden_12_2015,dauer_stunden_15_2015,dauer_stunden_20_2015]
    ]

x = ['7 Z.', '8 Z.', '9 Z.', '10 Z.','11 Z.', '12 Z.','15 Z.','20 Z.']
y = ['RTX4090 (2022)','RTX3090 (2020)','RTX2080ti (2018)', 'GTX1080ti (2017)','GTX980ti (2015)'] 

z_notation =    [
                [pretty_time(kombinationen7, "RTX4090 (2022)", anzahl_gpus),pretty_time(kombinationen8, "RTX4090 (2022)", anzahl_gpus), pretty_time(kombinationen9, "RTX4090 (2022)", anzahl_gpus), pretty_time(kombinationen10, "RTX4090 (2022)", anzahl_gpus),pretty_time(kombinationen11, "RTX4090 (2022)", anzahl_gpus),pretty_time(kombinationen12, "RTX4090 (2022)", anzahl_gpus),pretty_time(kombinationen15, "RTX4090 (2022)", anzahl_gpus),pretty_time(kombinationen20, "RTX4090 (2022)", anzahl_gpus)],
                [pretty_time(kombinationen7, "RTX3090 (2020)", anzahl_gpus),pretty_time(kombinationen8, "RTX3090 (2020)", anzahl_gpus), pretty_time(kombinationen9, "RTX3090 (2020)", anzahl_gpus), pretty_time(kombinationen10, "RTX3090 (2020)", anzahl_gpus),pretty_time(kombinationen11, "RTX3090 (2020)", anzahl_gpus),pretty_time(kombinationen12, "RTX3090 (2020)", anzahl_gpus),pretty_time(kombinationen15, "RTX3090 (2020)", anzahl_gpus),pretty_time(kombinationen20, "RTX3090 (2020)", anzahl_gpus)],
                [pretty_time(kombinationen7, "RTX2080ti (2018)", anzahl_gpus),pretty_time(kombinationen8, "RTX2080ti (2018)", anzahl_gpus), pretty_time(kombinationen9, "RTX2080ti (2018)", anzahl_gpus), pretty_time(kombinationen10, "RTX2080ti (2018)", anzahl_gpus),pretty_time(kombinationen11, "RTX2080ti (2018)", anzahl_gpus),pretty_time(kombinationen12, "RTX2080ti (2018)", anzahl_gpus),pretty_time(kombinationen15, "RTX2080ti (2018)", anzahl_gpus),pretty_time(kombinationen20, "RTX2080ti (2018)", anzahl_gpus)],
                [pretty_time(kombinationen7, "GTX1080ti (2017)", anzahl_gpus),pretty_time(kombinationen8, "GTX1080ti (2017)", anzahl_gpus), pretty_time(kombinationen9, "GTX1080ti (2017)", anzahl_gpus), pretty_time(kombinationen10, "GTX1080ti (2017)", anzahl_gpus),pretty_time(kombinationen11, "GTX1080ti (2017)", anzahl_gpus),pretty_time(kombinationen12, "GTX1080ti (2017)", anzahl_gpus),pretty_time(kombinationen15, "GTX1080ti (2017)", anzahl_gpus),pretty_time(kombinationen20, "GTX1080ti (2017)", anzahl_gpus)],
                [pretty_time(kombinationen7, "GTX980ti (2015)", anzahl_gpus), pretty_time(kombinationen8, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen9, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen10, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen11, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen12, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen15, "GTX980ti (2015)", anzahl_gpus),pretty_time(kombinationen20, "GTX980ti (2015)", anzahl_gpus)]
                ]


fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_notation,colorscale='RdBu') # YlGnBu
fig.update_traces(hoverinfo='skip')
fig.update_layout(title=f"""Vergleich der Dauer, um ein Passwort mit unterschiedlicher länge zu hacken \n (Worst Case)""",width=1500)
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
Dabei gilt es zu beachten, dass hier die "Worst Case Szenario" Berechnung durchgeführt wurde. Das heißt, dass innerhalb der angegebenen Zeit, alle Kombinationen durchprobiert werden.
Es könnte daher auch schon viel früher passieren, dass das gesuchte Passwort gefunden wird. Zudem basiert die Rechnung auf Passwörtern, die bereits Klein- und Großbuchstaben sowie Zahlen und Sonderzeichen enthalten.
Um die Berechnungszeiten individuell darzustellen, können im nachfolgenden Absatz die entsprechenden Werte angepasst werden.

''')
st.markdown(text, unsafe_allow_html=True)

options = st.multiselect(
    'Passwort enthält:',
    ["Sonderzeichen","Zahlen", "Kleinbuchstaben", "Großbuchstaben"],default="Kleinbuchstaben")

number = st.number_input('Länge des Passworts:',step=1, min_value = 3, max_value = 20)

algorithmus = st.radio(
    "Wähle einen Hash-Algorithmus aus",
    ("7-Zip", "bcrypt", "NTLM", "SHA-1"),key="second")

zahlen = 10 if "Zahlen" in options else 0
buchstaben_groß = 26 if "Großbuchstaben" in options else 0
buchstaben_klein = 26 if "Kleinbuchstaben" in options else 0
sonderzeichen = 32 if "Sonderzeichen" in options else 0

alles = zahlen + buchstaben_groß + buchstaben_klein + sonderzeichen

laenge = number
kombinationen = alles**laenge

data_vergleich_personal = data_vergleich_personal[(data_vergleich_personal["GPU"]=="RTX4090 (2022)") & (data_vergleich_personal["hash_mode"]==algorithmus)]

#anzahl_gpus = 8
anzahl_gpus = st.slider('Anzhal der Grafikkarten', 1, 10, 8)

dauer_tag = kombinationen / data_vergleich_personal["speed (H/s)"].item() / minuten / stunden / tage / anzahl_gpus # WARUM ACHT ERKLÄREN
dauer_stund = kombinationen / data_vergleich_personal["speed (H/s)"].item() / minuten / stunden / anzahl_gpus # WARUM ACHT ERKLÄREN
dauer_min = kombinationen / data_vergleich_personal["speed (H/s)"].item() / minuten / anzahl_gpus # WARUM ACHT ERKLÄREN
st.write("Benötigte Tage: ", np.round(dauer_tag,2))
st.write("Benötigte Stunden: ", np.round(dauer_stund,2))
st.write("Benötigte Minuten: ", np.round(dauer_min,2))

my_time = kombinationen / data_vergleich_personal["speed (H/s)"].item() / anzahl_gpus
my_year = my_time // (24 * 3600 * 365)
my_day = my_time // (24 * 3600)
my_time = my_time % (24 * 3600)
my_hour = my_time // 3600
my_time %= 3600
my_minutes = my_time // 60
my_time %= 60
my_seconds = my_time
st.write("Tage:Stunden:Minuten:Sekunden: %d:%d:%d:%d:%d" % (my_year, my_day, my_hour, my_minutes, my_seconds))


text = markdown.markdown('''
</br>
Dieser individuelle Rechner soll nochmals verdeutlichen, wie sehr zusätzliche Zeichen das Hacken eines Passworts erschweren.

Doch wie sehr betrifft dieser Vorgang überhaupt eine individuelle Person? Leider lässt sich ein Hackangriff nicht darauf beschränken, dass nur eine
bestimmte Person Ziel einer Attacke ist. Mittlerweile hat sich ein regelrechter Markt etabliert, hinter dem ein riesiges Businessmodell steht. Unzählige Hashes und deren 
daraus resultierende Zeichenketten stehen schon vorberechnet zur Verfügung (zum Beispiel von den häufigst benützten Passwörtern), um den Hackvorgang nochmal deutlich
schneller zu gestalten. Vor allem die Einfachheit ist hier hervorzuheben, da Tools wie Hashcat für jedermann zu benutzten sind.
-- QUELLE?! ---

#### Fazit
Abschließend lässt sich sagen, dass die Ausgangsthese "Im Verlauf der letzten Jahre ist es um einiges einfacher geworden, ein Passwort mit beispielsweise 8 Zeichen zu hacken", bestätigt wurde. 
Die Grafikkarten-Generationen haben sich in den letzten Jahren stark verbessert. Die Datenanalyse des Artikels unterstreicht diese drastische Entwicklung. Es ist daher stark zu empfehlen, darauf zu achten, dass
benutzte Passwörter Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten und zumindest 12 Stellen lang sind. Beispielsweise Telefonnummern sind kein gutes Beispiel für Passwörter.

---

#### Expert:innen-Leitfaden
* 5-8 Fragen und Antworten zu den Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management. 
    * Welche konkreten Maßnahmen können Enduser ergreifen, um ihre Daten bzw. Identität vor Diebstahl zu schützen?
    * Worauf gilt es neben einem möglich großen Zeichenraumes bei der Passwortwahl noch zu achten?
    * Was macht einen Hash-Algorithmus sicher und worin unterscheiden sie sich grundlegend?
    * Worauf sollten Enduser als auch Entwickler achten und wie können Passwörter sicher gespeichert werden?
    * Können Enduser überhaupt feststellen, ob die Applikation oder Service den sie nutzen Wert auf ihre Passwort Sicherheit legen?
    * Aus verschiedenen Ecken des Internets ist immer wieder zu hören dass Serviceprovider oder Regierungen sogenannte Backdoors zu diesen Alorithmen besitzen, wieivel ist an solchen Aussagen dran bzw. ist das überhaupt möglich?
    * 
    * Wie sehen Sie die zukünftige Entwicklung der Passwortsicherheit?

* Warum haben wir genau diesen Experten ausgewählt? </br></br>
Der Experte ist IT-Sicherheitsexperte und hat sich auf die Themen Passwortsicherheit, Identitätsdiebstahl und Passwort-Management spezialisiert.
Zudem forscht er an der Universität Wien an der IT-Security Fakultät und ist dort als Dozent tätig.
Daher ist er der richtige Ansprechpartner für die Fragen, die im Expert:innen-Leitfaden gestellt wurden.

#### Was habt ihr aus der Story gelernt?
Hervorzuheben ist hier auf jeden Fall, dass sich die Definition von "sicheren Passwörtern" in den letzten Jahren stark geändert hat. Vor allem der 
Einsatz von Sonderzeichen und Zahlen also die Erweiterung des Suchraums ist ein wichtiger Punkt, der nochmal in der Story verdeutlicht wird.
Interessant war vor allem auch wie einfach es ist an die nötigen Informationen zu kommen z.B. um ein passwortgeschützes ZIP File zu öffnen.


---

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

##########################################################################################################################

