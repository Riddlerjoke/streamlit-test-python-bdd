import mysql.connector as mybdd
import pandas as pd
import streamlit as st
from PIL import Image
from data import connection_bdd as dd


st.title('bienvenue cher utilisateur')

image = Image.open('Plan_bibus_2016-2017.png')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

print(dd.dataset1)


def Data1() :
    bdd = mybdd.connect(
    user = "root",
    password = "example",
    host = "localhost",
    port = "3307",
    database = "streamlit_breizhibus",)

    cursor = bdd.cursor()
    query = "SELECT horaires.heure, lignes.nom, arrets.libelle from horaires join lignes ON lignes.id= horaires.ligne join arrets ON horaires.arret= arrets.id"
    cursor.execute(query)
    results = cursor.fetchall()
    dataset1 = pd.DataFrame(results, columns=cursor.column_names)
    
    cursor.close()
    bdd.close()
    return dataset1


def Data2():
    bdd = mybdd.connect(
        user="root",
        password="example",
        host="localhost",
        port="3307",
        database="streamlit_breizhibus", )

    cursor = bdd.cursor()
    query = "SELECT lignes.nom AS Ligne, SUM(frequentation.nombre_passagers) AS Total_Passagers FROM frequentation INNER JOIN horaires ON frequentation.horaire = horaires.id INNER JOIN lignes ON horaires.ligne = lignes.id GROUP BY lignes.nom"
    cursor.execute(query)
    results = cursor.fetchall()
    dataset2 = pd.DataFrame(results, columns=cursor.column_names)

    cursor.close()
    bdd.close()
    return dataset2


def Data3():
    bdd = mybdd.connect(
        user="root",
        password="example",
        host="localhost",
        port="3307",
        database="streamlit_breizhibus", )

    cursor = bdd.cursor()
    query = "SELECT SUM(frequentation.nombre_passagers) AS passagers, horaires.heure, lignes.nom AS ligne FROM frequentation JOIN horaires ON frequentation.horaire = horaires.id JOIN lignes ON horaires.ligne = lignes.id GROUP BY horaires.heure, ligne"
    cursor.execute(query)
    results = cursor.fetchall()
    dataset3 = pd.DataFrame(results, columns=cursor.column_names)

    cursor.close()
    bdd.close()
    return dataset3


def Data4():
    bdd = mybdd.connect(
        user="root",
        password="example",
        host="localhost",
        port="3307",
        database="streamlit_breizhibus", )

    cursor = bdd.cursor()
    query = "SELECT frequentation.jour AS Jour, SUM(frequentation.nombre_passagers) AS Total_Passagers FROM frequentation GROUP BY frequentation.jour;"
    cursor.execute(query)
    results = cursor.fetchall()
    dataset4 = pd.DataFrame(results, columns=cursor.column_names)

    cursor.close()
    bdd.close()
    return dataset4