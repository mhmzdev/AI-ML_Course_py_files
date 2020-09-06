import pandas as pd
import numpy as np

# df == dataframe
### CSV File reading
df = pd.read_csv('files/pandas/pokemon_data.csv')

# first 10 rows
df.head()

# last 5 rows
# df.tail(5)



### Excel file reading
df_xlsx = pd.read_excel('files/pandas/pokemon_data.xlsx')


### .txt file reading as df
df_txt = pd.read_csv('files/pandas/pokemon_data.txt', delimiter='\t')


### .html file
# df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

### Creating our own data frame
myDf = pd.DataFrame({'Name':['Hamza','Asnan'],'Age':['22','21']})


### Basic operations
# .describe() will get you all min max std mean etc
df.describe()

# to describe() single column/feature .col.describe()
df.HP.describe()

# !important .uniqueness in a feature ## Most Important ftn in ML
df.HP.unique()

# value_counts
df.HP.value_counts()

# data types
df.dtypes

# !important finding the missing data (IMP)
'''
Note: It is important to remove all the NaN or null values from the datasets because ML
is all about matrix multiplication and whatever get multiply by null/NaN will results zero
from there the prediction for a model layer will become zero and hence everything will be ruined
'''
df.isnull().sum()

'''
After getting all the null values, you have two options
1. Fill the missing values
2. Drop the missing values
'''

# Filling the missing values
# df.fillna(0, inplace=True)
# df.isnull().sum()

# Droping the values
'''
keyword 'inplace' means at place of where the condition is True.
axis = 1 will apply this ftn column wise and 0 will implement this row wise

Note:
But it is a bad practice as ML model needs approx 80k rows for training so the more you have
the better the model will train itself. Hence, filling the missing values is preferred.
'''
# df.dropna(inplace=True, axis=0)
# df.isnull().sum()


# renaming the column
df.rename({'Type 1':'myTable'}, axis=1)
