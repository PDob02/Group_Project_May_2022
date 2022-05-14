from dash import Dash
from dash import dcc
from dash import html
import pandas as pd




app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#fig.update_layout(
  #  plot_bgcolor=colors['background'],
  #  paper_bgcolor=colors['background'],
  #  font_color=colors['text']
#)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Expected Movie Gross Revenue Using Historical Movie Releases ",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

])


if __name__ == '__main__':
    app.run_server(debug=True)