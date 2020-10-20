#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:13:00 2020

@author: jason
"""

''' This code creates a file called InTEST.csv (also .xlsx) which is a concatenation
or appending of several excel data files. The script also deletes the first few rows of each file
and repalces the column headers wiht a row of choice. There is also inbuilt functionality
to skip missing files

N.B. the CSV output may need to be opened in Excel and saved to 
get the columns ordered correctly'''

import pandas as pd

#set up variables in the file names
year=range(1988,2018,1)

#create an empty dataframe to append to
total=pd.DataFrame()

#iterate through different file names
for y in year:
    fileName=str('history_export_'+str(y)+'.csv')
    print(fileName)
    #use try and excpet to skip past missing files
    try:
        input=pd.read_csv(fileName)
        print(len(input.index))
        #delete first few rows and replace column header names with selected row
        new_header = input.iloc[9] 
        input = input[10:] 
        input.columns = new_header       
        total=total.append(input)
    except IOError:
        pass

#write to excel and csv - csv is easier to debug
total.to_excel('InTEST.xlsx', sheet_name='Summary', index=False)
total.to_csv('InTEST.csv', index=False)