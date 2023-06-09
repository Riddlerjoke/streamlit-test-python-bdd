import mysql.connector as mybdd
import pandas as pd


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
    query = "SELECT lignes.nom AS Lignes, arrets.libelle AS Arrets, horaires.heure AS Horaire FROM horaires INNER JOIN lignes ON horaires.ligne = lignes.id INNER JOIN arrets ON horaires.arret = arrets.id ORDER BY Lignes, Arrêts, Horaire;"
    cursor.execute(query)

    results = cursor.fetchall()
    dataset1 = pd.read_sql_query(results, query, con=BDD)

    cursor.close()
    BDD.close()

    return dataset1



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