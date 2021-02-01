####Visualization Lab


For this lab, I chose to use the COVID-19 vaccination data set. The specific subset of data and relationships I investigated was the daily COVID vaccinations per million for 5 different countries, USA, China, Israel, Canada, and England, over time. The dates in the csv of the data were already sorted from earliest to latest data within each country, so by filtering the data set by country, graphing the dates vs. daily vaccinations in each country allowed me to visualize the daily vaccinations per country over time. By plotting the five lines (one per country) on the same graph, I can both directly compare the daily vaccinations per million for each country with each other and analyze how the dependent variable changed over the course of the month-long period.

This graph shows the daily vaccinations per million of the five different countries. The lines are color coded as:

Red: Israel
Green: USA
Blue: England
Purple: Canada
Orange: China. 

![](https://cdn.discordapp.com/attachments/580924483884417064/805641627695448074/Combined_aod_data.png)

From this graph, we can infer that, on aerage, the order of daily vaccinations per million from least to greatest is China, Canada, England, USA, Israel. Using the pandas mean and means functions and comparing the outputs confirms this order, since there aren't any significant or obvious outliers that would skew the mean/median. 

One interesting thing to note about the graphs is that, for every country besides Israel, the daily vaccinations per million steadily increase over time. For Israel, it fluctuates between going up and down despite having the highest average (median and mean) daily covid vaccinations per million. Comparing the standard deviation of Irsael's daily vaccinations per million to the other countries confirms this observation: Israel's standard deviation for daily COVID vaccinations per million is 5.0114e+03, which is over 3 times greater than the next greatest standard deviation, England (1.5e+03). Even when considering Israel's greater center of data, its standard deviation is still far greater than any other countries, meaning a greater variance in the data points (which is evident from the visualization).

From this visualization, we can conclude that each of these five countries has increased their daily covid vaccinations per million over time (due to their positive correlations). However, Israel's vaccinations have fluctuated, with a sudden decrease before rising again, leading to greater variance. In addition, we can compare the center of the data for each country to make a claim on ordering the average daily covid vaccinations per million for each country, which is China, Canada, England, USA, Israel from least to greatest. 