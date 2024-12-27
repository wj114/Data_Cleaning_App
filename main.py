# This is a data cleaning application

'''
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 

'''

import pandas as pd
import numpy as np
import time
import openpyxl  #open, reads, modify Excel files
import xlrd  # read data from Excel
import os
import random

#data_path ='Walmart.csv'
#data_name ='data_walmart'

def data_cleaning_master(data_path, data_name):

    #Starting message
    print('Thank you for giving the details')

    # generating random number
    sec =random.randint(1,4)

    #print delay message
    print(f'Please wait for {sec} seconds! Check file path')
    time.sleep(sec)

    #checking if the path exist
    if not os.path.exists(data_path):
        print('Incorrect path! Try again with correct path')
        return 

    else:
        #checking the file type

        if data_path.endswith('.csv'):
            print('Dataset is CSV!')
            data =pd.read_csv(data_path, encoding_errors='ignore')


        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data =pd.read_excel(data_path) #check name and datapath
            
        else:
            print('Unknown file type')
            return
    
    # generating random number
    sec2 =random.randint(1,4)
    # print delay message
    print(f'Please wait for {sec2} seconds! Check total numbers and columns')
    time.sleep(sec2)


    #showing number of records
    print(f'Datast contain total rows: {data.shape[0]} \n Total columns {data.shape[1]}')

    #start cleaning

    ### ----------------start with duplicates---------------------
    # generating random number
    sec7 =random.randint(1,4)
    #print delay message
    print(f'Please wait for {sec7} seconds! Check total duplicates')
    time.sleep(sec7)

    #checking duplicates
    duplicates =data.duplicated()
    total_duplicates = data.duplicated().sum()  #total of duplicated records

    print(f'Dataset has total duplicate records : {total_duplicates}')

    # generating random number
    sec3 =random.randint(1,5)
    # print delay message
    print(f'Please wait for {sec3} seconds! Saving total duplicates rows')
    time.sleep(sec3)

    #saving the duplicates
    if total_duplicates>0:
        duplicate_records=data[duplicates]

        duplicate_records.to_csv(f'{data_name}_duplicates.csv',index=None)

    #delete duplicates

    df= data.drop_duplicates()  #now df is clean data

    ###----------------missing values---------------------

    # generating random number
    sec4 =random.randint(1,5)
    # print delay message
    print(f'Please wait for {sec4} seconds! Check for missing values')
    time.sleep(sec4)


    total_missing_records= df.isnull().sum().sum() #give us total missing records

    missing_value_columns =df.isnull().sum() #each column

    print(f'Datasert has Total missing records: {total_missing_records}')
    print(f'Data contain missing value by column \n{missing_value_columns}')

    #dealing with missing values
    #using fillna for int & float, dropna for others

    # generating random number
    sec5 =random.randint(1,5)
    # print delay message
    print(f'Please wait for {sec5} seconds! Cleaning datasets')
    time.sleep(sec5)

    columns = df.columns

    for col in columns:
        if df[col].dtype in (float, int):
            df[col]=df[col].fillna(df[col].mean())  #replace missing value with mean
        else:
            df.dropna(subset=col, inplace=True) #delete the missing record for non-number column
                                                        #using inplace so the data is automatically updated

    # generating random number
    sec6 =random.randint(1,5)
    #print delay message
    print(f'Please wait for {sec6} seconds! Exporting dataset')
    time.sleep(sec6)

    # now the data is cleaned

    print(f'Congratulations! Dataset is cleaned! \nNumber of rows: {df.shape[0]} Number of columns {df.shape[1]}')

    #saving clean data
    df.to_csv(f'{data_name}_clean_data.csv', index=None)

    print('Dataset is saved!')

    
    
        

if __name__ == "__main__":  #excute only when run Python script on Terminal

    start = 1

    while start==1:
        print('Welcome to Data Cleaning Master!')

        #ask path and file name
        data_path =input('Please enter dataset path :')
        data_name =input('Please enter dataset name (your preference name) :')

        #calling function
        start=data_cleaning_master(data_path, data_name)


        # after complete the cleaning
        option = input('Do you wish to continue to clean another dataset? (Y/N) : ')

        
        if option.upper() =='Y':
            start= 1
        else:
            print('Thank you. The data cleaning process is now completed!')
            start=0