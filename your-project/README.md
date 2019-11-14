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

    Open Brewery: API with a directory of breweries in US, with their addresses. 
    
    https://www.openbrewerydb.org/#projects


    Punk Ipa: API with different information of beers providing: brands, description beers, food combination.
    
    https://punkapi.com/documentation/v2

Other important sources that support this analysis:

https://www.homebrewing.org/SRM-Beer-Color-Scale_ep_81-1.html#

## Database
The API from PUNKAPI, is mainly composed by different types of beer with additional information like color, alcohol by volumne, food pairings or data cooking. 

On the other side, the other datasets are formed by beer, beer's categories, breweries, style of beer, and other additional data like alcohol percentage.

## Workflow
On the first place we searched for a usable API whose information would interest us. When found, we posed the questions that interested us the most.

With those questions in mind, we explored the API in order to find the answers and tried to add complementary information that in this case we found in csv files. The csv files had to be cleaned thoroughly due to their inconsistencies. A SQL database was created in order to allow direct calling of the files from the cloud in the future.

For the sake of clarity, every question had its own Jupyter document, but a common initial code was created in order to get the data from the API or the csv files. We worked with pandas to try to obtain answers to the questions. 


## Organization
We used a Trello board with the tasks to do, the ones on the process and the pieces of work already done.

Our repository contains what follows:

QUESTIONS - With question files.
NEW DATA - Clean datasets and the Tableau data.
RAW DATA - Old data as we found it.
DATA CLEANING: A cleaning file for the csv files and the API.


## Links

[Repository](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/b/RV54bqoU/project-3-brewery-data-analysis)
[SRM](https://en.wikipedia.org/wiki/Beer_measurement)
