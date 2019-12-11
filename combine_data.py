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
    
    