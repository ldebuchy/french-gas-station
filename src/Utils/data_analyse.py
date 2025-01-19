import pandas as pd
import statistics as st
from typing import Dict, List, Optional

# Fonction pour récupérer les éléments uniques dans une liste de listes
def get_with_no_repetition(data: pd.DataFrame) -> list:
    liste = []
    for ligne in data:
        if type(ligne) is list:
            for element in ligne:
                if element not in liste:
                    liste.append(element)
    return liste

# Fonction pour filtrer les données selon plusieurs critères
def get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate) -> pd.DataFrame:
    options = data

    # Filtrage des données selon le code postal (cp)
    if selected_cp is not None:
        options = options[data["cp"] == selected_cp]
    # Filtrage des données selon la ville
    if selected_city is not None:
        options = options[data["city"] == selected_city]
    # Filtrage des données selon le nom de la station
    if selected_name is not None:
        options = options[data["name"] == selected_name]
    # Filtrage des données selon la marque
    if selected_brand is not None:
        options = options[data["brand"] == selected_brand]
    # Filtrage des données selon le type de carburant
    if selected_fuel is not None:
        options = options[data["fuel"].apply(lambda fuels: selected_fuel in fuels)]
    # Filtrage des données selon la population (route ou autoroute)
    if selected_pop is not None:
        options = options[data["pop"] == selected_pop]
    # Filtrage des données selon la présence d'un automate 24/24
    if selected_automate is not None:
        options = options[data["automate_24_24"] == selected_automate]
    
    return options

# Fonction pour mettre à jour la liste des codes postaux selon les filtres appliqués
def update_cp(
    data: pd.DataFrame,
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, None, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    return [{"label": option, "value": option} for option in options["cp"].unique()]

# Fonction pour mettre à jour la liste des villes selon les filtres appliqués
def update_city(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, None, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    return [{"label": option, "value": option} for option in options["city"].unique()]

# Fonction pour mettre à jour la liste des noms des stations selon les filtres appliqués
def update_name(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, selected_city, None, selected_brand, selected_fuel, selected_pop, selected_automate)
    return [{"label": option, "value": option} for option in options["name"].unique() if option is not None]

# Fonction pour mettre à jour la liste des marques selon les filtres appliqués
def update_brand(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, selected_city, selected_name, None, selected_fuel, selected_pop, selected_automate)
    return [{"label": option, "value": option} for option in options["brand"].unique() if option is not None]

# Fonction pour mettre à jour la liste des types de carburant selon les filtres appliqués
def update_fuel(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, None, selected_pop, selected_automate)
    return [{"label": option, "value": option} for option in get_with_no_repetition(options["fuel"])]

# Fonction pour mettre à jour la liste des types de population (route/autoroute) selon les filtres appliqués
def update_pop(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_automate: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, None, selected_automate)
    choix = ["R", "A"]
    choix_nom_complet = ["Route", "Autoroute"]
    return [{"label": choix_nom_complet[i], "value": choix[i]} for i in range(len(choix)) if choix[i] in options["pop"].values]

# Fonction pour mettre à jour la liste des informations sur les automates 24/24 selon les filtres appliqués
def update_automate(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str]
    ) -> list:
    options = get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, None)
    return [{"label": option, "value": option} for option in options["automate_24_24"].unique() if option is not None]

# Fonction pour obtenir les données nécessaires à un graphique en histogramme
def get_data_histogram(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> pd.DataFrame:

    tmps = get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    departement: Dict[str, Dict[str, List[float]]] = {}

    # Agrégation des prix par département
    for index, station in tmps.iterrows():
        dep = str(station["cp"])[:2]
        if dep not in departement.keys():
            departement[dep] = {
                "price_gazole": [station["price_gazole"]],
                "price_sp95": [station["price_sp95"]],
                "price_sp98": [station["price_sp98"]],
                "price_gplc": [station["price_gplc"]],
                "price_e10": [station["price_e10"]],
                "price_e85": [station["price_e85"]]
            }
        else:
            if not pd.isna(station["price_gazole"]):
                departement[dep]["price_gazole"].append(station["price_gazole"])
            if not pd.isna(station["price_sp95"]):
                departement[dep]["price_sp95"].append(station["price_sp95"])
            if not pd.isna(station["price_sp98"]):
                departement[dep]["price_sp98"].append(station["price_sp98"])
            if not pd.isna(station["price_gplc"]):
                departement[dep]["price_gplc"].append(station["price_gplc"])
            if not pd.isna(station["price_e10"]):
                departement[dep]["price_e10"].append(station["price_e10"])
            if not pd.isna(station["price_e85"]):
                departement[dep]["price_e85"].append(station["price_e85"])

    # Calcul de la moyenne des prix par département
    departement_list = []
    for dep, prices in departement.items():
        departement_list.append({
            "departement": dep,
            "price_gazole": st.mean(prices["price_gazole"]),
            "price_sp95": st.mean(prices["price_sp95"]),
            "price_sp98": st.mean(prices["price_sp98"]),
            "price_gplc": st.mean(prices["price_gplc"]),
            "price_e10": st.mean(prices["price_e10"]),
            "price_e85": st.mean(prices["price_e85"])
        })

    # Conversion en DataFrame
    departement_df = pd.DataFrame(departement_list).sort_values(by="departement").reset_index(drop=True)
    return departement_df

# Fonction pour obtenir les données nécessaires pour la carte
def get_data_map(
    data: pd.DataFrame,
    selected_cp: Optional[str],
    selected_city: Optional[str],
    selected_name: Optional[str],
    selected_brand: Optional[str],
    selected_fuel: Optional[str],
    selected_pop: Optional[str],
    selected_automate: Optional[str]
    ) -> pd.DataFrame:
    tmps = get_data_with_parameter(data, selected_cp, selected_city, selected_name, selected_brand, selected_fuel, selected_pop, selected_automate)
    return tmps["geo_point"]