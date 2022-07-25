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
### Why would we care?
In a nutshell, we are like the violinists at Titanic, continuing to live our normal lives while our economic and wellness structure crumbles beneath our feet.

Despite the world continuing to grow in population, it does so in an uneven manner where every Nation, regardless of circumstances, once it reaches a certain level of development, its fertility rates becomes stagnant and average lifespan increases.

Subsequently, Nations reach an inflexion point when fertility rates average <2 as this means the population will shrink and the implications that may have on pension funds and social security, as it will become unsustainable.

Therefore, we can look at immigration policies, especially for younger people as one of the solutions to the demographic dilemma.

In this sense, we aim to better understand the world's data from the 21st century to see how may Fertility rates and Net Migration rates be related.

### Exploratory Data Analysis
204 countries are selected for this report, with columns that include a variety of quantitative data.

For correlations we will be considering r>=0.85.

**Correlations (all countries)**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure2.png" />
</p>

We can see strong correlations for:
- Life Expectancy and HDI (0.9)
- Fertility and Median Age (-0.87)
- Fertility and HDI (-0.86)
- Fertility and Life Expectancy (-0.85)

**Correlations (developed countries)**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure3.png" />
</p>
Here the most remarcable correlations is:
- Net Migration and Population Growth (0.91)

**Life Expectancy and HDI**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure13.png" />
</p>
 
**Life expectancy by Continent**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure4.png" />
</p>

**Life expectancy by Class of Country**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure5.png" />
</p>

To better understand fertility, we will consider it individually and then see how it is related to other variables.

**Fertility rate by Continent**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure6.png" />
</p>

**Fertility Rate by Continent (Boxplot)**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure15.png" />
</p>

**Fertility rate by Class of Country**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure7.png" />
</p>

**Fertility sorted by Continent and Country Class**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure14.png" />
</p>

As shown, Fertility rate has a high correlation with Median Age.

**Fertility rate vs Median Age**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure11.png" />
</p>

We can now see how Fertility rate is correlated to the Human Development Index.

**Fertility rate vs Human Development Index**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure10.png" />
</p>

**Fertility rate vs Human Development Index by Continent**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure8.png" />
</p>

**Fertility rate vs Human Development Index by Class of Country**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure9.png" />
</p>

The last strong correlation is between Fertility and Life Expectancy.

**Fertility Rate vs Life Expectancy**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure12.png" />
</p>

We can better understand the Net Migration Rate individually and then see how it related to the Population Growth in Developped Countries

**Net Migration Rate Distribution by Continent**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure16.png" />
</p>

**Net Migration Rate Distribution by Class**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure17.png" />
</p>

**Net Migration Rate vs Population Growth for Developed Countries**
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/FigureXX.png" />
</p>


## Conclusion
​
The persistent historical trends mentioned have inescapable consequences in terms of population. There is no easy fix for the demographic dillemma. However, immigration when inspected closely seems to be playing a significant role in the long term sustainability of a Country's Wellfare State.

The bottom line is that positive net immigration can ensure population stability or growth in the aging advanced economies of the developed Nations and this will happen only if we promote forward-looking immigration policies that allow larger numbers of immigrants and consider their long-run impact, rather than focusing only on the short-term calculations of their (mostly political) costs.
 

​
## Considerations and limitations
​
This analysis was carried out on data updated in the 21st century. I have selected 204 countries and discarded 28 countries by lack of data (8 values minimum in a row) -12% of the total, which does not affect the Hypothesis nor the Conclusion. By the end of the year 2022, Net Migration rates will be considerably different in Europe as more Ukrainians continue to leave their country. The data is static as has been taken from 21st century data sources in a given point of time.

### How reliable is this data?
<p align="left">
<img src="https://github.com/nico-stan/project-II/blob/main/Output/images/Figure1.png" />
</p>


​
## Project files
​
The main directory has 3 subdirectories:
- Input: Holds the data used to analyze the hypothesis. It is a folder with multiple files which are then merged into a single dataframe in the Output folder df_clean.
- Output: Contains the df created from the original data, and a folder named images with the figures that are used multiple times through the project.
- src: Contains python files with all functions created specifically for this analysis.
- README: This file works both as a report and a presentation tool for the project
In the root directory there are 2 Jupyter Notebook files that include all the code used in the project:
- "Exploratory data analysis" (EDA): This file explores the data (how much data there is, how is it organized and the quality of it). This file also scrapes information from wikipedia on Net Migration by country and merges all input files into a single dataframe.
- Plotting: This file is used to create plots that help visualize the data in order to check if the hypothesis is true.


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
