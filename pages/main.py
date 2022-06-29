import dash
import dash_bootstrap_components as dbc
from components import main,nav
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/')


layout = dbc.Container(
    [
        nav.navbar,
        main.body_main,
        
    ],
    className="dbc",
    fluid=True,
)