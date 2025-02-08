import pandas as pd
import numpy as np

#1. Write a Pandas program to create a dataframe from a dictionary and display it.
sample_dict = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
sample_pd = pd.DataFrame(sample_dict)
#2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
exam_pd = pd.DataFrame(exam_data, index=labels)
# 3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
#exam_pd.info()
# 4. Write a Pandas program to get the first 3 rows of a given DataFrame.
exam_pd.head(3)
# or
exam_pd.iloc[:3]
# 5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
exam_pd[["name", "score"]]
# 6. Write a Pandas program to select the specified columns and rows from a given data frame.
# Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the data frame.
exam_pd.iloc[[0, 2, 4, 5], [0, 1]]
# 7.  Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
exam_pd[exam_pd['attempts'] > 2]
# 8. Write a Pandas program to count the number of rows and columns of a DataFrame.
#print("Number of Rows: " + str(exam_pd.shape[0]))
#print("Number of columns: " + str(exam_pd.shape[1]))
# 9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
exam_pd[exam_pd['score'].isnull()]
# 10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
exam_pd[(exam_pd['score'] >= 15) & (exam_pd['score'] <=20)]
# 11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
exam_pd[(exam_pd['attempts'] < 2) & (exam_pd['score'] > 15)]
# 12. Write a Pandas program to change the score in row 'd' to 11.5.
exam_pd.loc['d', 'score'] = 11.5
# 13. Write a Pandas program to calculate the sum of the examination attempts by the students.
exam_pd['attempts'].sum()
# 14. Write a Pandas program to calculate the mean of all students' scores.
exam_pd['score'].dropna().mean()
# 15. Write a Pandas program to append a new row 'k' to data frame with given values for each column. 
# Now delete the new row and return the original DataFrame.
exam_pd.loc['k'] = ['Suresh', 15.5, 1, 'yes']
#print(exam_pd)
new_exam_pd = exam_pd.drop('k')
# 16. Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
exam_pd_sorted = exam_pd.sort_values(['name', 'score'], ascending=[False, True])
# 17. Write a  Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
exam_pd['qualify'] = exam_pd['qualify'].map({'yes': True, 'no': False})
# 18. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
exam_pd.loc['d', 'name'] = 'New Suresh'
# 19. Write a Pandas program to delete the 'attempts' column from the DataFrame.
#del exam_pd['attempts']
# 20. Write a Pandas program to insert a new column color in existing DataFrame.
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red', 'Blue']
exam_pd['color'] = color
# 21. Write a Pandas program to iterate over rows in a DataFrame.
new_exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
new_exam_pd = pd.DataFrame(new_exam_data)
#for key, value in new_exam_pd.iterrows():
#    print(value['name'], value['score'])
# 22. Write a Pandas program to get list from DataFrame column headers.
exam_pd.columns.values
# 23. Write a Pandas program to rename columns of a given DataFrame.
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
new_data = pd.DataFrame(d)
new_data = new_data.rename(columns={'col1': 'Column 1', 'col2': 'Column 2', 'col3': 'Column 3'})
# 24. Write a Pandas program to select rows from a given DataFrame based on values in some columns.
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
new_d = pd.DataFrame(d)
new_d[new_d['col1'] == 4]
# 25. Write a Pandas program to change the order of a DataFrame columns.
new_d_column = new_d[['col3', 'col2', 'col1']]
#26. Write a  Pandas program to add one row in an existing DataFrame.
df2 = {'col1': [10], 'col2': [11], 'col3': [12]}
df2_pd = pd.DataFrame(df2)
new_d = pd.concat([new_d, df2_pd], ignore_index=True)
#27. Write a Pandas program to count city wise number of people from a given of data set (city, name of the person).
city_data = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
g1 = city_data.groupby(["city"]).size().reset_index(name="Number of People")
#27 . 
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
d_pd = pd.DataFrame(d)
d_pd.to_csv("new_file.csv", sep="\t")

# 31. Write a Pandas program to select a row of series/dataframe by given integer index.
d_pd.iloc[2]
#32. Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
exam_data_pd = pd.DataFrame(exam_data)
new_exam_data_pd = exam_data_pd.fillna(0)

#33. Write a Pandas program to convert index in a column of the given dataframe.
exam_data_pd.reset_index(level=0, inplace=True)
#34. Write a Pandas program to set a given value for particular cell in  DataFrame using index value.
exam_data_pd.iloc[8, 1] = 10.2
# 35. Write a Pandas program to count the NaN values in one or more columns in DataFrame.
exam_data_pd.isna().values.sum()
#36. Write a Pandas program to drop a list of rows from a specified DataFrame.
d_pd= d_pd.drop(d_pd.index[[2,4]])
#37. Write a Pandas program to reset index in a given DataFrame.


