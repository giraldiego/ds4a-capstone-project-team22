import dash_bootstrap_components as dbc
from dash import html

navbar_simple = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("About us", style={"color": "white"})),
    dbc.NavItem(dbc.NavLink("Contact us",  style={"color": "white"})),
    ],
    style={"margin": "auto !important"},
    brand="DS4A",
    color="#000000",
    brand_href="/",
    fluid=True,
    dark=True,
)

navbar = dbc.Row([
    dbc.Col(
        navbar_simple,
        className="col-md-11",
    ),
    dbc.Col(
        dbc.NavLink("Dashboards",className="btn btn-light mt-2", style={"float": "right"}, href="/selection"),
        className="col-md-1",
        style={"background-color":"#000000"},
    ),
    
],
style={"background-color":"#000000"})
