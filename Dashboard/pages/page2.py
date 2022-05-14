import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


markdown_text = '''
### Page 2 - Machine Learning Model

This page will contain our machine learning model.
The user will be able to enter information about a movie (release month, budget, genre, etc.)
and our model will predict the movie's gross earnings. 


'''



layout = html.Div([

    dcc.Markdown(children=markdown_text),
    dbc.Container([
    dbc.Row([
        dbc.Col(html.H1(children='Machine Learning'), className="mb-2")
    ]),
])
])