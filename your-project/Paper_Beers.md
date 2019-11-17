
# How is compose the beer market?

Beers are one of the main products buy by any person in their life. Thousands of them are been sold. However, many breweries have seen a potential increase in the new category of craft beers, which they did not have any potential in the past. By this new trend builded by people how love beers and want to try others things, the market is having important change in the market and the way the production of them.

We decided to analyze in this market because all of us are fans of beers and we do love trying new types. Moreover, it is something unique due to the fact we drink them in social moments and makes thoses meeting more funny and differents each time.


### What are the main things we thought about?
 
When we start thinking about the beer market and breweries in it, we decided to put our shape in a amateur brewerer which is going to start a need business. At first we thought about the differents categories in the beer's market because we do not know which kind of beers exist. In addition, when you think about about beers, we have to know which are the competitor in the market and the quantity of breweries for categories, maybe there could be a monopole or an oligopole in some categories. 

But the most important question we did have was: Which is the main differents between the regular beers and the craft beers?
By having this important question, we decided to see how they are compose and which are the main ingredients to make them. And the main thing we were aking ourself was if there is any relation from the main characteristics 



### Exploratory Data Analysis

In the main data, we observe many tables which we are going to use the beer table with many different types of beers with their brewery and their category and their ABV (alcohol by volume), which we are going to be mainly using. We have also, a table with the categories which will help to group the beers. Moreover, we have the breweries table which let us see the main breweries in the market. 


![Table Beers Dataset](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/images_jupyter/beers_dataset.png)




And, as a second dataset, we have an API about some craft beers and regular beers with their main ABV, the SRM and EBC (which is two differents scales for the colour of the beer), PH of the beer and the temperature and duration of cooking. This API will help us identify if there is any relation between the main characteristics mixing these two sectors.




![Table Beers Dataset](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/images_jupyter/API_Structure.png)


### Main Points Observed

##### First Question:

For answering the first question, we start by finding the clusters of beers and breweries by categories to observe the highest one:

![Table Beers](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/images_jupyter/Num_beers.png)



![Table breweries](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/images_jupyter/Num_breweries.png)



As we observe, the category with more beers is the **North American Ale** with 1014, and the second (Belgian and French Ale) has only 254.

The category with more breweries is the **North American Ale** with 277 breweries, and the second one (Other Style) has 109. The Belgian and French Ale has only 35 breweries.



##### Second Question:

For looking inside the different features of the beers, we observe the next information: 

![table beers_features](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/Tableau/images/categories_beers.png)


As we observe, the different beers been group by the SRM (the colour of the beer), their main features have **aproximately the same values for all the three categories** of it. We can conclude that, between the craft and larger beers, there is not any difference we can really see. 


##### Third Question:

He start looking the main ABV of the beers categories to see the highest and the lowest, and we look the beers maximum and minimum ABV (The first grafic is from the Dataset Beers and the other two are from the API, which contains the mix beers (craft and larger).

![table categories](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/Tableau/images/categories_beers.png)

![Max_ABV](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/Tableau/images/abv_max_beers.png)


![Min_ABV](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/Tableau/images/abv_min_beers.png)

The category with the highest ABV is the **Belgian and French Ale**, follow by the Northe American Ale.

And the highest ABV beer is the **Tactical Nuclear Penguin** with 32 ABV , and the lowest are the **Petite Orval, Huckleberry Ale, Sea Dog Apricot Wheat and Sea Dog Blue Paw Wheat** with 3.5 ABV.


##### Fourth and Fifth Questions:

The main points for both question were if there is any correlation between the ABV and the SRM (colour of beer), because we though there could be some relation for the strongers beer been darker or the otherside. And the second correlation is between the ABV and the temperature of cooking.

![Correlation](https://github.com/rubenmartinezlorente/Project-Week-3-Data-Thieves/blob/master/your-project/NEW_DATA/images_jupyter/correlation.png)


From this table, we can see that there is not a correlation for both question because the first one has a correlation of 0.003290 and the other has a correlation of -0.051953. For been consider a good correlation, the result has to be between 0.6 and 0.8, and in this case, they do not overpass the 0.1.









