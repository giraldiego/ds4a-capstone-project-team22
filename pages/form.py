import dash
import dash_bootstrap_components as dbc
from components import form_analysis,nav
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/analysis')


layout = dbc.Container(
    [
        nav.navbar,
        form_analysis.form_variables, 
        
    ],
    className="dbc",
    fluid=True,
)