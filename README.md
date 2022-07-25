# Project II - Web scraping and merging Dataframes
​
## Premise
​
It is January 2023 and we continue to be in the middle of an all-out war between Russia and Ukraine. Northern African and Middle East nations are suffering unparalled starvation as their food supply is stockpilled throughout Ukraine and rotting. The Black Sea continues to be heavily guarded by Turkey and the stand-off between Ukraine's Army and its underwater mines, and Russia's unrivaled Navy at bay is still ongoing.

I am hired as an external consultant Data Analyst for an International Affairs Panel on the topic immigration policies for the United Nations. They show a special interest on how developped nations can solve their long term issues included but not limited to: low fertility rates, population pyramid inversion and crippling pension debt. Therefore, they want to know how might new immigration policies impact their countries existing infraestructure, as they prepare to receive refugees by the millions.
​
## Hypothesis
​
My educated guess is that immigration, with the right policies, can solve the demographic dilemma in developped Nations.
The demographic dillema is the situation where the rate of a country's growth is inversely proportional to its population fertility rate, which depicts a grim future for developped nations.

In addition, fertility rates which are lower than 2 means that the difference in births and deaths would produce population declines and substantial increases in average ages, both of which could disrupt labor markets, threaten the fiscal sustainability of pension systems, as well as slow down economic growth, unless total net immigration offsets such declines.

Hence, I believe that not only would it be benefitial for a developped nation to adopt the right immigration policies for its prosperity and economic growth, but also it is imperative for a developped nation's survival, as these population trends transcend culture and geography, they are intrinsic to Humankind.
​
## Project files
​
The main directory has 3 subdirectories:
· Input: Hidden in GitHub, the input folder holds the data used to analyze the hypothesis. It is a file containing most recorded shark attacks (anywhere in the world and as far back in time as Ancient Greece). The file can be downloaded and seen at https://www.kaggle.com/teajay/global-shark-attacks
· Output: Contains files created from the original data (new datasets, plots, etc.) that are used multiple times through the project.
· src: Contains python files with all functions created specifically for this analysis.

​
In the root directory there are 4 Jupyter Notebook files that include all the code used in the project:
* "Exploratory data analysis" (EDA): This file explores the data (how much data there is, how is it organized and the quality of it).
* Cleaning: This file gets rid of some of the data that will not be used and standarize the way that the data is written so it is easier to work with later. The data is also categorized more efficiently.
* Analysis: It checks whether the hypothesis is true or not.
* Visualization: The last file is used to create plots that help visualize the data in order to check the hypothesis and a small market analysis in case the company decides to move forward with its project.
​
## Conclusion
​
The persistent historical trends mentioned have inescapable consequences in terms of population. Between 1950 and 2010, the populations of the rich regions of the North increased through net immigration, and since 1990 immigration has been the North’s primary source of population growth. In Europe, immigration accounted for 80 percent of the population growth between 2000 and 2018, while in North America, it constituted 32 percent in that same period.

The bottom line is that only net immigration can ensure population stability or growth in the aging advanced economies of the North—and this will happen only if we promote forward-looking immigration policies that allow larger numbers of immigrants and consider their long-run impact, rather than focusing only on the short-term calculations of their (mostly political) costs.





The data concludes that 

Net Migration Rate (N)

N = 1000 x (I - E) / P
N: Net migration rate per 1000 people.
I: Number of people immigrating into the country.
E: Number of people emmigrating out of the country.
P: Estimated mid-year population.

An excess of persons entering the country is referred to as net immigration (e.g., 3.56 migrants/1,000 population); an excess of persons leaving the country as net emigration (e.g., -9.26 migrants/1,000 population). The net migration rate indicates the contribution of migration to the overall level of population change. The net migration rate does not distinguish between economic migrants, refugees, and other types of migrants; nor does it distinguish between lawful migrants and unlawful migrants.

Pending:

Importing and actually using the functions in the python file

Dictionary for continents and worlds.

Data correlation
net migration vs fertility
heatmap
graphs
Clear graphs
hide folders and gitignore

​
## Considerations and limitations
​
This analysis was carried out on data updated on the 21st century. I have selected 205 countries and discarded 35 countries by lack of data (8 values minimum in a row) <15% of the total, which does not affect the Hypothesis nor the Conclusion. By the end of the year 2022, Net Migration rates will be considerible different in Europe as more Ukrainians continue to leave their country.