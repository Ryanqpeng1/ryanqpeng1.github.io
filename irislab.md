
####Iris Lab

Our goal for this lab was to process information from a data set of three different species Iris flowers and determine which species had the greates petal length and sepal with. To do this, I first used a dictionary reader to organize the data into a list of dictionaries, which each row of the list being a dictionary containing the measurements and species for an individual flower. After this, I made three functions:

1. convertDict 
    This method takes a category and list, and returns a dictionary with three keys. Each key in the dictionary wis one of the three species of Iris flower, and has a list of all of the corresponding measurements of the given category (i.e if the category was sepal-width, the method returns a dictionary with a list of all of the sepal-widths for each species). Since the original measurements from the data set are strings, they were casted to floats. The list parameter is intended to be the list of dictionaries created by the dicitonary reader reading the original data set. 
![](https://cdn.discordapp.com/attachments/580924483884417064/764521360478175232/Screen_Shot_2020-10-10_at_12.04.35_PM.png)
2. averagesDict
    This method takes a dictionary as its parameter, which is intended to be one of the dictionaries created by the convertDict method above. All it does is take the list of the measurements for each of the keys (each of the species), and calculates the average of each of the measurements. It then returns a dictionary, where instead of a list of measurements for each species, it returns the average of the measurements for each species. 
![](https://cdn.discordapp.com/attachments/580924483884417064/764521336159600640/Screen_Shot_2020-10-10_at_12.04.43_PM.png)
3. findGreatest
    This method takes a dictionary, which is intended to be one of the dictionaries from the averagesDict methods, compares the averages for each of the species, and returns the species with the greatest average.
![](https://cdn.discordapp.com/attachments/580924483884417064/764521311783354418/Screen_Shot_2020-10-10_at_12.04.50_PM.png)

These three methods together allows us to find the species with the greatest average measurement for any given category. We first call the convertDict method on the original data set with the 'sepal-width' category, and put that dictionary through the averagesDict method, and then put the dictionary that returns through the findGreatest method to get the species with the greatest average sepal-width. The same process is repeated for petal-length. 

I found that the species with the greatest average sepal width is Iris-Setosa at 3.418, and the species with the greates average petal width is Iris-virginica at 5.552.

I really enjoyed working on this lab. I originally wrote the code to specifically look for the petal-length rather than in functions, but convereting the code to three functions made repeating the process for the sepal-width much more efficient. One error I had was that the original data had to be cast to a list after being processed from the original file with dictReader to be used in a function multiple times, which I did not originally do. 
