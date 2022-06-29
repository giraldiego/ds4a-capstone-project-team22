import dash_bootstrap_components as dbc
from dash import html

body_main = html.Div(
    [
        html.H1("Informal Economy In Colombia", style={"margin":"auto", "font-size": "5rem"}),
        html.H2(
            "Informal economy effects on quality of life measured by GEIH dimensions. Longitudinal study (2019-2021) of Barranquilla, Bogotá, Bucaramanga, Cali, Cartagena and Medellín Metropolitan Areas.",
             style={"margin":"auto", "width": "55%", "margin-top": "5rem"}
        ),
        html.H2("CONNECT WITH US ON:", style={"margin":"auto", "margin-top": "5rem"}),
        dbc.Row(
            [
                dbc.Col(
                    html.I(className="fa-brands fa-facebook fa-2x"),
                    class_name="col-md-4 col-sm-4 col-12" ,
                ),
                 dbc.Col(
                    html.I(className="fa-brands fa-instagram fa-2x"),
                    class_name="col-md-4 col-sm-4 col-12" ,
                ),
                 dbc.Col(
                    html.I(className="fa-brands fa-twitter fa-2x"),
                    class_name="col-md-4 col-sm-4 col-12"  ,
                ),        
            ],
            style={"max-width":"25%", "min-width":"25%","margin": "auto","margin-top": "5px"}, 
        )
    ],
    className = "div-main flex-column text-center mb-3"
)