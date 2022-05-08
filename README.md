# Group_Project_May_2022 Group #6

Each year over a billion movie tickets are sold resulting in box office revenues of over $11 billion dollars (Source #1). Since it is not always guaranteed that the movie consumers spend their money on is of good quality we decided to produce a movie machine that determines expected gross revenue. This will focus on new in-theater releases & help studios find trends that can help monetize & maximize their releases. Our model will be able to input different factors including release month, budget, production company, & star power to predict a movies success with revenue. Our datasource will come from Kaggle and cover movies since 1980, including the recent pandemic release trends. The type of regression model we will consider include:Linear Regression, Lasso & Ridge Regression, Muli-Linear regression & a statsmodel Linear Regression. We will also have a front end website where users can fill out details regarding a pending release and the machine learning model should print things like expected revenue & other relevant metrics.

=================

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

**Machine Learning Model:**
SciKitLearn  will be used using a multi-linear regression model to train and test the data. We will also use a Lasso & Ridge regression model. Our output labels will be predicted gross revenue. We will also be using a fourth Linear Regression Model that's run through statsmodels instead of SciKitLearn. It reproduces the first Linear Regression model, but also provides a summary statistics table.

**Database:** We have chosen a PostgreSQL database for this project that will set locally on each of our machines. This will be important to recreate identically for each of us. We will do this by saving & outputting the commands in PostgreSQL to our shared repository. 

## References
1. https://www.the-numbers.com/market/