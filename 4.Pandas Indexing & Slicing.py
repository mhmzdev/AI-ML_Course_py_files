import pandas as pd
import numpy as np

df = pd.read_csv('datasets/pandas/pokemon_data.csv')

## Getting specific Columns
df[['Name', 'Type 1']].head()

## Read each Rows;iloc ==> index location
df.iloc[0:4]


## Rows of specific column
# for index, row in df.iterrows():
# 	print(index, row['Name'])

## Rows at specific location	; loc ==> location
## CONCEPT Name ==> 'Selective Search'
df.loc[df['Type 1'] == 'Grass']

# Second Method of doing the above thing	; df.iloc[row, column]
df.iloc[2,1]


############## Features and Target ########################
# Target ==> Jiski prediction karni hoti hai
# Features ==> Jis ki help sy prediction krni hoti hai
# Both are columns

## CSV file as not availble that's why created this on my own
hiring = pd.read_excel('datasets/hiring.xlsx')

## Feature ==> x axis
## Target ==> y axis
y = hiring['salary']
x = hiring[['experience','test_score','interview_score']]

print(x)