import dash_bootstrap_components as dbc
from dash import html

navbar_simple = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("About us", style={"color": "white"})),
    dbc.NavItem(dbc.NavLink("Contact us",  style={"color": "white"})),
    ],
    style={"margin": "auto !important"},
    brand="DS4A",
    color="#000000",
    fluid=True,
    dark=True,
)

navbar = dbc.Row([
    navbar_simple,
   html.Div(
        dbc.Button("Dashboards",className="btn btn-light mt-2", style={"float": "right"}),
        style={ "position": "absolute"}
    ),
])
