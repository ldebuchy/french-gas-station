import plotly.express as px
import pandas as pd
from typing import Optional
from src.Utils import get_data_histogram

# Fonction pour mettre à jour l'histogramme en fonction des filtres sélectionnés
def update_histogram(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> px.line:
    data_histogram = get_data_histogram(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)

    color_map = {"price_gazole": "pink", "price_sp95": "blue", "price_sp98": "yellow", "price_gplc": "black", "price_e10": "green", "price_e85": "red"}

    # Création d'un graphique en ligne avec Plotly pour afficher les prix des carburants par département
    fig = px.line(
        data_histogram,
        x="departement",
        y=["price_gazole", "price_sp95", "price_sp98", "price_gplc", "price_e10", "price_e85"],
        color_discrete_map=color_map,
        labels={"value": "Prix"},
        markers=True 
    )

    # Mise à jour de la mise en page du graphique (titres des axes)
    fig.update_layout(
        xaxis_title="Departement",
        yaxis_title="Prix",
        barmode="stack",
    )

    return fig
