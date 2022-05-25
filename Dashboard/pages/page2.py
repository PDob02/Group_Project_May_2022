from ast import Return
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import joblib
from encode import encode


markdown_text = '''
Enter the required information for the upcoming release or movie project. The machine learning model will predict its expected gross revenue.


'''


layout = html.Div([

    dcc.Markdown(markdown_text),
    html.Br(),

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
                    'Action': 'Action',
                    'Adventure': 'Adventure',
                    'Animation': 'Animation',
                    'Biography': 'Biography',
                    'Comedy': 'Comedy',
                    'Crime': 'Crime',
                    'Drama': 'Drama',
                    'Horror': 'Horror',
                    'Other': 'Other'},
                placeholder='Select the genre'))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Month of Release')),
        dbc.Col(dcc.Dropdown(id='release-month',
                options = {
                    '1': 'January',
                    '2': 'February',
                    '3': 'March',
                    '4': 'April',
                    '5': 'May',
                    '6': 'June',
                    '7': 'July',
                    '8': 'August',
                    '9': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'},
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
                    'Tim Burton': 'Tim Burton',
                    'John Carpenter': 'John Carpenter',
                    'Wes Craven': 'Wes Craven',
                    'Brian De Palma': 'Brian De Palma',
                    'Directors': 'Directors',
                    'Clint Eastwood': 'Clint Eastwood',
                    'Renny Harlin': 'Renny Harlin',
                    'Walter Hill': 'Walter Hill',
                    'Ron Howard': 'Ron Howard',
                    'Spike Lee': 'Spike Lee',
                    'Barry Levinson': 'Barry Levinson',
                    'Garry Marshall': 'Garry Marshall',
                    'Sam Raimi': 'Sam Raimi',
                    'Rob Reiner': 'Rob Reiner',
                    'Ivan Reitman': 'Ivan Reitman',
                    'Joel Schumacher': 'Joel Schumacher',
                    'Martin Scorsese': 'Martin Scorsese',
                    'Ridley Scott': 'Ridley Scott',
                    'Tony Scott': 'Tony Scott',
                    'Steven Soderbergh': 'Steven Soderbergh',
                    'Steven Spielberg': 'Steven Spielberg',
                    'Oliver Stone': 'Oliver Stone',
                    'Robert Zemeckis': 'Robert Zemeckis',
                    'Other': 'Other'},
                placeholder='Select the director'))
    ]),
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Writer')),
    dbc.Col(dcc.Dropdown(id='writer',
            options = {
                'Woody Allen': 'Woody Allen',
                'Luc Besson': 'Luc Besson',
                'John Carpenter': 'John Carpenter',
                'Michael Crichton': 'Michael Crichton',
                'Joel Coen': 'Joel Coen',
                'Wes Craven': 'Wes Craven',
                'Brian Helgeland': 'Brian Helgeland',
                'John Hughes': 'John Hughes',
                'Stephen King': 'Stephen King',
                'Ehren Kruger': 'Ehren Kruger',
                'David Mamet': 'David Mamet',
                'Robert Rodriguez': 'Robert Rodriguez',
                'William Shakespeare': 'William Shakespeare',
                'M. Night Shyamalan': 'M. Night Shyamalan',
                'Kevin Smith': 'Kevin Smith',
                'Quentin Tarantino': 'Quentin Tarantino',
                'Leigh Whannell': 'Leigh Whannell',
                'Other': 'Other'},
            placeholder='Select the writer')),
    ]), 
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Production Company')),
    dbc.Col(dcc.Dropdown(id='company',
            options = {
                'Columbia Pictures':'Columbia Pictures',
                'Metro-Goldwyn-Mayer (MGM)':'Metro-Goldwyn-Mayer (MGM)',
                'New Line Cinema':'New Line Cinema',
                'Paramount Pictures':'Paramount Pictures',
                'Touchstone Pictures':'Touchstone Pictures',
                'Twentieth Century Fox':'Twentieth Century Fox',
                'Universal Pictures':'Universal Pictures',
                'Walt Disney Pictures':'Walt Disney Pictures',
                'Warner Bros.':'Warner Bros.',
                'Other':'Other'},
            placeholder='Select the company')),
    ]), 
    html.Br(),
    dbc.Row([
    dbc.Col(html.Label(children='Lead Actor')),
    dbc.Col(dcc.Dropdown(id='actor',
            options = {
                'Ben Affleck': 'Ben Affleck',
                'Christian Bale': 'Christian Bale',
                'Jeff Bridges': 'Jeff Bridges',
                'Sandra Bullock': 'Sandra Bullock',
                'Nicolas Cage': 'Nicolas Cage',
                'Jim Carrey': 'Jim Carrey',
                'George Clooney': 'George Clooney',
                'Kevin Costner': 'Kevin Costner',
                'Tom Cruise': 'Tom Cruise',
                'John Cusack': 'John Cusack',
                'Matt Damon': 'Matt Damon',
                'Johnny Depp': 'Johnny Depp',
                'Robert De Niro': 'Robert De Niro',
                'Leonardo DiCaprio': 'Leonardo DiCaprio',
                'Robert Downey Jr.': 'Robert Downey Jr.',
                'Clint Eastwood': 'Clint Eastwood',
                'Will Ferrell': 'Will Ferrel',
                'Harrison Ford': 'Harrison Ford',
                'Richard Gere': 'Richard Gere',
                'Mel Gibson': 'Mel Gibson',
                'Tom Hanks': 'Tom Hanks',
                'Dwayne Johnson': 'Dwayne Johnson',
                'Steve Martin': 'Steve Martin',
                'Matthew McConaughey': 'Matthew McConaughey',
                'Eddie Murphy': 'Eddie Murphy',
                'Liam Neeson ': 'Liam Neeson ',
                'Al Pacino': 'Al Pacino',
                'Brad Pitt': 'Brad Pitt',
                'Keanu Reeves': 'Keanu Reeves',
                'Adam Sandler': 'Adam Sandler',
                'Arnold Schwarzenegger': 'Arnold Schwarzenegger',        
                'Sylvester Stallone': 'Sylvester Stallone',
                'Will Smith': 'Will Smith',
                'Ben Stiller': 'Ben Stiller',
                'Meryl Streep': 'Meryl Streep',
                'John Travolta': 'John Travolta ',
                'Mark Wahlberg': 'Mark Wahlberg',
                'Denzel Washington': 'Denzel Washington',
                'Robin Williams': 'Robin Williams',
                'Bruce Willis': 'Bruce Willis',
                'Other': 'Other'},
            placeholder='Select the lead actor')),
    ]), 
    html.Br(),  
    html.Br(),              
    dbc.Row([
        dbc.Col(html.Label(children='Nominations Won by Lead Actor')),
        dbc.Col(dcc.Slider(id='nominations', min=0, max=25, value=0, step=1,
                            marks={
                                0: {'label': '0'},
                                5: {'label': '5'},
                                10: {'label': '10'},
                                15: {'label': '15'},
                                20: {'label': '20'},
                                25: {'label': '25'},
                            },
                            tooltip={'placement': 'bottom', 'always_visible': True})),
    ]),
    html.Br(),  
    html.Br(),              
    dbc.Row([
        dbc.Col(html.Label(children='Awards Won by Lead Actor')),
        dbc.Col(dcc.Slider(id='awards', min=0, max=5, value=0, step=1,
                            # marks={
                            #     0:{'label': '0'},
                            #     5:{'label': '5'},
                            # },
                            tooltip={'placement': 'bottom', 'always_visible': True})),
    ]),
    html.Br(),        
    html.Br(),        
    dbc.Row([
        dbc.Col(html.Label(children='Age of Lead Actor')),
        dbc.Col(dcc.Slider(id='age', min=0, max=100, value=0, step=1,
                            marks={
                                0:{'label': '0'},
                                25:{'label': '25'},
                                50:{'label': '50'},
                                75:{'label': '75'},
                                100:{'label': '100'}
                            },
                            tooltip={'placement':'bottom', 'always_visible': True})),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Select the Budget Amount (USD$)')),
        dbc.Col(dcc.Slider(id='budget', min=0, max=400000000, value=0, 
                            step=1000000,
                            marks={
                                0:{'label': '0'},  
                                100000000:{'label': '100M'},
                                200000000:{'label': '200M'},
                                300000000:{'label': '300M'},
                                400000000:{'label': '400M'},
                            
                            },
                            tooltip={'placement':'bottom', 'always_visible': True})),
    ]),
    html.Br(), 
    html.Br(),               
    dbc.Row([
        dbc.Col(html.Label(children='Runtime (Minutes)')),
        dbc.Col(dcc.Slider(id='runtime', min=0, max=300, value=0, step=1,
                            marks={
                                0:{'label': '0'},
                                100:{'label': '100'},
                                200:{'label': '200'},
                                300:{'label': '300'}
                            },
                            tooltip={'placement':'bottom', 'always_visible': True})),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color='primary')
    ]),
    html.Br(),
    # dbc.Row([html.Div(id='prediction-output')])
    html.Center(
    html.Div([
        html.H1(id='prediction-output', style={'color': 'black'})
    ]))
    ])


@callback(Output(component_id='prediction-output', component_property='children'),
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
                Input(component_id='submit-val', component_property='n_clicks'),
                )

def update_result( rating, genre, release_month, release_dow, director,
                    writer, company, actor, nominations, awards, age, budget, runtime, n_clicks):

    if n_clicks > 0:

        prediction = encode(rating, genre, release_month, release_dow, director, writer, company, actor, nominations, awards, age, budget, runtime)
            
        prediction = int(prediction)
    
        return f"The predicted gross revenue is: ${prediction:,.2f}"
    