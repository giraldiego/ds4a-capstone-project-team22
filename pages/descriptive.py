import dash
import dash_bootstrap_components as dbc
from components import main, nav
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/descriptive')


layout = [
    nav.navbar,
    dbc.Container(
        [
            html.H1(['Hello Dash'],
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
                        'title': 'Dash Data Visualization'
                    }
                }
            )

        ])
]
