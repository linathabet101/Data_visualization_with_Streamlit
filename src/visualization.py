import plotly.express as px

def generate_visualizations(df, question):
    """ Génère des graphiques basés sur la question posée """
    figs = []

    # Histogramme si l'utilisateur demande une distribution
    if "distribution" in question.lower() or "histogram" in question.lower():
        for col in df.select_dtypes(include=["number"]).columns:
            fig = px.histogram(df, x=col, title=f"Distribution of {col}")
            figs.append(fig)
    
    # Heatmap pour la corrélation si l'utilisateur demande une analyse de relations
    if "correlation" in question.lower() or "relation" in question.lower():
        fig = px.imshow(df.corr(), text_auto=True, title="Correlation Matrix")
        figs.append(fig)

    # Scatter plot pour les relations entre variables numériques
    if "relationship" in question.lower() or "comparison" in question.lower():
        cols = df.select_dtypes(include=["number"]).columns[:2]
        if len(cols) >= 2:
            fig = px.scatter(df, x=cols[0], y=cols[1], title=f"Relationship: {cols[0]} vs {cols[1]}")
            figs.append(fig)

    return figs
