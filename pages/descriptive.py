import dash
import dash_bootstrap_components as dbc
from components import main, nav
from dash import html, dcc, callback, Input, Output
from dash.dependencies import Output, Input

import pandas as pd

dash.register_page(__name__, path='/descriptive')



layout = [
    nav.navbar,
    dbc.Container(
        [
            html.H1(['Descriptive Dashboard for Informal Economy'],
                    className="h-100 p-5 bg-light border rounded-3"),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5],
                         'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Boilerplate Data Visualization'
                    }
                }
            )

        ])
]

# layout = dbc.Container([
#     html.H1(["Google Translator"],  className="h-100 p-5 bg-light border rounded-3"),
#     dbc.Input(id="my-input", placeholder="Type something", type="text", value="home"),
#     html.Br(),
#     html.P(id="my-output", children=['home'])
# ])

# # Callback
# @callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     # translated_input_text = GoogleTranslator(source='auto', target='es').translate(input_value)
#     translated_input_text = input_value + " en otro idioma"
#     return 'Your translation:  "{}"'.format(translated_input_text)
