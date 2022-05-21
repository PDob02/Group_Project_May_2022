from ast import Return
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import joblib


markdown_text = '''
### Page 2 - Machine Learning Model

This page will contain our machine learning model.
The user will be able to enter information about a movie (release month, budget, genre, etc.)
and our model will predict the movie's gross earnings. 


'''


layout = html.Div([


    dbc.Row([html.H3(children='Predict Gross Revenue')]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Rating')),
        dbc.Col(dcc.Dropdown(id='rating',
                                options = {
                                    'G': 'G',
                                    'PG': 'PG',
                                    'PG-13': 'PG-13',
                                    'R': 'R'},
                                    placeholder='Select the rating' ))
    ]),
    html.Br(),                
    dbc.Row([
        dbc.Col(html.Label(children='Genre')),
        dbc.Col(dcc.Dropdown(id='genre', 
                options = {
                    'Drama': 'Drama',
                    'Adventure': 'Adventure',
                    'Action': 'Action',
                    'Comedy': 'Comedy',
                    'Horror': 'Horror',
                    'Biography': 'Biography',
                    'Crime': 'Crime',
                    'Fantasy': 'Fantasy',
                    'Sci-Fi': 'Sci-Fi',
                    'Animation': 'Animation',
                    'Thriller': 'Thriller'},
                placeholder='Select the genre'))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Month of Release')),
        dbc.Col(dcc.Dropdown(id='release-month',
                options = {
                    'January': 'January',
                    'February': 'February',
                    'March': 'March',
                    'April': 'April',
                    'May': 'May',
                    'June': 'June',
                    'July': 'July',
                    'August': 'August',
                    'September': 'September',
                    'October': 'October',
                    'November': 'November',
                    'December': 'December'},
                placeholder='Select the month of release'))

    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children="Day of Week of Movie's Release")),
        dbc.Col(dcc.Dropdown(id='release-dow',
                options = {
                    'Monday': 'Monday',
                    'Tuesday': 'Tuesday',
                    'Wednesday': 'Wednesday',
                    'Thursday': 'Thursday',
                    'Friday': 'Friday',
                    'Saturday': 'Saturday',
                    'Sunday': 'Sunday'},
                placeholder='Select the day of the week'))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Director')),
        dbc.Col(dcc.Dropdown(id='director',
                options = {
                    'Woody Allen': 'Woody Allen',
                    'Clint Eastwood': 'Clint Eastwood',
                    'Steven Spielberg': 'Steven Spielberg',
                    'Ridley Scott': 'Ridley Scott',
                    'Ron Howard': 'Ron Howard',
                    'Joel Schumacher': 'Joel Schumacher',
                    'Steven Soderbergh': 'Steven Soderbergh',
                    'Tim Burton': 'Tim Burton',
                    'Barry Levinson': 'Barry Levinson',
                    'Spike Lee': 'Spike Lee',
                    'Martin Scorsese': 'Martin Scorsese',
                    'Oliver Stone': 'Oliver Stone',
                    'Robert Zemeckis': 'Robert Zemeckis',
                    'Wes Craven': 'Wes Craven',
                    'Brian De Palma': 'Brian De Palma',
                    'Directors': 'Directors',
                    'Walter Hill': 'Walter Hill',
                    'Garry Marshall': 'Garry Marshall',
                    'John Carpenter': 'John Carpenter',
                    'Rob Reiner': 'Rob Reiner',
                    'Ivan Reitman': 'Ivan Reitman',
                    'Tony Scott': 'Tony Scott',
                    'Sam Raimi': 'Sam Raimi',
                    'Renny Harlin': 'Renny Harlin',
                    'Other': 'Other'},
                placeholder='Select the director'))
    ]),
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Writer')),
    dbc.Col(dcc.Dropdown(id='writer',
            options = {
                'Stephen King': 'Stephen King',
                'Woody Allen': 'Woody Allen',
                'John Hughes': 'John Hughes',
                'Luc Besson': 'Luc Besson',
                'Wes Craven': 'Wes Craven',
                'Joel Coen': 'Joel Coen',
                'William Shakespeare': 'William Shakespeare',
                'M. Night Shyamalan': 'M. Night Shyamalan',
                'Brian Helgeland': 'Brian Helgeland',
                'Quentin Tarantino': 'Quentin Tarantino',
                'Robert Rodriguez': 'Robert Rodriguez',
                'David Mamet': 'David Mamet',
                'John Carpenter': 'John Carpenter',
                'Michael Crichton': 'Michael Crichton',
                'Kevin Smith': 'Kevin Smith',
                'Ehren Kruger': 'Ehren Kruger',
                'Leigh Whannell': 'Leigh Whannell',
                'Other': 'Other'},
            placeholder='Select the writer')),
    ]), 
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Production Company')),
    dbc.Col(dcc.Dropdown(id='company',
            options = {
                'Other':'Other',
                'Universal Pictures':'Universal Pictures',
                'Columbia Pictures':'Columbia Pictures',
                'Warner Bros':'Warner Bros',
                'Paramount Pictures':'Paramount Pictures',
                'Twentieth Century Fox':'Twentieth Century Fox',
                'New Line Cinema':'New Line Cinema',
                'Walt Disney Pictures':'Walt Disney Pictures',
                'Touchstone Pictures':'Touchstone Pictures',
                'Metro-Goldwyn-Mayer (MGM)':'Metro-Goldwyn-Mayer (MGM)',},
            placeholder='Select the company')),
    ]), 
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Lead Actor')),
    dbc.Col(dcc.Dropdown(id='actor',
            options = {
                'Nicolas Cage': 'Nicolas Cage',
                'Robert De Niro': 'Robert De Niro',
                'Tom Hanks': 'Tom Hanks',
                'Tom Cruise': 'Tom Cruise',
                'Bruce Willis': 'Bruce Willis',
                'Denzel Washington': 'Denzel Washington',
                'Sylvester Stallone': 'Sylvester Stallone',
                'Johnny Depp': 'Johnny Depp',
                'Kevin Costner': 'Kevin Costner',
                'Adam Sandler': 'Adam Sandler',
                'Eddie Murphy': 'Eddie Murphy',
                'Matthew McConaughey': 'Matthew McConaughey',
                'Arnold Schwarzenegger': 'Arnold Schwarzenegger',
                'Harrison Ford': 'Harrison Ford',
                'Keanu Reeves': 'Keanu Reeves',
                'John Travolta': 'John Travolta ',
                'Dwayne Johnson': 'Dwayne Johnson',
                'Matt Damon': 'Matt Damon',
                'Mel Gibson': 'Mel Gibson',
                'Robin Williams': 'Robin Williams',
                'Ben Stiller': 'Ben Stiller',
                'Mark Wahlberg': 'Mark Wahlberg',
                'Will Smith': 'Will Smith',
                'Brad Pitt': 'Brad Pitt',
                'Meryl Streep': 'Meryl Streep',
                'Jeff Bridges': 'Jeff Bridges',
                'Clint Eastwood': 'Clint Eastwood',
                'Richard Gere': 'Richard Gere',
                'Jim Carrey': 'Jim Carrey',
                'Ben Affleck': 'Ben Affleck',
                'Liam Neeson ': 'Liam Neeson ',
                'Al Pacino': 'Al Pacino',
                'George Clooney': 'George Clooney',
                'Christian Bale': 'Christian Bale',
                'Sandra Bullock': 'Sandra Bullock',
                'Leonardo DiCaprio': 'Leonardo DiCaprio',
                'Robert Downey Jr.': 'Robert Downey Jr.',
                'John Cusack': 'John Cusack',
                'Steve Martin': 'Steve Martin',
                'Will Ferrell': 'Will Ferrel',
                'Other': 'Other'},
            placeholder='Select the lead actor')),
    ]), 
    html.Br(),                
    dbc.Row([
        dbc.Col(html.Label(children='Nominations Won by Lead Actor')),
        dbc.Col(dcc.Slider(id='nominations', min=0, max=15, value=0)),
    ]),
        html.Br(),                
    dbc.Row([
        dbc.Col(html.Label(children='Awards Won by Lead Actor')),
        dbc.Col(dcc.Slider(id='awards', min=0, max=15, value=0)),
    ]),
    html.Br(),                
    dbc.Row([
        dbc.Col(html.Label(children='Age of Lead Actor')),
        dbc.Col(dcc.Slider(id='age', min=0, max=100, value=0)),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Select the Budget Amount')),
        dbc.Col(dcc.Slider(id='budget', min=0, max=50000000, value=0)),
    ]),
    html.Br(),                
    dbc.Row([
        dbc.Col(html.Label(children='Runtime')),
        dbc.Col(dcc.Slider(id='runtime', min=0, max=200, value=0)),
    ]),
    html.Br(),
    dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color='primary')
    ]),
    html.Br(),
    dbc.Row([html.Div(id='prediction-output')])

    ])



@callback(Output(component_id='prediction-output', component_property='children'),
                Input(component_id='submit-val', component_property='n_clicks'),
                State(component_id='rating', component_property='value'),
                State(component_id='genre', component_property='value',),
                State(component_id='release-month', component_property='value',),
                State(component_id='release-dow', component_property='value',),
                State(component_id='director', component_property='value',),
                State(component_id='writer', component_property='value',),
                State(component_id='company', component_property='value',),
                State(component_id='actor', component_property='value',),
                State(component_id='nominations', component_property='value',),
                State(component_id='awards', component_property='value',),
                State(component_id='age', component_property='value',),
                State(component_id='budget', component_property='value',),
                State(component_id='runtime', component_property='value',),

                )

def update_result(n_clicks, rating, genre, release_month, release_dow, director,
                    writer, company, actor, nominations, awards, age, budget, runtime):


    print(rating, genre, budget)
    # x = np.array([[float(rating), float(genre), float(budget)]])
    jlib_model = joblib.load('Ridge_model.joblib')
    jlib_model.predict(x)
    

    return f"The expected gross revenue is: {prediction}"

   