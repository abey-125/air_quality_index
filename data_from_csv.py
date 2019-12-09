# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:21:05 2019

@author: abeya
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_csv(year):
    temp=0
    average=[]
    for row in pd.read_csv('data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=row)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data :
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        #temp_i=temp_i+1
        average.append(avg)
    return average
if __name__=="__main__":

    print("started")
    lstdata=[]
    i=0
    #plt.plot(range(0,365),lst2013,label="2013 data")
    for year in range(2013,2019):
        lst_data=avg_data_csv(year)
        lstdata.append(lst_data)
        #plt.plot(range(0,365),lstdata[i],label='{}data '.format(year))
        if(year==2014) or year==2018:
            plt.plot(range(0,364),lstdata[i],label='{}data '.format(year))
        else:
            plt.plot(range(0,365),lstdata[i],label='{}data '.format(year))
        i +=1
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    print("sucess")
    plt.show