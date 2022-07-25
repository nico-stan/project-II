# Project II - Web scraping and merging Dataframes

<p align="center">
<img src="https://www.memecreator.org/static/images/memes/5425681.jpg" width="375" height="231" />
</p>

​
## Premise
​
It is January 2023 and we continue to be in the middle of an all-out war between Russia and Ukraine. Northern African and Middle East nations are suffering unparalleled starvation as their food supply is stockpiled throughout Ukraine and rotting. The Black Sea continues to be heavily guarded by Turkey and the stand-off between Ukraine's Army and its underwater mines, and Russia's unrivaled Navy at bay is still ongoing.
 
I am hired as an external consultant Data Analyst for an International Affairs Panel on the topic immigration policies for the United Nations. They show a special interest on how developed nations can solve their long term issues included but not limited to: low fertility rates, population pyramid inversion and crippling pension debt. Therefore, they want to know how might new immigration policies impact their countries existing infrastructure, as they prepare to receive refugees by the millions.
 
​
## Hypothesis
​
My educated guess is that immigration, with the right policies, can solve the demographic dilemma in developed Nations.
The demographic dilemma is the situation where a country's Human Development Index and Life expectancy is inversely proportional to its population fertility rate, which depicts a grim future for developed nations.
 
In addition, fertility rates which are lower than 2 means that the difference in births and deaths would produce population declines and substantial increases in average ages, both of which could disrupt labor markets, threaten the fiscal sustainability of pension systems, as well as slow down economic growth, unless total net immigration offsets such declines.
 
Hence, I believe that not only would it be beneficial for a developed nation to adopt the right immigration policies for its prosperity and economic growth, but also it is imperative for a developed nation's survival, as these population trends transcend culture and geography, they are intrinsic to Humankind.
 
​
## Analysis
​
### Why would we care?
In a nutshell, we are like the violinists at Titanic, continuing to live our normal lives while our economic and wellness structure crumbles beneath our feet.

Despite the world continuing to grow in population, it does so in an uneven manner where every Nation, regardless of circumstances, once it reaches a certain level of development, its fertility rates becomes stagnant and average lifespan increases.

Subsequently, Nations reach an inflexion point when fertility rates average <2 as this means the population will shrink and the implications that may have on pension funds and social security, as it will become unsustainable.

Therefore, we can look at immigration policies, especially for younger people as one of the solutions to the demographic dilemma.

In this sense, we aim to better understand the world's data from the 21st century to see how may Fertility rates and Net Migration rates be related.

For correlations we will be considering r>=0.85

<p align="center">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure2.png" />
</p>

<p align="center">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure3.png" />
</p>

 
 
## Conclusion
​
The persistent historical trends mentioned have inescapable consequences in terms of population. Between 1950 and 2010, the populations of the rich regions of the North increased through net immigration, and since 1990 immigration has been the North’s primary source of population growth. In Europe, immigration accounted for 80 percent of the population growth between 2000 and 2018, while in North America, it constituted 32 percent in that same period.
 
The bottom line is that only net immigration can ensure population stability or growth in the aging advanced economies of the North—and this will happen only if we promote forward-looking immigration policies that allow larger numbers of immigrants and consider their long-run impact, rather than focusing only on the short-term calculations of their (mostly political) costs.
 
The data concludes that
 
​
## Considerations and limitations
​
This analysis was carried out on data updated in the 21st century. I have selected 204 countries and discarded 28 countries by lack of data (8 values minimum in a row) -12% of the total, which does not affect the Hypothesis nor the Conclusion. By the end of the year 2022, Net Migration rates will be considerably different in Europe as more Ukrainians continue to leave their country. The data is static as has been taken from 21st century data sources in a given point of time.
 
​
## Project files
​
The main directory has 3 subdirectories:
· Input: Holds the data used to analyze the hypothesis. It is a folder with multiple files which are then merged into a single dataframe in the Output folder df_clean.
· Output: Contains the df created from the original data, and a folder named images with the figures that are used multiple times through the project.
· src: Contains python files with all functions created specifically for this analysis.
· README: This file works both as a report and a presentation tool for the project
​
In the root directory there are 2 Jupyter Notebook files that include all the code used in the project:
· "Exploratory data analysis" (EDA): This file explores the data (how much data there is, how is it organized and the quality of it). This file also scrapes information from wikipedia on Net Migration by country and merges all input files into a single dataframe.
· Plotting: This file is used to create plots that help visualize the data in order to check if the hypothesis is true.
​
 
​
## Annex
​
**Sex-ratio (ratio)**
Male/Female ratio over 100 people in a given year and country.
 
**Fertility (rate)**
The total fertility rate of a population is the average number of children that would be born to a woman over her lifetime if: 
(1) She were to experience the exact current age-specific fertility rates through her lifetime.
(2) She were to live from birth until the end of her reproductive life.
Notice that this rate includes both parents in the same woman.
 
**GDP per capita ($)**
Measures the annual economic output of a nation per person.
 
**Life expectancy (years)**
Average time that a person is expected to live in a given year and country.
 
**Meat consumption (kg)**
Average quantity of meat (kg) consumed per person in a given year and country.
 
**Median age (years)**
Average age of a person on a given year and country.
 
**Net Migration Rate (rate)**
The net migration rate is the difference between the number of immigrants (people coming into an area) and the number of emigrants (people leaving an area) throughout the year in a given country.
**N = 1000 x (I - E) / P**
N: Net migration rate per 1000 people.
I: Number of people immigrating into the country.
E: Number of people emigrating out of the country.
P: Estimated mid-year population.
An excess of persons entering the country is referred to as net immigration (e.g., 3.56 migrants/1,000 population); an excess of persons leaving the country as net emigration (e.g., -9.26 migrants/1,000 population). The net migration rate indicates the contribution of migration to the overall level of population change. The net migration rate does not distinguish between economic migrants, refugees, and other types of migrants; nor does it distinguish between lawful migrants and unlawful migrants.
 
**Population growth (%)**
Rate of change (increase/decrease) in the number of people in a country's population in a given year.
 
**Suicide rate (rate)**
Number of deaths per 100,000 people in a given year and country.
 
**Urbanization rate (rate)**
Average rate of change of the size of the urban population in a given year and country.
 
**Human Development Index (Index)**
The HDI is a summary composite measure of a country's average achievements in life expectancy, education (mean years of schooling completed and expected years of schooling upon entering the education system), and per capita income indicators.
