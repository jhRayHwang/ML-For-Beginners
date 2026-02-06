# Load the hotel reviews from CSV
from itertools import count
import pandas as pd
import time
# importing time so the start and end time can be used to calculate file loading time
print("Loading data file now, this could take a while depending on file size")
start = time.time()
# df is 'DataFrame' - make sure you downloaded the file to the data folder
df = pd.read_csv('6-NLP/data/Hotel_Reviews.csv')
end = time.time()
print("Loading took " + str(round(end - start, 2)) + " seconds")

#Print out the shape of the data frame you have just loaded (the shape is the number of rows and columns)
print(df.shape)
#Calculate the frequency count for reviewer nationalities:
#How many distinct values are there for the column Reviewer_Nationality and what are they?
print(df['Reviewer_Nationality'].nunique())
#What reviewer nationality is the most common in the dataset (print country and number of reviews)?
print(df['Reviewer_Nationality'].value_counts())
#What are the next top 10 most frequently found nationalities, and their frequency count?
nationality_freq = df['Reviewer_Nationality'].value_counts()
print(nationality_freq.head(11))
# What was the most frequently reviewed hotel for the top 10 nationalities
# Normally with pandas you will avoid an explicit loop, but wanted to show creating a new dataframe using criteria (don't do this with large amounts of data because it could be very slow)
for nat in nationality_freq[:10].index:
   # First, extract all the rows that match the criteria into a new dataframe
   nat_df = df[df["Reviewer_Nationality"] == nat]   
   # Now get the hotel freq
   freq = nat_df["Hotel_Name"].value_counts()
   print("The most reviewed hotel for " + str(nat).strip() + " was " + str(freq.index[0]) + " with " + str(freq[0]) + " reviews.") 
#How many reviews are there per hotel (frequency count of hotel) in the dataset?
# First create a new dataframe based on the old one, removing the uneeded columns
hotel_freq_df = df.drop(["Hotel_Address", "Additional_Number_of_Scoring", "Review_Date", "Average_Score", "Reviewer_Nationality", "Negative_Review", "Review_Total_Negative_Word_Counts", "Positive_Review", "Review_Total_Positive_Word_Counts", "Total_Number_of_Reviews_Reviewer_Has_Given", "Reviewer_Score", "Tags", "days_since_review", "lat", "lng"], axis = 1)

# Group the rows by Hotel_Name, count them and put the result in a new column Total_Reviews_Found
hotel_freq_df['Total_Reviews_Found'] = hotel_freq_df.groupby('Hotel_Name').transform('count')

# Get rid of all the duplicated rows
hotel_freq_df = hotel_freq_df.drop_duplicates(subset = ["Hotel_Name"])
print(hotel_freq_df) 
# While there is an `Average_Score` for each hotel according to the dataset, 
# you can also calculate an average score (getting the average of all reviewer scores in the dataset for each hotel)
# Add a new column to your dataframe with the column header `Calc_Average_Score` that contains that calculated average. 
df['Calc_Average_Score'] = round(df.groupby('Hotel_Name').Reviewer_Score.transform('mean'), 1)
# Add a new column with the difference between the two average scores
df["Average_Score_Difference"] = df.apply(get_difference_review_avg, axis = 1)
# Create a df without all the duplicates of Hotel_Name (so only 1 row per hotel)
review_scores_df = df.drop_duplicates(subset = ["Hotel_Name"])
# Sort the dataframe to find the lowest and highest average score difference
review_scores_df = review_scores_df.sort_values(by=["Average_Score_Difference"])
print(review_scores_df[["Average_Score_Difference", "Average_Score", "Calc_Average_Score", "Hotel_Name"]])
# Do any hotels have the same (rounded to 1 decimal place) `Average_Score` and `Calc_Average_Score`?

# Continue from here
df.columns