from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from app import app
from pages import page1cpy, page2, home

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Visualizations", href="/viz"),
        dbc.DropdownMenuItem("Machine Learning", href="/model"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/movie.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Movie Dashboard", className="ml-2")),
                    ],
                    align="center",
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]

    ),
    color = "dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{1}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])


def display_page(pathname):
    if pathname== "/viz":
        return page1cpy.layout
    elif pathname == "/model":
        return page2.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)