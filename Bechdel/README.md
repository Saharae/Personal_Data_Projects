# Bechdel Test

----

## Overview
The Bechdel test is a test of women's representation in films named after cartoonist Alison Bechdel.

In order to pass the Bechdel test, a movie needs to have:
1. 2 named female characters
2. These characters need to speak to each other during the movie
3. The conversation needs to be about something other than a man

Fivethirtyeight posted an article analyzing the financial aspect of movies in relation to their Bechdel test status.
They found that movies made the same amount based on their test status, but movies that passed the Bechdel test
 were given less of a budget. 
 
I was able to find a different dataset with information about movie ratings from IMDb. 
IMDb dataset: https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+ratings.csv

Because the IMDb dataset used the same movie identifier as the 538 dataset, I was able to merge them and assess the
 movie Bechdel test status by the movie ratings. 
 

## Code + Files

Bechdel_figures: This is the iPython notebook that holds all the code and figures for this project.
It also functions as a write up of the results.

data: Folder containing the relevant datafiles  
|  
------- CPIAUCNS_inflation.csv: Inflation information used to transform the financial data.  
|  
------- movies.csv: Bechdel test dataset from 538 (https://github.com/fivethirtyeight/data/tree/master/bechdel)  
|  
------- IMDb_ratings.csv: Dataset containing all infromation about movie ratings (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset)

