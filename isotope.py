import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from sklearn.linear_model import LinearRegression
from numpy import shape
#from sklearn.model_selection import cross_val_predict
import csv
import pandas as pd



import os
import sys


file_path = '/Users/FengLIANG/Documents/Mg同位素数据处理软件'

analysis_times = []
analysis_dates = []
delta25Mgs = []
delta26Mgs = []
filename = []

for file in os.listdir(file_path):
    if os.path.splitext(file)[1] == '.exp':
        
        date_time = pd.read_csv(os.path.join(file_path,file), engine='python', sep=': ')
        analysis_date = date_time.loc['Date'].at['Neptune Analysis Data Report']
        analysis_time = date_time.loc['Analysis time'].at['Neptune Analysis Data Report']
        
        try:   
            df = pd.read_csv(os.path.join(file_path,file),sep='\t',skiprows=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21))
            df = df.dropna(axis=1, how='all', inplace=False)
            df = df.dropna(axis=0, how='all', inplace=False)
            df = df.set_index('Time')
            delta25Mg = df.loc['Mean'].at['25Mg/24Mg (1)']
            delta26Mg = df.loc['Mean'].at['26Mg/24Mg (2)']
  
        except(KeyError):
            df = pd.read_csv(os.path.join(file_path,file),sep='\t',skiprows=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
            df = df.dropna(axis=1, how='all', inplace=False)
            df = df.dropna(axis=0, how='all', inplace=False)
            df = df.set_index('Time')
            delta25Mg = df.loc['Mean'].at['25Mg/24Mg (1)']
            delta26Mg = df.loc['Mean'].at['26Mg/24Mg (2)']
    
        #print(file)
        #print(analysis_time, analysis_date, file, delta25Mg, delta26Mg)
        analysis_times.append(analysis_time)
        analysis_dates.append(analysis_date)
        filename.append(file)
        delta25Mgs.append(delta25Mg)
        delta26Mgs.append(delta26Mg)

analysis_times_frame = pd.DataFrame(analysis_times, columns=['time'])
analysis_dates_frame = pd.DataFrame(analysis_dates, columns=['date'])
filename_frame = pd.DataFrame(filename, columns=['filename'])
delta25Mgs_frame = pd.DataFrame(delta25Mgs, columns=['delta25Mg'])
delta26Mgs_frame = pd.DataFrame(delta26Mgs, columns=['delta26Mg'])


result = pd.concat([analysis_times_frame, analysis_dates_frame, filename_frame, delta25Mgs_frame, delta26Mgs_frame], axis=1)
#result.reset_index(inplace=True)
#del result['index']
print(result.head())
#result = result.sort_values(by=['time', 'date'], ascending=(True,True))

#result.to_csv('Mg result.csv')






