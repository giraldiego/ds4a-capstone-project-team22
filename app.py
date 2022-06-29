#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from components import nav,main

#declared external css to use
external_stylesheets = [
    dbc.themes.BOOTSTRAP, 
    "assets/styles.css",
    {
        'href': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==',
        'crossorigin': 'anonymous'
    }
]




# Dash instance declaration
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#title app
app.title = "Informal economy"
#favicon app
app._favicon = ("favicon.jpg")

#Main layout
app.layout = dbc.Container(
    [
        nav.navbar,
        main.body_main,
        
    ],
    className="dbc",
    fluid=True,
)

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(debug=True)