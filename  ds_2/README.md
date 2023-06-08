# Home task 2

## Part One: Getting to know Pandas
Read the data using the `read_html` method from the table "Fertility rate in the regions of Ukraine (1950-2019)" link

To do:
- Print the first rows of the table using the head method
- Determine the number of rows and columns in the dataframe (shape attribute)
- Replace the value "-" in the table with the value NaN
- Determine the types of all columns using dataframe.dtypes
- Change the types of non-numeric columns to numeric. The hint is the columns where the symbol "-" was located
- Calculate the percentage of blanks in each column (use the isn'tull and sum methods)
- Remove the data for the whole country from the table, the last row of the table
- Replace missing data in columns with the average values of these columns (fillna method)
- Get a list of regions where the birth rate in 2019 was higher than the average for Ukraine
- Which region had the highest birth rate in 2014?
- Build a bar chart of the birth rate by region in 2019

## Part two: Analyze the file
Analyze the file `2017_jun_final.csv`. The file contains the results of the June 2017 developer survey.

Required:
- Read the 2017_jun_final.csv file using the read_csv method
- Read the resulting table using the head method
- Determine the size of the table using the shape method
- Determine the types of all columns using dataframe.dtypes
- Calculate the percentage of blanks in each column (use the isn'tull and sum methods)
- Remove all columns with blanks except for the "Programming language" column
- Again, calculate the proportion of blanks in each column and make sure that only the "Programming language" column remains
- Delete all rows in the original table using the dropna method
- Define a new table size using the shape method
- Create a new table python_data, which will contain only rows with specialists who have specified the Python programming language
- Resize the python_data table using the shape method
- Using the groupby method, group by the "Position" column
- Create a new DataFrame, where for the grouped data by the "Position" column, perform data aggregation using the agg method and find the minimum and maximum values in the "Salary.in.month" column
- Create a fill_avg_salary function that returns the average salary per month. Use it for the apply method and create a new column "avg"
- Create descriptive statistics using the describe method for the new column.
- Save the resulting table to a CSV file

## Part three: Analyzing a dataset from Kaggle.com
In this part of the homework, we'll dive even deeper into the pandas library and look at more advanced features.

For this exercise, we use data on the Top 50 best-selling books on Amazon for 11 years (from 2009 to 2019). The dataset is publicly available on Kaggle.com. Download the csv file from the link and move it to the same directory as your work laptop (for convenience). After that, proceed to the assignment

To complete this part of the homework, you will not only have to write the code, but also answer the related questions. Wherever you see the answer in bold, you will need to paste the question into the file and answer it.

For example:

What library is used to work with dataframes in python? Answer: pandas

To do:
- Read the csv file (use the read_csv function)
- Print the first five lines (use the head function)
- Print the dimensions of the dataset (use the shape attribute)
- Answer: How many books does the dataset store data about?

There are 7 variables (columns) available for each of the books. Let's take a closer look at them:
- Name - the name of the book
- Author - author
- User Rating - rating (on a 5-point scale)
- Reviews - number of reviews
- Price - price (in dollars as of 2020)
- Year - year when the book was included in the Top 50 rating
- Genre - genre

To simplify our work, let's change the names of the variables a bit. As you can see, all the names here start with a capital letter, and one of them even contains a space. This is very undesirable and can be quite inconvenient. Let's change the case to lowercase and replace the space with a lowercase underscore (snake_style). And at the same time, let's learn a useful attribute of the dataframe: columns (you can simply assign a list of new names to this attribute)

`df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']`

### Initial data exploration
- Check if all rows have enough data: print the number of blanks (na) in each column (use the isna and sum functions)
- Answer: Are there any variables with missing values?
- Check for unique values in the genre column (use the unique function)
- Answer: What are the unique genres?
- Now look at the price distribution: build a chart (use kind='hist')
- Determine what is the maximum, minimum, mean, median price (use the max, min, mean, median functions)
- Answer: The maximum price?
- Answer: The minimum price?
- Answer: Average price?
- Answer: Median price?
### Search and sort data
- Answer: Which rating in the dataset is the highest? Answer:
- Answer: How many books have this rating? Answer:
- Answer: Which book has the most reviews? Answer:
- Answer: Of the books in the Top 50 in 2015, which book is the most expensive (you can use an intermediate date frame)? Answer:
- Answer: How many Fiction books were in the Top 50 in 2010 (use &)? Answer:
- Answer: How many books with a rating of 4.9 were ranked in 2010 and 2011 (use | or the isin function)? Answer:
- And finally, let's sort in ascending order of price all the books that were ranked in 2015 and cost less than $8 (use the sort_values function).
- Question: Which book is last in the sorted list? Answer:
### Aggregating data and joining tables
The last section of this homework includes more advanced functions. But don't worry, pandas makes all the operations simple and straightforward.

To begin, let's look at the maximum and minimum prices for each genre (use the groupby and agg functions, and use max and min to calculate the minimum and maximum values). Don't take all the columns, select only the ones you need
Example: The maximum price for the Fiction genre: Answer

- Answer: Minimum price for the genre Fiction: Answer
- Answer: Maximum price for the genre Non Fiction: Answer
- Answer: Minimum price for the genre Non Fiction: Answer

Now create a new dataframe that will contain the number of books for each author (use the groupby and agg functions, and use count to count the number). Don't take all the columns, just the ones you need.

- Question: What is the size of the table? Answer:
- Answer: Which author has the most books? Answer:
- Answer: How many books are there by this author? Answer:

Now create a second dataframe that will contain the average rating for each author (use the groupby and agg functions, use mean to calculate the average). Don't take all the columns, just select the ones you need

- Answer: Which author has the lowest average rating? Answer:
- Answer: What is the average rating for this author? Answer:

Join the last two dataframes so that you can see the number of books and the average rating for each author (use the concat function with axis=1). Save the result to a variable

Sort the dataframe by increasing number of books and increasing rating (use the sort_values function)

- Question: Which author is first in the list?

The work is submitted as a Jupyter file Hw2.3.ipynb

## Visualization
For each of the previous tasks:
Hw2.1.ipynb
Hw2.2.ipynb
Hw2.3.ipynb
add 3 to 5 function graphs of different types of your choice. Set the graphs to look different so that each graph in your homework is distinctive and does not look like the others. You can use either matplotlib or seaborn.

Don't forget to add the %matplotlib inline directive to the Jupyter file so that the graphs are plotted inside the document.