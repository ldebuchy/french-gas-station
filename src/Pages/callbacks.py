from dash import Dash, Input, Output
from typing import Optional
from src.Utils import update_cp, update_city, update_name, update_brand, update_fuel, update_pop, update_automate
from src.Pages.Viz import update_histogram, update_map
import pandas as pd
import plotly.express as px



def set_callbacks(app: Dash, data: pd.DataFrame) -> None:
    # Callback pour mettre à jour les options du dropdown postal en fonction des autres sélections
    @app.callback(
        Output("postal-dropdown", "options"),
        [
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_postal(
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_cp(data, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    
    # Callback pour mettre à jour les options du dropdown des villes en fonction des autres sélections
    @app.callback(
        Output("city-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_city(
        selected_cp: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_city(data, selected_cp, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    
    # Callback pour mettre à jour les options du dropdown des stations en fonction des autres sélections
    @app.callback(
        Output("name-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_name(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_name(data, selected_cp, selected_city, selected_brand, selected_fuel, selected_pop, selected_automate)

    # Callback pour mettre à jour les options du dropdown des marques en fonction des autres sélections
    @app.callback(
        Output("brand-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ]
    )
    def callbacks_brand(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_brand(data, selected_cp, selected_city, selected_name, selected_fuel, selected_pop, selected_automate)

    # Callback pour mettre à jour les options du dropdown des carburants en fonction des autres sélections
    @app.callback(
        Output("fuel-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_fuel(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_fuel(data, selected_cp, selected_city, selected_name, selected_brand, selected_pop, selected_automate)
    
    # Callback pour mettre à jour les options du dropdown des types de route en fonction des autres sélections
    @app.callback(
        Output("pop-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_pop(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_automate: Optional[str]
        ) -> list:
        return update_pop(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_automate)
    
    # Callback pour mettre à jour les options du dropdown des stations avec automate en fonction des autres sélections
    @app.callback(
        Output("automate-dropdown", "options"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value")
        ],
    )
    def callbacks_automate(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        ) -> list:
        return update_automate(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop)
    
    # Callback pour mettre à jour la carte (carte thermique) en fonction des autres sélections
    @app.callback(
        Output("heatmap", "srcDoc"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_maps(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> str:
        return update_map(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    
    # Callback pour mettre à jour l'histogramme des prix en fonction des autres sélections
    @app.callback(
        Output("histogram", "figure"),
        [
            Input("postal-dropdown", "value"),
            Input("city-dropdown", "value"),
            Input("name-dropdown", "value"),
            Input("brand-dropdown", "value"),
            Input("fuel-dropdown", "value"),
            Input("pop-dropdown", "value"),
            Input("automate-dropdown", "value")
        ],
    )
    def callbacks_histogram(
        selected_cp: Optional[str],
        selected_city: Optional[str],
        selected_name: Optional[str],
        selected_brand: Optional[str],
        selected_fuel: Optional[str],
        selected_pop: Optional[str],
        selected_automate: Optional[str]
        ) -> px.line:
        return update_histogram(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)