import numpy as np
import pandas as pd

# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
pd1 = pd.Series([1, 3, 7, 8])
# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
pd_series= pd.Series([4.4, 2.4, 88.2, 1])
pd2 = pd_series.to_list()
# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]
pdlist1 = pd.Series(list1)
pdlist2 =  pd.Series(list2)
#Addition
pdlistadd = pdlist1 + pdlist2
#Substraction
pdlistsub = pdlist1 - pdlist2
#Multiplication
pdlistmul = pdlist1 * pdlist2
#Divide
pdlistdiv = pdlist1 / pdlist2
# 4.Write a Pandas program to compare the elements of the two Pandas Series.
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]
pdlist1 = pd.Series(list1)
pdlist2 =  pd.Series(list2)
# Greater than
pdcomparelist = pdlist1 > pdlist2
# Less than
pdcomparelist = pdlist1 < pdlist2
# Equal
pdcomparelist = pdlist1 == pdlist2
# 5. Write a Pandas program to convert a dictionary to a Pandas series.
orig_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
pddict = pd.Series(orig_dict)
# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
numpy_array = np.array([55.6, 87.3,123, 51.8])
numpd = pd.Series(numpy_array)
# 7. Write a Pandas program to change the data type of given a column or a Series.
pd_series = pd.Series([100, 200, 'python', 300.12, 400])
# to change a whole series
float_pd_series = pd.to_numeric(pd_series, errors='coerce')
# To change specific column
float_pd_series = pd_series.apply(pd.to_numeric, errors = "coerce")
# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.
newd = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
pddatafrme = pd.DataFrame(newd)
# Use iloc
first_series = pddatafrme.iloc[:, 0]
# Use cloumn name
first_series = pddatafrme['col1']
# 9. Write a Pandas program to convert a given Series to an array.
pd_series = pd.Series([100, 200, 'python', 300.12, 400])
array_list = pd_series.to_list()
# 10. Write a Pandas program to convert Series of lists to one Series.
pd_series = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
# Through Stack
one_series = pd_series.apply(pd.Series).stack().reset_index(drop=True)
# Through Explode 
one_series = pd_series.explode().reset_index(drop=True)
# 11. Write a Pandas program to sort a given Series.
pd_series = pd.Series(['100', '200', 'python', '300.12', '400'])
pd_sorted = pd_series.sort_values()
# 12. Write a Pandas program to add some data to an existing Series.
pd_series = pd.Series(['100', '200', 'python', '300.12', '400'])
new_list = ["500", "php"]
new_pd_series = pd.concat([pd_series, pd.Series(new_list)], ignore_index=True)
# 13. Write a Pandas program to create a subset of a given series based on value and condition.
pd_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Subset Get less than 6 values
sub_pd_series = pd_series[pd_series < 6]
# 14. Write a Pandas program to change the order of index of a given series
pd_series = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
reindex_pd_series = pd_series.reindex(index = ['B','A','C','D','E'])
# 15. Write a Pandas program to create the mean and standard deviation of the data of a given Series.
pd_series = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
# mean
pd_series_mean = pd_series.mean()
# standard deviation
pd_series_std = pd_series.std()
# 16. Write a Pandas program to get the items of a given series not present in another given series.
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
# In Series
new_sr1 = sr1[sr1.isin(sr2)]
# Not in Series
new_sr1 = sr1[~sr1.isin(sr2)]
# 17. Write a Pandas program to get the items which are not common of two given series.
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
new_sr1 = sr1[sr1.isin(sr2)]
# 18. Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])
# 19.  Write a Pandas program to calculate the frequency counts of each unique value of a given series.
pd_series = pd.Series(np.random.randint(10, size=40))
freq_pd_series = pd_series.value_counts()
# 20. Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
pd_series = pd.Series(np.random.randint(10, size=40))
freq_pd_series = pd_series.value_counts()
#top 3 frequent
top_3_freq = freq_pd_series[0:3]
# fill values with 'Other'
#freq_pd_series[3:] = 'Other'
#pd_series[~pd_series.isin(top_3_freq.index[:1])] = 'Other'
# 21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
pd_series = pd.Series([1, 2, 5, 6, 7, 8, 9, 10])
# First Method
pd_series_mul = pd_series[pd_series % 5 == 0]
mul_index = pd_series_mul.index
# Second Method
result = np.where(pd_series % 5 == 0)
# 22. Write a Pandas program to extract items at given positions of a given series.
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
result = num_series.take(element_pos)
# 23. Write a Pandas program to get the positions of items of a given series in another given series.
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
result = [pd.Index(series1).get_loc(i) for i in series2]
# 24. Write a Pandas program convert the first and last character of each word to upper case in each word of a given series.
series1 = pd.Series(['php', 'python', 'java', 'c#'])
result = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
# 25.  Write a Pandas program to calculate the number of characters in each word in a given series.
series1 = pd.Series(['php', 'python', 'java', 'c#'])
result = series1.map(lambda x: len(x))
# or
result = series1.apply(len)
# 26. Write a Pandas program to compute difference of differences between consecutive numbers of a given series.
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])
diff_list = series1.diff().tolist()
diff_diff_list = series1.diff().diff().tolist()
# 27. Write a Pandas program to convert a series of date strings to a timeseries.
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
date_series_updated = pd.to_datetime(date_series, format='mixed')
# 28. Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings.
from dateutil.parser import parse
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
date_series_parse = date_series.map(lambda x: parse(x))
day_of_month = date_series_parse.dt.day.tolist()
# 29. Write a Pandas program to convert year-month string to dates adding a specified day of the month.
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
date_series_parse = date_series.map(lambda x: parse('11 ' + x))
# 30. Write a Pandas program to filter words from a given series that contain atleast two vowels.
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
result = color_series[color_series.str.lower().apply(lambda c: sum(1 for char in c if char in 'aeiou') >= 2)]
# 31. Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series.
nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
# 32. Write a Pandas program to replace missing white spaces in a given string with the least frequent character.
str1 = 'abc def abcdef icd'
str_ser = pd.Series(list(str1))
freq_str_ser = str_ser.value_counts()
least_freq = freq_str_ser.dropna().index[-1]
new_str1 = str1.replace(" ", least_freq)
# 33. Write a Pandas program to create a TimeSeries to display all the Sundays of given year.
result = pd.Series(pd.date_range('2025-01-01', periods=52, freq='W-SUN'))
#34. 