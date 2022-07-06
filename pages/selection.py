import dash
import dash_bootstrap_components as dbc
from components import main,nav
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/selection')


layout = dbc.Container(
    [
        nav.navbar,
        dbc.Row([
            dbc.Col(

                    dbc.Card(
                        [
                            dbc.CardImg(src="assets/powerbi.png", top=True, style={"width": "100%", "height":"100%"}),
                            dbc.CardBody(
                                [
                                    html.H4("tablero analisis descriptivo", className="card-title"),
                                    dbc.Button("Ir", color="primary", href="/descriptive"),
                                ],
                            
                            ),
                        ],
                        style={"width": "18rem", "margin": "auto", "float": "right"},
                    ),
            ),
                    dbc.Col(

                    dbc.Card(
                        [
                            dbc.CardImg(src="assets/form.png", top=True, style={"width": "100%", "height":"100%"}),
                            dbc.CardBody(
                                [
                                    html.H4("formulario informalidad", className="card-title"),
                                    dbc.Button("Ir", color="primary", href="/analysis"),
                                ],
                            ),
                        ],
                        style={"width": "18rem", "margin": "auto", "float": "left"},
                    ),
            ),
        ],
            style={"width":"100%", "height": "100%", "margin-top": "10vw"}
        )
        
    ],
    className="dbc",
    fluid=True,
)