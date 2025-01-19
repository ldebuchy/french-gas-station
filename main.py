import dash
from src.Pages import set_home_page, set_callbacks
from src.Utils import get_data

# Création de l'application Dash
app = dash.Dash(__name__)

# Récupération des données
data = get_data()

# Configuration de la page d'accueil
set_home_page(app)

# Définition des callbacks
set_callbacks(app, data)
    
# Lancement du serveur en mode débogage
if __name__ == "__main__":
    app.run_server(debug=False)