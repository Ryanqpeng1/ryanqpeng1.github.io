#### PostFix Calculator Lab

Our goal for this lab was to take a calculate_me.csv file with a list of lists of numbers and operations (+,-,*) in postfix format and make a program that could both evaluate the output for each row with postfix calculations and then compute the final average of all of the rows' outputs. To do this, I first used a list reader to organize the data into a list of lists, where each row of the list is a list in postfix format that will be evaulated to a single number. After this, I made two functions:

1. evaluate
    This method takes a list (intended to be a list of operations and numbers in postix format) and calculates the final output of the list. It does this with a stack: stacks are useful for evaluating postfix numbers because of the first-in first-out structure. Postfix calculations require the program to calculate the resulting output of two numbers after it detects an operation (i.e [6, 9, +] would evaluate to 6+9), so after finding an operation, it then needs to access the two numbers that came immediately before it. This is where a stack becomes useful: by pushing numbers into the stack until it finds an operation, the program can then remember and pop out the two most recent numbers (the two numbers at the top of the stack), perform the operation it had detected with those two numbers, and then push the calculated number back into the stack. This avoids any index issues that a list would have, because a stack automatically pop out the most recent number, which is what a post-fix calculator wants. My evaluation function does exactly this: it iterates through the list, adding any numbers it detects to the stack, and once it finds an operation, it stores the most recent two numbers in temporary variables while popping them out of the stack, then performs the corresponding operation with the two numbers and then pushes that result back into the stack. It then proceeds to add more numbers until it finds another operation and then repeats. I had to hardcode each operation because I am not familiar with any easy ways to turn strings such as "+" to operations, since you can't just cast strings to operations.

    ![](https://cdn.discordapp.com/attachments/580924483884417064/773320489200386068/unknown.png)

2. getAverage
    This method takes a list of numbers and returns the average of its elements by adding all of the elements together and dividing by the length. 
    
By calling the evaluate method on each row of the data, appending the results into another array, and then getting the average of the array, we can find the average of all of the post-fix values for each row in the data, which is 529.91.

I had a lot of fun with this lab! I didn't have any significant challenges besides having some issues locating my Stack class within my computer, so I pasted the Stack class into the file so I could use it without importing it. I also added a getList method to my stack class to make checking my final results easier.

