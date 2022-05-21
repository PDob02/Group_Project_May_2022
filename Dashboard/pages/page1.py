import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from config import db_password
from sqlalchemy import text

<<<<<<< HEAD

movies_df = pd.read_csv("Resources/movies.csv")

markdown_text = '''
### Page 1 - Visualizations

This page will contain various visualizations that will show trends in movies data.
For example, the highest grossing movies by year. 

Sample graphs are below:



'''
=======
# movies_df = pd.read_csv("movies.csv")
t = text("SELECT * FROM movies;")
movies_df = pd.read_sql(t, con=f"postgresql://postgres:{db_password}@127.0.0.1:5432/group_project")
>>>>>>> 4c7e225795182c18edf36e9dbbe3cdf9c22645d9

layout = html.Div([

    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Visualizations'), className="mb-2")
        ]),

    # dcc.Input(
    # id='slct_year',
    # type='number',
    # min = 1800,
    # max = 2022,
    # placeholder = "Enter a Year"
    # ),
    dcc.Dropdown(
        id='slct_year',
        options=[
            {'label': 1980, 'value': 1980},
            {'label': 1981, 'value': 1981},
            {'label': 1982, 'value': 1982},
            {'label': 1983, 'value': 1983},
            {'label': 1984, 'value': 1984},
            {'label': 1985, 'value': 1985},
            {'label': 1986, 'value': 1986},
            {'label': 1987, 'value': 1987},
            {'label': 1988, 'value': 1988},
            {'label': 1989, 'value': 1989},
            {'label': 1990, 'value': 1990},
            {'label': 1991, 'value': 1991},
            {'label': 1992, 'value': 1992},
            {'label': 1993, 'value': 1993},
            {'label': 1994, 'value': 1994},
            {'label': 1995, 'value': 1995},
            {'label': 1996, 'value': 1996},
            {'label': 1997, 'value': 1997},
            {'label': 1998, 'value': 1998},
            {'label': 1999, 'value': 1999},
            {'label': 2000, 'value': 2000},
            {'label': 2001, 'value': 2001},
            {'label': 2002, 'value': 2002},
            {'label': 2003, 'value': 2003},
            {'label': 2004, 'value': 2004},
            {'label': 2005, 'value': 2005},
            {'label': 2006, 'value': 2006},
            {'label': 2007, 'value': 2007},
            {'label': 2008, 'value': 2008},
            {'label': 2009, 'value': 2009},
            {'label': 2010, 'value': 2010},
            {'label': 2011, 'value': 2011},
            {'label': 2012, 'value': 2012},
            {'label': 2013, 'value': 2013},
            {'label': 2014, 'value': 2014},
            {'label': 2015, 'value': 2015},
            {'label': 2016, 'value': 2016},
            {'label': 2017, 'value': 2017},
            {'label': 2018, 'value': 2018},
            {'label': 2019, 'value': 2019},
            {'label': 2020, 'value': 2020},
        ],
        multi = False
    ),

    html.Br(),

    dcc.Graph(id="bar-revenue-by-year", figure ={}),

    html.Br(),

    dcc.Graph(id="scatter-matrix", figure={}),

    ]),


  
])




@callback(
     [Output(component_id='bar-revenue-by-year', component_property='figure'),
     Output(component_id="scatter-matrix", component_property='figure')],
     [Input(component_id='slct_year', component_property='value')]
)

def update_graph(option_slctd):

    movies_copy = movies_df.copy()
    movies_copy = movies_copy.sort_values('gross', ascending=False)
    movies_copy = movies_copy[movies_copy['year']== option_slctd].head(50)


    #Plotly Express
    fig = px.bar(
        data_frame = movies_copy,
        x = 'name',
        y = 'gross',
        hover_name = movies_copy['name'],
        labels = {'Title of Movie': 'Gross Revenue'},
        title = f"Gross Revenue for Top 50 Movies Released in {option_slctd}"
        
    )


    fig2 = px.scatter_matrix(
        movies_copy,
        dimensions=["rating", "genre", "score", "budget", "gross"],
        color="name",
        title="Scatter Matrix for Movie Data"
        )

    return fig, fig2