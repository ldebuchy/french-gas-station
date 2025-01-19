import folium
import pandas as pd
from src.Utils import get_data_map
from typing import Optional

def update_map(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> str:
    data_map = get_data_map(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)

    # Coordonnées pour centrer la carte sur la France
    coords = (46.539758, 2.430331)
    # Crée la carte avec les options définies
    map = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=5)

    # Ajoute des cercles pour chaque position sur la carte
    for position in data_map.values:
        if position is not None :
            folium.CircleMarker(
            location = (position["lat"], position["lon"]),
            radius = 2,
            color = 'red',
            fill = True,
            fill_color = 'red'
            ).add_to(map)

    return map._repr_html_()