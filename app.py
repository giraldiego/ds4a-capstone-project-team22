#libraries
from dash import Dash, html, dcc
import dash
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



print(dash.__version__)
# Dash instance declaration
app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)
#title app
app.title = "Informal Economy"
#favicon app
app._favicon = ("favicon.jpg")

#Main layout
# app.layout = dbc.Container(
#     [
#         nav.navbar,
#         main.body_main,

#     ],
#     className="dbc",
#     fluid=True,
# )


app.layout = html.Div([
	dash.page_container
])

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', port=7050, debug=True)
