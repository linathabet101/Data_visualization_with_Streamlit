import streamlit as st
import pandas as pd
import os
import anthropic
from src.analysis import generate_insights_with_claude

# Charge la clé API de Claude à partir de l'environnement
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Fonction d'upload de fichier CSV
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# Fonction de génération d'insights avec Claude
def generate_insights(df, question):
    # Assure-toi que la clé API Claude est définie
    if CLAUDE_API_KEY is None:
        st.error("La clé API Claude n'est pas définie.")
        return None
    return generate_insights_with_claude(df, question, CLAUDE_API_KEY)

# Interface utilisateur avec Streamlit
st.title("AI-Powered DataViz App")

# Upload du fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("Aperçu des données:", df.head())

    # Poser une question sur les données
    question = st.text_input("Posez une question sur les données")
    if question:
        insights = generate_insights(df, question)
        if insights:
            st.write("Insights générés:", insights)

# Affichage d'une erreur en cas de problème
else:
    st.warning("Veuillez télécharger un fichier CSV.")

