import streamlit as st
from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "utt"), database="locationvelo", encrypted=False)
session = driver.session()


# Create a Streamlit app
def app():
    # Exécution de la requête
    query = "MATCH (n:Station) RETURN n.name AS name, n.address AS address, n.ville AS ville"
    query1 = "MATCH (s:Client) RETURN s.name AS name, s.email AS email"
    query2 = "MATCH (s:Station {name: 'Eiffel Tower Station'})<-[:LOCATION_A]-(v:Velo) WHERE NOT (v)-[:LOUE]->() RETURN v.name as name, v.model as model"


    result = session.run(query)

    result1 = session.run(query1)

    result2 = session.run(query2)

    st.title("ESPACE ADMINISTRATEUR VISUALISATION ETAT")

    st.header("LES DIFFERENTES STATIONS DE VELO")
    # Récupération des résultats
    data = []
    data.append(["STATION", "ADRESSE", "VILLESSS"])
    for record in result:
        data.append([record["name"], record["address"], record["ville"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data)

    st.header("LES CLIENTS")
    # Récupération des résultats
    data1 = []
    data1.append(["CLIENT", "EMAIL"])
    for record1 in result1:
        data1.append([record1["name"], record1["email"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data1)

    st.header("LES VELOS LOUE à Eiffel Tower Station")
    # Récupération des résultats
    data2 = []
    data2.append(["Station","TYPE VELO", "MODEL"])
    for record2 in result2:
        data2.append(["Eiffel Tower Station", record2["name"], record2["model"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data2)


if __name__=="__main__":
    app()