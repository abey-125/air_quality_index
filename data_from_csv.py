# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:21:05 2019

@author: abeya
"""

import pandas
import matplotlib.pyplot as plt

def avg_data_csv():
    temp=0
    average=[]
    lisdata
    for row in pd.read_csv('D:/python/air_quality_index/day2/AQI/aqi2013.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.dataframe(data=row)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data :
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if(i!='nodata' and i!='pwrfail' and i!='---' and i!='Invld'):
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
        return average
if __name__=='___main__':
    lstdata=[]
    for i in range():
        lstdata[i]=avg_data_csv()
        plt.plot(range(0,360),lst2013,label='2013 data')
        plt.show