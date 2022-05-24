
from joblib import load
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, RobustScaler

# Create a Function to encode Dashboard inputs


def encode(rating, genre, release_month, release_dow, director, writer, company, actor, nominations, awards, age, budget, runtime):
    cleaned_movies = pd.DataFrame({"rating": rating,
                                    "genre": genre,
                                    "director": director,
                                    "writer": writer,
                                    "star": actor,
                                    "company": company,
                                    "runtime": runtime,
                                    "released_month": release_month,
                                    "adjusted_budget": budget,
                                    "weekday": release_dow,
                                    "nominations": nominations,
                                    "awards_won": awards,
                                    "star_age": age}, index=[0])
    movie_cat = cleaned_movies.dtypes[cleaned_movies.dtypes == "object"].index.tolist()
   
   
    # Create a OneHotEncoder instance

    
    enc = OneHotEncoder(sparse=False, categories = [['G', 'PG', 'PG-13', 'R'],
 ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
        'Drama', 'Horror', 'Other'],
 ['Barry Levinson', 'Brian De Palma', 'Clint Eastwood', 'Directors',
        'Garry Marshall', 'Joel Schumacher', 'Martin Scorsese',
        'Oliver Stone', 'Other', 'Renny Harlin', 'Ridley Scott',
        'Rob Reiner', 'Robert Zemeckis', 'Ron Howard', 'Spike Lee',
        'Steven Soderbergh', 'Steven Spielberg', 'Tim Burton',
        'Tony Scott', 'Walter Hill', 'Wes Craven', 'Woody Allen'],
 ['Brian Helgeland', 'David Mamet', 'Ehren Kruger', 'Joel Coen',
        'John Hughes', 'Kevin Smith', 'Leigh Whannell', 'Luc Besson',
        'M. Night Shyamalan', 'Michael Crichton', 'Other',
        'Quentin Tarantino', 'Robert Rodriguez', 'Stephen King',
        'Wes Craven', 'William Shakespeare', 'Woody Allen'],
 ['Adam Sandler', 'Al Pacino', 'Arnold Schwarzenegger',
        'Ben Affleck', 'Ben Stiller', 'Brad Pitt', 'Bruce Willis',
        'Christian Bale', 'Clint Eastwood', 'Denzel Washington',
        'Dwayne Johnson', 'Eddie Murphy', 'George Clooney',
        'Harrison Ford', 'Jeff Bridges', 'Jim Carrey', 'John Cusack',
        'John Travolta', 'Johnny Depp', 'Keanu Reeves', 'Kevin Costner',
        'Leonardo DiCaprio', 'Liam Neeson', 'Mark Wahlberg', 'Matt Damon',
        'Matthew McConaughey', 'Mel Gibson', 'Meryl Streep',
        'Nicolas Cage', 'Other', 'Richard Gere', 'Robert De Niro',
        'Robin Williams', 'Sandra Bullock', 'Steve Martin',
        'Sylvester Stallone', 'Tom Cruise', 'Tom Hanks', 'Will Ferrell',
        'Will Smith'],
['Columbia Pictures', 'Metro-Goldwyn-Mayer (MGM)',
        'New Line Cinema', 'Other', 'Paramount Pictures',
        'Touchstone Pictures', 'Twentieth Century Fox',
        'Universal Pictures', 'Walt Disney Pictures', 'Warner Bros.'],
 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday',
        'Wednesday']])

    # Fit and transform the OneHotEncoder using the categorical variable list
    encode_df = pd.DataFrame(enc.fit_transform(cleaned_movies[movie_cat]))
 

    

    # Add the encoded variable names to the dataframe
    encode_df.columns = enc.get_feature_names(movie_cat)

    # Merge one-hot encoded features and drop the originals
    cleaned_movies = cleaned_movies.merge(encode_df, left_index=True, right_index=True)
    cleaned_movies = cleaned_movies.drop(movie_cat,1)
    
    # Convert dataframe to np.array
    array = cleaned_movies.to_numpy()
    print(array)

    # Load RobustScaler parameters and apply scaler to the dataframe
    scaler = load("scaler.joblib")
    

    # Scale the data
    array_scaled = scaler.transform(array)

    

    model = load("Ridge_model.joblib")
    print(model.coef_)
    predict = model.predict(array_scaled)

    if predict > 0:
       return predict**2
    else:
       return 0