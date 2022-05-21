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
    min = 1980,
    max = 2022,
    placeholder = "Enter a Year"
    ),
   
    html.Br(),

    dcc.Graph(id="bar-revenue-by-year", figure ={}),
    html.Br(),

    dcc.Graph(id="scatter-matrix", figure={}),
    html.Br(),
    
    dcc.Graph(id="my-output", figure={}),

    ]),


  
])




@callback(
     [Output(component_id='bar-revenue-by-year', component_property='figure'),
     Output(component_id="scatter-matrix", component_property='figure')],
     Output(component_id="my-output", component_property='figure'),
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

    # https://plotly.com/python/heatmaps/
    data= 1
    fig3 = px.imshow(
        data_frame = movies_df,
        labels=dict(x="Day of Week", y="Time of Day", color="Gross Revenue"),
        x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'],
        y=['Morning', 'Afternoon', 'Evening']
        )
    fig3.update_xaxes(side="top")

    return fig, fig2, fig3

# if __name__ == '__main__':
#     app.run_server(debug=True)