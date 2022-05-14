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
The group chose this topic for a few different reasons.  The first reason was that there was a pretty meaningful dataset. We were able to explore and discuss different possible options for our project.
The data we were able to find also needed minimal cleaning to analyze and come up with an agreeable topic to discuss. The data was also meaningful enough to allow us to come up with practical and everyday uses that anyone could find useful.

## References
1. https://www.the-numbers.com/market/

### Source of our data
[Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies). This dataset was originally web scraped from the IMDb website.  IMDb is an online database that contains information related to movies, tv series, video games, as well as streaming content.

