<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Brewerys and beers analysis
By Jordana Jordi, Martínez Rubén & Navarro Alex.

*Data Analytics, Ironhack Barcelona -20/10-21/12 2019*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Database](#database)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
In this project you will find a sample of our training to show our experience in ETL and data analysis for the Data Analytics bootcamp carried out in the Q4 of 2019.

The goal of this project is the data analysis from beer&breweries topics. We want answer some questions we made previous to have the datasets or APIs.

We find in this projects concepts of Python, Pandas, Tableau, API's and SQL.

## Questions & Hypotheses
The information we want to extract from the datasets and the API's related with beers and breweries are the followings:

1. What kind of categories of beers exists?
2. Which is the beer (and category) with more breweries?
3. What are the main differences between these beers (hop, temperatures cooking, or bitterness)?
4. What beer (and category) has the maximum ABV (alcohol graduation)? and the minimum?
5. Is there any relationship between the ABV and the SEM (color of beer)?
6. Is there any relationship between the ABV and the fermentation temperature?

## Datasets
There are three different resources (APIs and websites):

- Websites: four different databases for beers, breweries, category styles and geocodes.

    https://openbeerdb.com/

- APIs:

    Punk Api: API with different information of beers providing: brands, description beers, food combination.
    
    https://punkapi.com/documentation/v2

Other important sources that support this analysis:

https://www.homebrewing.org/SRM-Beer-Color-Scale_ep_81-1.html#

## Database
The API from PUNKAPI, is mainly composed by different types of beer with additional information like color, alcohol by volumne, food pairings or data cooking. 

On the other side, the other datasets are formed by beer, beer's categories, breweries, style of beer, and other additional data like alcohol percentage.

## Workflow
On the first place we searched for a useful API whose information be enough to answer at least, some of the interested questions. Once we found some APIs, we propose the questions more interesting.

A process of data cleaning and exploring is initiated. We need to clean the different data-set (from API and web), in order to explore and structure all legible data and answer the questions.

For the sake of clarity, every question had its own Jupyter document, but a common initial code was created in order to get the data from the API or the csv files. We worked with pandas to try to obtain answers to the questions. 


## Organization
We used a Trello board with the tasks to do, the ones on the process and the pieces of work already done.

Our repository contains the folling folder and files:

**FOLDERS**

QUESTIONS - 6 files where each  question is answered.

NEW DATA - Clean datasets with files from Tableau to make visualization plots.

RAW DATA - Datasets from the web and the API we used to make the data cleaning and exploring.

**FILES**

README.md - This file that explains a summary of the project.

API_connection.py - Python code that launch the request and save the dataset file in the repository. We make a pre-datacleaning to split up data we just can do                         from the web.

DataCleaning.ipnyb - Jupyter notebook file where we make all data cleaning and exploring to answer the questions proposed.

Paper_Beers.md - Document where we present formally the project.



## Links

[Repository](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/b/RV54bqoU/project-3-brewery-data-analysis)
[SRM](https://en.wikipedia.org/wiki/Beer_measurement)
