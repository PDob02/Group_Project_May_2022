# Group Project May 2022 Group #6

**Expected Movie Gross Revenue using Historical Movie Releases**

Each year over a billion movie tickets are sold resulting in box office revenues of over $11 billion dollars (Source #1). Since it is not always guaranteed that the movie consumers spend their money on is of good quality we decided to produce a movie machine that determines expected gross revenue. This will focus on new in-theater releases with the objective to help studios, producers, or other industry professionals find trends that can help monetize and maximize their releases. We will create a model that will be able to take inputs including release month, budget, production company, and star power to predict whether a movie will be successful. Success is determined by gross revenue. Our datasource will come from Kaggle and cover movies released between 1980 and 2020, including the recent pandemic release trends. The type of regression models we consider using include: Linear Regression, Lasso, and Ridge Regression. We will also have a dashboard with a user interface that allows users to enter details regarding a pending release and the machine learning model will predict the movie's gross revenue. 

We chose this topic for a few different reasons. The first reason was that there was a pretty meaningful and robust dataset. We were able to explore and discuss different possible options for our project. The data we were able to find required minimal cleaning. The data was also meaningful enough to allow us to come up with practical and everyday uses that anyone could find either useful or interesting. Movies are also a fun project and predicting the gross revenue of these movies will be something that we can enjoy during the summer blockbuster season. 

## View an In-Depth Presentation of our Project on Google Slides [Here](https://docs.google.com/presentation/d/19gyoO1Xixo4S4uNQXGSk6etrtWgv2QRmYCXpXCZC0VE/edit#slide=id.p)


## View a demo of our Dashboard [Here](https://drive.google.com/file/d/1pef2VDipcpTnSwwBJgdTziZaoPFYamyA/view?usp=sharing)

# Project Outline

## Source of data

We obtained our main movie dataset from [Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies). The dataset was originally scraped from the IMDB website. IMBD is an online database that contains information related to movies, TV series, video games, as well as streaming content. This particular dataset caught our eyes because it is robust and we could seemingly draw direct conclusions from linear regression models.  

We obtained additional datasets containing the birthdates, number of nominations, and number of awards won by the lead actor/actress listed for each movie in the movie dataset. These secondary datasets were obtained by webscraping Wikipedia pages. Wikipedia is an online encyclopedia allowing free public access. Information provided by volunteers and contributors through open collaboration. The dataset containing the birthdates was obtained by a script that visited each actors' individual Wikipedia page. The second dataset, containing the Academy Award nominations and awards won for leading and supporting roles since 1927, was obtained by scraping [Academy Award Nominations](https://en.wikipedia.org/wiki/List_of_actors_with_Academy_Award_nominations#List_of_actors). 

## Data Exploration & Analysis

Initial cleaning of the movie dataset from Kaggle included removing any rows with null values. The released column contained both the date of the movie's release and the country of release. To obtain the release date only, we used the `str.replace` method and RegEx, then converted the date to the month only using pandas `dt.month`. Since the dataset contains monetary information in the budget and gross revenue columns spanning movies released from 1980 to 2020, we wanted to account for inflation. To do this, we used the `cpi.inflate` from a python library that adjusts U.S. dollars for inflation using the Consumer Price Index. 

When pulling data tables from our database, we merged the movies table with the released_dayofweek to obtain the day of week each movie was released. Additionally, we merged the actors_bday with the actor_awards table to essentially create a profile for each movie's starring actor. Since the information scraped from Wikipedia's Academy Awards included all actors who received a nomination or award since 1921, any actor who did not have a value in the actor_awards table is reasoned to have neither been nominated nor awarded and their values were filled with 0's accordingly. These two dataframes were then merged to create the final dataset including the cleaned information for movies and actors. 
Upon investigation, we removed movies with the following ratings: NC-17, Not Rated, TV-MA, Unrated, and X. These movies made up a small portion of the sample and were likely to skew our results since we were focusing on theater releases. Since some columns had numerous unique values, to prepare for the machine learning, we binned the following data: genre, director, writer, star, and company. Additionally, the purpose of obtaining the birthdate of each actor was to find their age at the time of the movie's release. We used their birthdate and the release date to find the age. The following information in our data were categorical: rating, genre, director, writer, star, company, released_month, and weekday. We used Sklearn's `OneHotEncoder` to encode these data columns so we could feed them to our model. 

## Database
We have chosen to use a PostgreSQL database for this project that will be created and maintained locally. Our database contains four tables: movies, actor_awards, actor_bday, and released_dayofweek. The movies table contains the cleaned dataset obtained from Kaggle. The actor_awards table consists of the number of Academy Award nominations and awards. This table can be merged with the movies table to determine the prominence of the movie's leading actor. The actor_bdays table contains the actors' birthdates, this is used to determine the age of the leading actor when the movie was released. Lastly, the released_dayofweek table contains the day of week that each movie from the movies table was released. 

The connection string we are using is SQLAlchemy since our data is very tabular with only a few NaN values. We did not find that it was necessary to use the MongoDB product. We have attached an ERD snapshot below:

![](https://github.com/PDob02/Group_Project_May_2022/blob/main/Images/moviesERD.png)


## Machine Learning

The features for the machine learning model were spread across four tables in the database, so SQLAlchemy was used to call and filter the tables so they could be merged into one dataframe for cleaning and preprocessing. For the data preprocessing we did the following:
  - To account for inflation, we used a lambda function to apply the Consumer Price Index (cpi) library to adjust the budget and gross revenue dollar values.
  - Columns with many unique categorical values such as writer, director, star, and company had the majority of less frequent values binned into an “Other” category to reduce the number of columns in the dataframe once encoded
  - Actor age and movie release date were used to generate a new “star_age” column with the age of the actor at the time of movie release
  - Nomination and Award columns had null values replaced with 0 to indicate the lack of actor nominations/awards
  -	Non-feature columns were dropped and columns with categorical data were encoded with OneHotEncoder so they could be input into a linear regression model
  -	Data was split into training and testing data, and feature values were scaled using a RobustScaler

After analyzing our data, we determined that the best features to include in our model would be the columns with continuous values, such as the runtime and budget (adjusted for inflation) because continuous values are more easily processed by linear regression. We also wanted continuous values that could represent the actor variable, so we generated an age feature for the actors, as well as nominations for Oscars and awards won. Finally, we chose categorical features such as rating, actor, company, and month of release because they seemed relevant, and through testing on the Linear Regression model, seemed to improve the model’s accuracy.

Data was split into training and testing data using SciKit Learn’s train_test_split() function, where the features of the model were input as the X value and the square root of the target value (adjusted gross revenue) was input as the y value. We used the square root of target value to account for the data’s strong positive skew. After the data was split, both the training and testing feature values were scaled using SciKit Learn’s RobustScaler() to account for outliers noticed during data exploration.
We chose to use a linear regression model because the target value we are trying to predict is a continuous value. The limitations of the linear regression are that it is limited to linear relationships, only looks at the mean of the dependent variable, is sensitive to outliers, and data must be independent. This mean heavy way of looking at things can easily be skewed. (Source #2)

Our model produced an r2 score of 0.58 and a mean squared error of approximately 22 million. The r2 score is commonly used to describe the accuracy of a linear regression model, and it shows how well a linear model fits a set of data. In this case, our model shows 58% of the total variance in the dependent variable was predictable from the independent variables. The mean squared error describes how close, on average, our regression line is to the original target variables. While an error of 22 million may seem alarming, the gross income variable that is being measured is commonly in the hundred-million range.


## Dashboard

We will create a multi-page dashboard using Dash, an open source library developed by Plotly. We will have one page showcasing interesting visualizations that the user can manipulate using drop down menus. The visualizations will also use hover features that allow for further exploration of the data. 
Additionally, the machine leanring page will contain multiple user inputs (rating, runtime, director, writer, budget, etc.) using either drop down menus or slider bars. The user's inputs will be fed into our machine learning model and will provide the user with a gross revenue prediction. 


## References
1. https://www.the-numbers.com/market/
2. https://sciencing.com/advantages-using-independent-group-ttest-8647277.html 
