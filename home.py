import streamlit as st
import mysql.connector as mybdd
from PIL import Image
import pandas as pd


st.title('bienvenue cher utilisateur')

image = Image.open('Plan_bibus_2016-2017.png')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

dataset1 = pd.DataFrame()
dataset2 = pd.DataFrame()
dataset3 = pd.DataFrame()
dataset4 = pd.DataFrame()


def Data1():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "streamlit_breizhibus"

    global dataset1

    BDD = mybdd.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = BDD.cursor()
    query = "SELECT arrets.libelle, lignes.nom, horaires.heure FROM arrets JOIN lignes ON arrets.id = lignes.id JOIN horaires ON lignes.id = horaires.id"
    cursor.execute(query, con=BDD)

    print(query)

    results = cursor.fetchall()
    print(results)
    dataset1 = pd.read_sql_query(results, query, con=BDD)
    print(dataset1)
    cursor.close()
    BDD.close()



def Data2():
    user = "root",
    password = "example",
    host = "localhost",
    port = "3307",
    database = "streamlit_breizhibus"

    global dataset2

    BDD = mybdd.connect(user=user, password=password, host=host, port=port, database=database)

    query = "SELECT * FROM frequentation, lignes"

    dataset2 = pd.read_sql_query(query, con=BDD)

    BDD.close()


def Data3():
    user = "root",
    password = "example",
    host = "localhost",
    port = "3307",
    database = 'streamlit_breizhibus'

    global dataset3

    BDD = mybdd.connect(user=user, password=password, host=host, port=port, database=database)

    query = "SELECT * FROM frequentation, heure"

    dataset3 = pd.read_sql_query(query, con=BDD)

    BDD.close()


def Data4():
    user = "root",
    password = "example",
    host = "localhost",
    port = "3307",
    database = 'streamlit_breizhibus'

    global dataset4

    BDD = mybdd.connect(user=user, password=password, host=host, port=port, database=database)

    query = "SELECT * FROM frequentation, jour"

    dataset4 = pd.read_sql_query(query, con=BDD)

    BDD.close()