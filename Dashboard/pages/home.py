import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback
from config import db_password
from sqlalchemy import text
import plotly.io as pio
import dash_bootstrap_components as dbc

markdown_text = '''

Over one billion movie tickets are sold worldwide annually resulting in box office revenues of over $11 billion dollars. 

Big-budget films with recognizable stars sometimes underperform at the box office. Star-studded comedy such as "How Do You Know" 
with Reese Witherspoon, Paul Rudd, and Jack Nicholson earned $49.6 million despite a budget of $120 million. 
Possibly even more suprising, "Slumdog Millionaire" achieved unphathomable success. Its director, Danny Boyle, was respected
but had not yet earned his blockbuster director moment. It had a cast of mostly unknown actors. Yet, Fox Searchlight invested 
$15 million into the film with hopes it would gain critic attention and circulate positively in award festivals. The film would
go onto earn $141 million domestic. If these film examples tell us anything, it's that there doesn't seem to be a formula to 
follow that guarantees a successful film. This made us ask the question, can the gross revenue of a movie be predicted before 
it is released? 

What factors determine whether a movie will be successful? Does the day of the week a film is released have an impact on how much 
money it will make at the box office? Will the director, writer, or production company play a role in how successful a film will 
be? How does the leading actor's accolades or age impact how well the movie performs? 

This tool for movie industry professionals uses machine leanrning to predict a film's gross revenue using factors including but 
not limited to month of release, budget, production company, and lead actor/actress. 


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
https://www.cbsnews.com/pictures/biggest-movie-flops-box-office-bombs/38/
https://www.looper.com/198166/movies-that-became-unexpected-blockbusters/


'''


markdown_machine_learning = '''
In many real world situations, mutliple factors weigh into an outcome or prediction. In these cases, multiple linear regression 
can be used to predict a dependent variable based on multiple independent varaibles. The machine learning model is given data to 
train on in which it quantifies the linear relationships. When new data is presented, the model can use the independent variables 
and give the user a prediction of the dependent. 

In developing the product, multiple linear regression models were tested and the final version uses ridge regression, which 
supervised learning model that predicts a continuous quantity. This tool uses the Ridge model to predict whether a movie will be 
successful, which is measured by the gross revenue it earns. Gross earnings are predicted using rating, genre, director, writer, 
lead actor, company, runtime, month of release, day of week of release, budget, the awards won by the lead actor, and the age of 
the lead actor. 



'''


layout = html.Div([

    html.Center(
    html.Img(src="/assets/movie_poster.png", style={'width': '100%'})),

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
