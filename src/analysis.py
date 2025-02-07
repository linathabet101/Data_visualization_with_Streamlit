import anthropic
import pandas as pd

# Fonction pour générer des insights avec Claude
def generate_insights_with_claude(df, question, api_key):
    # Initialiser le client Claude avec la clé API
    client = anthropic.Anthropic(api_key=api_key)

    # Créer un prompt en utilisant les premières lignes du DataFrame et la question
    prompt = f"Voici un extrait des données :\n{df.head()}\n\nRépondez à la question suivante : {question}"

    try:
        # Appel à l'API Claude pour générer la réponse
        response = client.completions.create(
            model="claude-2",
            max_tokens=200,
            prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}"
        )
        
        # Retourner la réponse générée par Claude
        return response.completion
    
    except Exception as e:
        # Gérer les erreurs potentielles
        print(f"Erreur lors de l'appel à l'API Claude : {e}")
        return None
