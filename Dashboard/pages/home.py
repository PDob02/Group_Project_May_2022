import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback
from config import db_password
from sqlalchemy import text
import plotly.io as pio
import dash_bootstrap_components as dbc

markdown_text = '''

Over one billion movie tickets are sold worldwide annually resulting in box office revenues of over $11 billion dollars. 

Can the gross revenue of a movie be predicted before it is released? What factors determine whether a movie will be successful?

Using machine learning, this tool for movie industry professionals will predict gross revenue using factors 
including but not limited to month of release, budget, production company, and lead actor/actress. 


'''


markdown_contributors = '''
### Contributors 
David Hyde | Kylie Hicks | Patrick Dobry | Kaiya Hull

'''




markdown_citations = ''' ### Citations & Sources

https://www.the-numbers.com/market/ \n
https://sciencing.com/advantages-using-independent-group-ttest-8647277.html \n
https://www.kaggle.com/datasets/danielgrijalvas/movies \n
https://en.wikipedia.org/wiki/Main_Page \n
https://en.wikipedia.org/wiki/List_of_actors_with_Academy_Award_nominations#List_of_actors


'''


markdown_machine_learning = '''
Linear regression is a statistical model that is used to predict a dependent variable based on
a single independent variable. In many instances in the real world, mutliple factors weigh into 
an outcome or prediction. In these cases, multiple linear regression can be used to predict 
a dependent variable based on multiple independent varaibles. The machine leanring model is given
data to train on in which it quantifies the linear relationships. When new data is presented, the 
model can use the independent variables and give the user a prediction of the dependent. 

In developing the product, three types of linear regression models were tested: LinearRegression, 
Ridge, and LASSO.

This tool uses the Ridge model to predict whether a movie will be successful, which 
is measured by the gross revenue it earns. Gross earnings are predicted using rating, 
genre, director, writer, lead actor, company, runtime, month of release, day of week of 
release, budget, the awards won by the lead actor, and the age of the lead actor. 

'''


layout = html.Div([

    html.Center(
    html.Img(src="/assets/posters.png", style={'width': '100%'})),

    html.Br(),


    dbc.Container([
    html.Center(
    dbc.Row([
        dbc.Col(html.H1(children='Welcome to the Movie Dashboard'), className="mb-4")
    ])),

    html.Br(),
 
    dcc.Markdown(children=markdown_text),

    html.Br(),
    html.Br(), 


    html.Center(
    dbc.Row([
        dbc.Col(html.H1(children='Multiple Linear Regression Overview '), className="mb-4")
    ])),
    dcc.Markdown(children=markdown_machine_learning),

    html.Br(),
    html.Br(),
    html.Br(),

    html.Center(
        dcc.Markdown(children=markdown_contributors)),

    html.Br(), 
    html.Br(),
    html.Br(),  

    html.Center(
        dcc.Markdown(children=markdown_citations))


])

])
