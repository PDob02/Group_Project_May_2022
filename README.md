# Group Project May 2022 Group #6
**Expected Movie Gross
 Revenue using Historical Movie Releases**

Each year over a billion movie tickets are sold resulting in box office revenues of over $11 billion dollars (Source #1). Since it is not always guaranteed that the movie consumers spend their money on is of good quality we decided to produce a movie machine that determines expected gross revenue. This will focus on new in-theater releases & help studios find trends that can help monetize & maximize their releases. Our model will be able to input different factors including release month, budget, production company, & star power to predict a movies success with revenue. Our datasource will come from Kaggle and cover movies since 1980, including the recent pandemic release trends. The type of regression model we will consider include: Linear Regression, Lasso & Ridge Regression, Multi-Linear regression & a statsmodel Linear Regression. We will also have a front end website where users can fill out details regarding a pending release and the machine learning model should print things like expected revenue & other relevant metrics.

=================
## View an In-Depth Presentation of our Project on Google Slides [Here](https://docs.google.com/presentation/d/19gyoO1Xixo4S4uNQXGSk6etrtWgv2QRmYCXpXCZC0VE/edit#slide=id.p)
=======
Roles For Segment One:
- Patrick is the Square 
- Kaiya is the Circle
- David is the Triangle
- Kylie is the X

We were each responsible for an branch during the first segment:

![](https://github.com/PDob02/Group_Project_May_2022/blob/pdobry/segment_1/Images/Git_Branches_Segment_1.png)

==================

**Communication protocols:**

We have met for both of the classes & office hours this week as well as on Tuesday, Friday, & Sunday. After our TAs approved the project on Saturday we pushed the final commits on Sunday night. We have been using Slack, Zoom, & other tools to communicate. 

### Questions we hoped to answer with the data

Based on the information provided in the data, the group would like to determine the sucess of a movie based on the following:
* Release month
* Day of the week
* Movie Director
* Main star
* Genre

**Machine Learning Model:**
SciKitLearn  will be used using a multi-linear regression model to train and test the data. We will also use a Lasso & Ridge regression model. Our output labels will be predicted gross revenue. We will also be using a fourth Linear Regression Model that's run through statsmodels instead of SciKitLearn. It reproduces the first Linear Regression model, but also provides a summary statistics table.

**Database:** We have chosen a PostgreSQL database for this project that will set locally on each of our machines. This will be important to recreate identically for each of us. We will do this by saving & outputting the commands in PostgreSQL to our shared repository. 

### Why we selected the topic.
The group chose this topic for a few different reasons.  The first reason was that there was a pretty meaningful & robust dataset. We were able to explore and discuss different possible options for our project. The data we were able to find also needed minimal cleaning to analyze and come up with an agreeable topic to discuss. The data was also meaningful enough to allow us to come up with practical and everyday uses that anyone could find useful. Movies are also a fun project and predicting the gross revenue of these movies will be something that we can enjoy during the summer blockbuster season. 

## References
1. https://www.the-numbers.com/market/

### Source of our data
[Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies). This dataset was originally web scraped from the IMDb website.  IMDb is an online database that contains information related to movies, tv series, video games, as well as streaming content. This particular dataset caught our eyes since it was robust and we could seemingly draw direct conclusions from linear regression & machine learning models.

Content
The presentation outlines the project,
including the following:
✓ Selected topic - Data analysis for Movies
✓ Reason why they selected their topic - Fun topic- we explained this in the first readme
✓ Description of their source of data- Kaggle done
✓ Questions they hope to answer with
the data - We hope to predict gross revenue as either an absolute number or a range based on different factors including leading actor/actress, release month, release month etc. This will be a handy tool for upcoming summer blockbusters. It will also help us determine which movies overperformed & underperformed based on our model. 
✓ Description of the data exploration
phase of the project - For the data exploration phase we took a dataset from Kaggle with movies that dated back to the year 1980. Additionally, we scraped actor's birthdays from wikipedia to try to find if there is a correlation between actor age & success. We scrubbed the data for missing values and loaded that data into our PostgreSQL database. 
✓ Description of the analysis phase of
the project
Slides Presentations are drafted in Google Slides. 

Main Branch All code in the main branch is productionready.
The main branch should include: ✓ All code necessary to perform
exploratory analysis - Code has been loaded into the PostgreSQL database.
✓ Some code necessary to complete the
machine learning portion of the project
README.md 

README.md must include: 

✓ Description of the communication
protocols - DONE

✓ Outline of the project (this may include
images, but should be easy to follow and
digest)
Note: The descriptions and explanations
required in all other project deliverables
should also be in your README.md as
part of your outline, unless otherwise
noted.
Individual Branches 

✓ At least one branch for each team member - Satisfied

✓ Each team member has at least four
commits for the duration of the second
segment (eight total commits per person) Yes

Team members submit the code for their machine learning model, as well as the
following:
✓ Description of preliminary data
preprocessing- For the dat preprocessing we did the following...
✓ Description of preliminary feature
engineering and preliminary feature
selection, including their decision-making
process 
✓ Description of how data was split into
training and testing sets - We used the standard train test split code for this part of the deliverable. 

✓ Explanation of model choice, including
limitations and benefits- The limitation of the linear regression are:

Team members present a fully integrated
database.
✓ Database stores static data for use
during the project 
✓ Database interfaces with the project in
some format (e.g., scraping updates the
database, or database connects to the
model) - We have scraped wikipedia primarily for actor/actresses' birthdays as we think that information will be statistically significant in our analysis 
✓ Includes at least two tables (or
collections, if using MongoDB) 
✓ Includes at least one join using the
database language (not including any
joins in Pandas) The database language we are using is SQL via PostgreSQL
✓ Includes at least one connection string 
(using SQLAlchemy or PyMongo) The connection string we are using is SQLAlchemy since our data is very tabular with only a few NaN values. We have attached an ERD snapshot below:
Note: If you use a SQL database, you
must provide your ERD with relationships

A blueprint for the dashboard is created
and includes all of the following:
✓ Storyboard on Google Slide(s) 
✓ Description of the tool(s) that will be
used to create final dashboard - One of the primary tools to create our dashboard include the DASH library in python. We also have a list of the technical installs that we are making in the technology.md file. 
✓ Description of interactive element(s) - Some of the interactive elements that we will have on our page include drop down menus, a graphical search bar, multiple pages, & the ability to hover over different parts of the dataset. 