from dash import Dash, dcc, html


def set_home_page(app: Dash) -> None:
    app.layout = html.Div(
        [
            html.H1("Les stations d'enssence en France"),
            html.Div(
                className="param",
                children=[
                    html.H2("Paramètres"),
                    html.Div([
                        html.H5("Code Postal"),
                        dcc.Dropdown(
                            id="postal-dropdown",
                            options=[],
                            multi=False,
                            searchable=True,
                            style={"width": "50%"},
                        ),
                        html.H5("Ville"),
                        dcc.Dropdown(
                            id="city-dropdown",
                            options=[],
                            multi=False,
                            searchable=True,
                            style={"width": "50%"},
                        ),
                        html.H5("Nom de la station"),
                        dcc.Dropdown(
                            id="name-dropdown",
                            options=[],
                            multi=False,
                            searchable=True,
                            style={"width": "50%"},
                        ),
                        html.H5("Marque de la station"),
                        dcc.Dropdown(
                            id="brand-dropdown",
                            options=[],
                            multi=False,
                            searchable=True,
                            style={"width": "50%"},
                        )
                    ]),
                    html.Div([
                        html.H5("Essence disponible"),
                        dcc.Dropdown(
                            id="fuel-dropdown",
                            options=[],
                            multi=False,
                            searchable=False,
                            style={"width": "50%"},
                        ),
                        html.H5("Enplacement"),
                        dcc.Dropdown(
                            id="pop-dropdown",
                            options=[],
                            searchable=False,
                            multi=False,
                            style={"width": "50%"},
                        ),
                        html.H5("Automate 24-24"),
                        dcc.Dropdown(
                            id="automate-dropdown",
                            options=[],
                            searchable=False,
                            multi=False,
                            style={"width": "50%"},
                        )
                    ]),
                ]
            ),
            html.Div(
                className="result",
                children=[
                    html.H2("Résultats concernant votre recherche"),
                    html.H4("Moyenne des prix selon les départements de votre recherche"),
                    dcc.Graph(id="histogram"),
                    html.H4("Carte des stations essences de votre recherche"),
                    html.Iframe(
                        id="heatmap",
                        width="100%",
                        height="500",
                    ),
                ]
            )
        ]
    )