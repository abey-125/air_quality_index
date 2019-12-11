# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:39:51 2019

@author: abeya
"""
from data_from _csv import avg_data_csv()
import requests
import sys
import pandas as pd 
import os
import csv

def met_data(month,year):
    file_html=open('data/html_data/{}/{}.html'.format(year,month),'wb')
    plain_text=file_html.read()
    
    tempD=[]
    finalD=[]
    
    soup= BeautifulSoup(plain_text,'lxml')
    for table in soup.finadAll('table',{'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a=tr.get_text()
                tempD.append(a)
                
    rows =len(tempD)/15
    
    for times in range(round(rows)):
        newtempD=[]
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
        
    length=len(finalD)#gives the number of rows 
    
    finalD.pop(length-1)
    finalD.pop(0)
    
    for i in range(len(finalD)):
        finalD[i].pop(14)
        finalD[i].pop(13)
        finalD[i].pop(12)
        finalD[i].pop(11)
        finalD[i].pop(10)
        finalD[i].pop(4)
        finalD[i].pop(0)
        
    return finalD

def data_combine(year,cs):
    for a in pd.read_csv('data/real_data/real'+str(year)+'.csv',chunksize=cs):
        df= pd.DataFrame(data=a)
        mylist=df.values.tolist()
    return mylist

if __name__=='__main__':
    
    if os.path.exists("data/real_data"):
        os.makedirs("data/real_data")
    for year in range(2013,2019):
        final_data=[]
        with open('data/real_data/real'+str(year)+'.csv','w') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(0,13):
            temp=meta_data(month,year)
            final_data=final_data+temp
            
        pm=avg_data_csv(year)
        
        if len(pm)==364:
            pm.insert(364,'-')
        for i in range(len(final_data)):
            final_data[i].insert(8,pm[i])
            
        
        with open('data/real_data/real_'+str(year)+'.csv','w') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            for row in final_data:
                flag=0
                if elem in row:
                    if(elem=="" or elem==''):
                        flag=1
                if(flag!=1):
                    wr.writerow(row)
    data_2013= data_combine(2013,600)
    data_2014= data_combine(2014,600)
    data_2015= data_combine(2015,600)
    data_2016= data_combine(2016,600)
    data_2017= data_combine(2017,600)
    data_2018= data_combine(2018,600)
    
    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
     with open('data/real_data/real_combine.csv','w') as csvfile:
         wr=csv.writer(csvfile,dialect='excel')
         wr.writerow([['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5']])
         wr.writerows(total)
    
                    
            
    
    