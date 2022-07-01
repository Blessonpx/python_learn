import pandas as pd
import numpy as np
# https://www.w3resource.com/python-exercises/pandas/index-data-series.php
#See as series
x=pd.Series([1,2,3,4,5])
print(x,type(x))
#Series to list
print(x.tolist(), type(x.tolist()))
# add/subtrat/divide/multiply
a=pd.Series([2, 4, 6, 8, 10])
b=pd.Series([1, 3, 5, 7, 9])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# Compare element
print(a==b)
#Dict to series
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
new_series = pd.Series(d1)
print(new_series)
#numpy array to series
np_array = np.array([10, 20, 30, 40, 50])
print(pd.Series(np_array))
# Change Datatype to numeries for series
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print(pd.to_numeric(s1, errors='coerce'))
# Dataframes' first column to series
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
s1 = df.iloc[:,0]
print(s1)
# Series to Array 
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
a = np.array(s1.values.tolist())
print(a)
# Series of Series
s = pd.Series([ ['Red', 'Green', 'White'],['Red', 'Black'],['Yellow']])
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)
# Sort values in series
s = pd.Series(['100', '200', 'python', '300.12', '400'])
new_s = pd.Series(s).sort_values()
print(new_s)
# add new Values
new_s = s.append(pd.Series(['500', 'php']))
print(new_s)
# Create a subset from a series
s = pd.Series([0, 1,2,3,4,5,6,7,8,9,10])
new_s=s[s<=6]
print(new_s)
# Change sequence of Index of series
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
s = s.reindex(index = ['B','A','C','D','E'])
print(s)
# Show mean and standard deviation 
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print(s.mean())
print(s.std())
# series of elemenet presetnin in but not in other
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
result = sr1[~sr1.isin(sr2)]
print(result)
# Series of element not common in either of the 2 series
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]
print(result)
# Print Minimum, 25th percentile, median, 75th, and maximum of a given series
num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))
print("Original Series:")
print(num_series)
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])
print(result)
# Print frequncy of each unique element
num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
result = num_series.value_counts()
print(result)
# display most frequent value in a given series and replace everything else as ‘Other’ in the series.
np.random.RandomState(100)
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Top 2 Freq:", num_series.value_counts())
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print(num_series)
#  find the positions of numbers that are multiples of 5 of a given series.
num_series = pd.Series(np.random.randint(1, 10, 9))
result = np.where(num_series % 5==0)
print(result)
# Take elements at given locations
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
result = num_series.take(element_pos)
print(result)
#  get the positions of items of a given series in another given series.
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
result = [pd.Index(series1).get_loc(i) for i in series2]
print(result)
# convert the first and last character of each word to upper case in each word of a given series
series1 = pd.Series(['php', 'python', 'java', 'c#'])
result = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print(result)
# compute difference of differences between consecutive numbers of a given series.
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])
print(series1.diff().tolist())
print(series1.diff().diff().tolist())
# to convert a series of date strings to a timeseries 
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print(pd.to_datetime(date_series))
# get the day of month, day of year, week number and day of week from a given series of date strings
from dateutil.parser import parse
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
date_series = date_series.map(lambda x: parse(x))
print(date_series.dt.day.tolist())
print(date_series.dt.dayofyear.tolist())
print(date_series.dt.weekofyear.tolist())
print(date_series.dt.weekday.tolist())
print(date_series.dt.isocalendar().week.tolist() )
######
# Series.dt.weekofyear and Series.dt.week have been deprecated. Please use Series.dt.isocalendar().week instead.
######

# convert year-month string to dates adding a specified day of the month.
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
result = date_series.map(lambda d: parse('11 ' + d))
print(result)

# filter words from a given series that contain atleast two vowels
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
result = mask = color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(color_series[result])
#  compute the Euclidean distance between two given series
x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(np.linalg.norm(x-y))
# to find the positions of the values neighboured by smaller values on both sides in a given series
nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)
# replace missing white spaces in a given string with the least frequent character.
str1 = 'abc def abcdef icd'
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)
#  compute the autocorrelations of a given numeric series
num_series = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))
print(num_series)
autocorrelations = [num_series.autocorr(i).round(2) for i in range(11)]
print(autocorrelations[1:])
#  create a TimeSeries to display all the Sundays of given year.
result = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print(result)
# convert given series into a dataframe with its index as another column on the dataframe.
char_list = list('ABCDEFGHIJKLMNOP')
num_arra = np.arange(8)
num_dict = dict(zip(char_list, num_arra))
num_ser = pd.Series(num_dict)
df = num_ser.to_frame().reset_index()
print(df.head())
# stack two given series vertically and horizontally
series1 = pd.Series(range(10))
series2 = pd.Series(list('pqrstuvwxy'))
print(series1)
print(series2)
series1.append(series2)
df = pd.concat([series1, series2], axis=1)
print(df)
# find the index of the first occurrence of the smallest and largest value of a given series
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print(nums)
print(nums.idxmin())
print(nums.idxmax())

# check inequality over the index axis of a given dataframe and a given series
df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None]) 
print(df_data)
print(sr_data)
print(df_data.ne(sr_data, axis = 0))
