import matplotlib.pyplot as plt
import streamlit as st
import main
import pandas as pd



#Affichage du graphique de fréquantation par ligne


df = main.Data2()
fig = plt.figure(figsize=(25, 10))
plt.bar(df['Ligne'], df['Total_Passagers'])
plt.xlabel('Lignes de bus')
plt.ylabel('Nombre de passagers')
plt.title('Fréquentation par ligne de bus')
st.pyplot(fig)


#Affichage du graphique de fréquention par heure


df = main.Data3()
fig, ax = plt.subplots(figsize=(20, 6))
# Création du graphique de ligne
for ligne in df['ligne'].unique():
    ligne_df = df[df['ligne'] == ligne]
    ax.plot(ligne_df['heure'], ligne_df['passagers'], label=ligne)
ax.set_xlabel('Heure')
ax.set_ylabel('Fréquentation')
ax.set_title('Fréquentation des différentes lignes de bus par heure')
ax.legend()
# Affichage du graphique dans Streamlit
st.pyplot(fig)

#Affichage du camember de Fréquentation par Jour

df = main.Data4()
plt.figure(figsize=(6,5),dpi=80)

#Conversion de la valeur passagers qui est un string en float(pourquoi ?)

df["Total_Passagers"] = df["Total_Passagers"].astype(float)
fig, ax = plt.subplots()
ax.pie(df["Total_Passagers"], labels=df["Jour"], autopct='%1.1f%%')
ax.set_title('Fréquentation par jours')
st.pyplot(fig)
