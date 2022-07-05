import dash
import dash_bootstrap_components as dbc
from components import form_analysis,nav
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/descriptive')


layout = dbc.Container(
    [
        nav.navbar,
        html.Iframe(
            src="https://app.powerbi.com/view?r=eyJrIjoiZGM0MzM5YTMtYjc4NC00MmJjLTgxMTMtZjljMDgzMjBiZmYwIiwidCI6IjJkN2QzYzU0LTE3MTgtNGY2YS1iNzQwLWFiNTUzZTg5NWVkNyIsImMiOjR9&pageName=ReportSection608991b772c9c021b7e8",
            title="INFORMAL_APP_TEAM_22",
            width="100%",
            height="100%",
            style={"position":"absolute",}
            )
        
    ],
    className="dbc",
    fluid=True,
)