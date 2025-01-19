import requests
import pandas as pd

# URL de l'API pour récupérer les données sur les prix des carburants
url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/prix_des_carburants_j_7/records"

# Paramètres de la requête pour limiter et paginer les résultats
params = {
    "limit": 100,  # Nombre maximum de résultats à récupérer par requête
    "offset": 0  # Position du premier résultat à récupérer
}

# Fonction pour récupérer les données depuis le web
def get_data_from_web() -> pd.DataFrame :
    data = []
    try:
        # Envoi de la première requête pour récupérer les données
        out = requests.get(url, params=params)
        if out.status_code == 200:
            nb_data = out.json().get("total_count", 0)
            while nb_data >= params["limit"]:
                out = requests.get(url, params=params)
                if out.status_code == 200:
                    # Ajouter les résultats de cette page à la liste des données
                    data.extend(out.json().get("results", []))
                    nb_data -= params["limit"]
                    params["offset"] += params["limit"]
                else:
                    break
            # Conversion des données en DataFrame et sauvegarde dans un fichier CSV
            if data:
                df = pd.DataFrame(data)
                df.to_csv("data/raw/rawdata.csv", index=False, encoding="utf-8")
                print("Mise à jour des données depuis le Web terminée.")
                return df
            else:
                print("Aucune donnée récupérée.")
        else:
            print(f"Erreur {out.status_code} : {out.text}")
    except requests.RequestException as e:
        # Gestion des erreurs liées à la requête
        print(f"Erreur lors de la requête : {e}")
        
    return pd.DataFrame()

# Fonction pour vérifier la connexion Internet et récupérer les données
def get_data() -> pd.DataFrame:
    try:
        # Tester la connexion Internet en envoyant une requête à Google
        out = requests.get("https://www.google.fr/", timeout=5)
        if out.status_code == 200:
            return get_data_from_web()
        else:
            print("Connexion Internet non disponible.")
            return pd.DataFrame()
    except requests.RequestException:
        # Si la requête échoue (pas de connexion), afficher un message d'erreur
        print("Connexion Internet non disponible.")
        return pd.DataFrame()