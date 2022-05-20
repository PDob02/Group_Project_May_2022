import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


movies_df = pd.read_csv("movies.csv")

markdown_text = '''
### Page 1 - Visualizations

This page will contain various visualizations that will show trends in movies data.
For example, the highest grossing movies by year. 

Sample graphs are below:



'''

layout = html.Div([

    dcc.Markdown(children=markdown_text),

    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Visualizations'), className="mb-2")
        ]),

    dcc.Input(
    id='slct_year',
    type='number',
    min = 1800,
    max = 2022,
    placeholder = "Enter a Year"
    ),

    dcc.Dropdown(
        options=[
            {'label': '1980', 'value': '1980'},
            {'label': '1981', 'value': '1981'},
            {'label': '1982', 'value': '1982'},
            {'label': '1983', 'value': '1983'},
            {'label': '1984', 'value': '1984'},
            {'label': '1985', 'value': '1985'},
            {'label': '1986', 'value': '1986'},
            {'label': '1987', 'value': '1987'},

        ],
        multi = False
    )
   
    # html.Br(),

    # dcc.Graph(id="bar-revenue-by-year", figure ={}),

    # html.Br(),

    # dcc.Graph(id="scatter-matrix", figure={}),

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
    movies_copy = movies_copy[movies_copy['year']== option_slctd]


    #Plotly Express
    fig = px.bar(
        data_frame = movies_copy,
        x = 'name',
        y = 'gross',
        hover_name = movies_copy['name'],
        labels = {'Title of Movie': 'Gross Revenue'},
        title = f"Gross Revenue for Movies Released in {option_slctd}"
        
    )


    fig2 = px.scatter_matrix(
        movies_copy,
        dimensions=["rating", "genre", "score", "budget", "gross"],
        color="name",
        title="Scatter Matrix for Movie Data"
        )

    return fig, fig2


# if __name__ == '__main__':
#     app.run_server(debug=True)