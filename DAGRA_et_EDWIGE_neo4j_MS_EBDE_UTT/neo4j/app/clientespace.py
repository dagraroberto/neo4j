import streamlit as st
from neo4j import GraphDatabase

#from neo4j.v1 import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "utt"), database="locationvelo", encrypted=False)
session = driver.session()

# Create a function to run Cypher queries
def run_query(tx, query):
    result = tx.run(query)
    return result

# Create a function to return the name and ville of all bike rental stations
def get_stations():
    with driver.session() as session:
        result = session.read_transaction(run_query, "MATCH (s:Station) RETURN s.name, s.ville")
        return result

# Create the Streamlit app
def app():
    st.title("ESPACE CLIENT")
    st.header("Recherchez une station dans une ville")

    # Get the user's current ville
    ville = st.text_input("Entrez la ville: Ex: Paris, Lyon (Respectez la class, s'affiche les informations  disponible)")

    # Find the nearest bike rental station
    if ville:
        #query = f"MATCH (s:Station) WHERE s.ville = '{ville}' RETURN s.name, s.ville"
        query = f"MATCH (s:Station) WHERE s.ville = '{ville}' RETURN s.name as name, s.ville as ville, s.address as address"
        with driver.session() as session:
            result = session.run(query)
            data = []
            data.append(["STATION", "ADRESSE", "VILLE"])
            for record in result:
                data.append([record["name"], record["address"], record["ville"]])

            result = session.read_transaction(run_query, query)
            st.table(data)

            # st.success(f"la station est {data}")
    else:
        st.warning("Entrez une ville dans la base s'il vous plait. Ex: Paris, Lyon")

if __name__=="__main__":
    app()