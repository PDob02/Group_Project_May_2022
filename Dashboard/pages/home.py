import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback


markdown_text = '''
### Welcome to the Movie Dashboard

This is our homepage. It will include:
- Purpose of the project
- Practical uses for the project
- Sources/citations
- Names of contributors

'''

layout = html.Div([
    dcc.Markdown(children=markdown_text)

])