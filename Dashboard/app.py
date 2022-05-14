from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.LUX]

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

server = app.server