#### Hospital Lab

To approach this lab, I split the process into three parts, which I did within two separate python files.

1. Obtaining data server.

    I made a python file (HospitalLabQuery.py) that would print every row of the data from the server, and then piped the output of the file into a csv to be cleaned and processed in a different file (HospitalLab.py). To query the data, I used the given url, endpoint and key. I then made a query method that took in an id as a paramter and printed a row of data from the server with the given id. The query method did this by making a payload with the universal key and id parameter, and then used the requests.get method to request the data from the server with the payload. I then checked to see if the response from the server was ok (that there was no error), and if it was, I print the row of data in text form. I intentionally excluded printing an error message because I only wanted the python file to print data from the server. Because I did not know how many rows of data were in the data set on the server, I decided to test a large number (999): since the server returned an out of bounds error, I knew there were less than 999 rows of data. I then queried and printed the data for every id from 0 to 999: this guarantees that every id with a row of data will be printed. Although some of the later requests will have errors, since I excluded the error message, nothing will be printed. This ensures that the python file will print the data for every row with data from the server and nothing else. 
    ![](https://cdn.discordapp.com/attachments/478378271546015764/784555552889765938/Screen_Shot_2020-12-04_at_6.02.14_PM.png)

    I then piped the output of this python file into a csv file called hospitalllabdata.csv. I use this csv file for the next part of the lab.
    ![](https://cdn.discordapp.com/attachments/478378271546015764/784557122079686706/Screen_Shot_2020-12-01_at_7.52.32_PM.png)

2. Cleaning the data

    I first used a list reader to convert the csv of the data in the previous part to a list of lists. I used code to clean the data, and I did the cleaning and analysis of the data in the same python file. To clean the data, I decided to standardize all of the bed measures to 1000HAB. I first looked through the header row (0th index row) to get the index of the measurement and beds sections by checking the indices of the elements of the 0th row. Then, while iterating through every row of the data (besides the header/0th index) and checking what the bed measurement was, I adjusted the bed counts accordingly if they were not already 1000HAB and then changed the measurement to 1000HAB. Since all the measurements were either 500HAB, 1000HAB, or 2000HAB, I decided it would be easier to hardcode the two cases (500HAB or 2000HAB). If it was 500HAB, I doubled the bed count (i.e. 1 bed for every 500 people is the same as 2 beds for every 1000 people) and if it was 2000HAB, I halved the bed count. After standardizing the bed measures, the data was cleaned and ready to be analyzed. 

    ![](https://cdn.discordapp.com/attachments/478378271546015764/784555521364852736/Screen_Shot_2020-12-04_at_6.02.29_PM.png)

3. Analyzing the data

    The goal for this lab was to determine which county had the most hospital beds per person. Since the bed measurements were standardized, adding the bed counts for each county together and seeing which sum was the greatest yields the the county with the most hospital beds per person. Although we are technically trying to find the most hospital beds per person, since the bed measurements are standardized, the county with the greatest number of beds is also the county with the greatest number of beds per person. In order to do so, I used a dictionary. Each key represented a county, with the value for the key being the number of hospital beds. I then interated through the clean data set again. I first checked whether or not the county for the current row was already in the dictionary. If it was, I added its beds to the value of the corresponding key in the dictionary. If it wasn't in the dictionary yet, I made a new key for the county with the value being its number of beds. After going through the whole data set, the dictionary now contains every county, with the sum of its beds from each row (the total number of beds). I then found which key had the greatest value by using a temporary placeholder variable starting at -1 and iterating through the dictionary, comparing each value to the placeholder. 

    ![](https://cdn.discordapp.com/attachments/478378271546015764/784555490868592700/Screen_Shot_2020-12-04_at_6.02.35_PM.png)

I found that the county with the most hospital beds after standardizing the bed measures (and therefore the most hospital beds per person) was New York. I really enjoyed this lab! I initially had some struggles getting the data from the website and querying it properly, but I figured out what my syntax errors were after some trial and error. 


