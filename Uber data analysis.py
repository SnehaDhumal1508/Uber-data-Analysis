#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[ ]:


files=os.listdir(r'C:\ENGG PROJECTS\Data Analysis Hands On Projects\uber-pickups-in-new-york-city')
files


# In[ ]:


path = r'C:\ENGG PROJECTS\Data Analysis Hands On Projects\uber-pickups-in-new-york-city'

final=pd.DataFrame()

for file in files:
    df = pd.read_csv(path + '/' +file)
    final=pd.concat([df,final])


# In[ ]:


final.shape


# In[ ]:


final.fillna(0)


# In[ ]:


final.fillna(0)


# In[ ]:


final.dropna()


# In[ ]:


final.copy()
final.fillna(0)
df = final.dropna()
df


# In[ ]:


df.dtypes


# In[ ]:





# In[ ]:


df['Date/Time']=pd.to_datetime(df['Date/Time'],infer_datetime_format=True)


# In[ ]:


df.dtypes


# In[ ]:


df.head()


# In[ ]:


df['Month'] = df['Date/Time'].dt.month


# In[ ]:


df.head()


# In[ ]:


df.dtypes


# In[ ]:


df['Hour'] = df['Date/Time'].dt.hour


# In[ ]:


df.head()


# In[ ]:


df['Weekday'].value_counts()


# In[ ]:


get_ipython().system('pip install plotly')


# In[ ]:


#analysis by weekdays
import plotly.express as px
px.bar(x= df['Weekday'].value_counts().index,
       y= df['Weekday'].value_counts(),
       title = "Analysis by weekdays")


# In[ ]:


#Rush By Hour
plt.figure(figsize = (40,20)) 
for i,month in enumerate(df['Month'].unique()):
    plt.subplot(3,2,i+1) #3 rows 2 columns 
    df[df['Month']==month]['Hour'].hist()


# In[ ]:


df.head()


# In[ ]:


import plotly.graph_objs as go
from plotly.offline import download_plotlyjs , init_notebook_mode, plot, iplot
import chart_studio.plotly as py


# In[ ]:


#analysis of which month has highest rides
graphbar = go.Bar(x = df.groupby('Month')['Hour'].count().index,
       y= df.groupby('Month')['Hour'].count(),
       name = 'Priority')
iplot([graphbar])


# In[ ]:


df['Day'] = df['Date/Time'].dt.day


# In[ ]:


df.head()


# In[ ]:


# analysis of journery of each day
plt.figure(figsize = (10,8))
plt.hist(df['Day'],bins = 30,rwidth=0.9,range=(0.5,30.5))
plt.xlabel('Date of month')
plt.ylabel('Total Journery of each day')
plt.title('Journey by month day')


# In[ ]:


#analysis of total rides month wise
plt.figure(figsize= (20,20))
for i,month in enumerate(df['Month'].unique(),1):
    plt.subplot(3,2,i)
    df1 = df[df['Month']==month]
    plt.hist(df1['Day'])
    plt.xlabel('Days in month {}'.format(month))
    plt.ylabel('Total rides')
    plt.title('Analysis of total rides month wise')


# In[ ]:


#analysis rush in hr
ax = sns.pointplot(x = 'Hour' , y = 'Lat', data=df,hue='Weekday')
ax.set_title('Hours vs Latitude of passengers')


# In[ ]:


# analyse which base no gets popular by month name
base  = df.groupby(['Base', 'Month'])['Date/Time'].count().reset_index()
base.head(3)


# In[ ]:


plt.figure(figsize = (10,8))
sns.lineplot(x='Month',y='Date/Time', hue='Base', data=base)


# In[ ]:


#perform cross analysis using headmap - uses matrix, whoseever index is high it will return that

#heatmap between Hour and weekday
def count_rows(rows):
    return len(rows)


# In[ ]:


cross1 = df.groupby(['Weekday','Hour']).apply(count_rows)


# In[ ]:


pivot = cross1.unstack() #hours are columns
pivot


# In[ ]:


plt.figure(figsize=(10,8))
sns.heatmap(pivot)


# In[ ]:


def heatmap(col1,col2):
    cross = df.groupby([col1,col2]).apply(count_rows)
    pivot = cross.unstack()
    plt.figure(figsize=(10,8))
    return sns.heatmap(pivot)


# In[ ]:


heatmap('Day','Hour')


# In[ ]:


heatmap('Month','Day')


# In[ ]:


# analysis of location data points
plt.figure(figsize=(10,8))
df.head()
plt.plot(df['Lon'],df['Lat'],'r+',ms=0.5)
plt.xlim(-74.2,-73.7)
plt.ylim(40.5,41)


# In[ ]:


df2 = df[df['Weekday']=='Sunday']

rush = df2.groupby(['Lat','Lon'])['Weekday'].count().reset_index()
rush


# In[ ]:


rush.columns = ['Lat','Lon','Number of Trips']
rush.head(3)


# In[ ]:


from folium.plugins import HeatMap
import folium
#Folium is a Python library used for visualizing geospatial data.

basemap = folium.Map()
basemap


# In[ ]:


HeatMap(rush,zoom=20,radius=10).add_to(basemap)
basemap


# In[ ]:


#making a function
def plot(df,Day):
    basemap =  folium.Map()
    df2 = df[df['Weekday']==Day]
    HeatMap(df2.groupby(['Lat','Lon'])['Weekday'].count().reset_index(),zoom=20,radius=15).add_to(basemap)
    return basemap


# In[ ]:


plot(df,'Monday')


# In[ ]:


uber_15 = pd.read_csv(r'C:\ENGG PROJECTS\Data Analysis Hands On Projects\uber-pickups-in-new-york-city\uber-raw-data-janjune-15.csv')
uber_15.head(3)


# In[ ]:


uber_15.dtypes


# In[ ]:


uber_15['Pickup_date']=pd.to_datetime(uber_15['Pickup_date'],infer_datetime_format=True)


# In[ ]:


uber_15.dtypes


# In[ ]:


uber_15['Month']= uber_15['Pickup_date'].dt.month
uber_15['Weekday'] = uber_15['Pickup_date'].dt.day_name()
uber_15['Day']= uber_15['Pickup_date'].dt.day
uber_15['Minutes'] = uber_15['Pickup_date'].dt.minute
uber_15['Hour'] = uber_15['Pickup_date'].dt.hour


# In[ ]:


uber_15.head()


# In[ ]:


#uber pickups by the month in nyc
px.bar(x = uber_15['Month'].value_counts().index,
      y = uber_15['Month'].value_counts())


# In[ ]:


plt.figure(figsize=(10,8))
sns.countplot(uber_15['Hour'])


# In[ ]:


#rush in nyc day and hour wise
summary = uber_15.groupby(['Weekday','Hour'])['Pickup_date'].count().reset_index()
summary.head()
summary.columns = ['Weekday','Hour','counts']
summary.head(3)


# In[ ]:


plt.figure(figsize= (10,8))
sns.pointplot(x = 'Hour',y = 'counts', hue = 'Weekday', data = summary)


# In[ ]:


uber_foil  = pd.read_csv(r'C:\ENGG PROJECTS\Data Analysis Hands On Projects\uber-pickups-in-new-york-city\Uber-Jan-Feb-FOIL.csv')
uber_foil.head(3)


# In[ ]:


# which base no hase most active vehicles
uber_foil['dispatching_base_number'].unique()


# In[ ]:


sns.boxplot(x = 'dispatching_base_number',
            y = 'active_vehicles',
           data = uber_foil)


# In[ ]:


# analyis which base no has most trips
sns.boxplot(x = 'dispatching_base_number',
            y = 'trips',
           data = uber_foil)


# In[ ]:


uber_foil['Trips/Vehicle'] = uber_foil['trips']/uber_foil['active_vehicles']
uber_foil.head(2)


# In[ ]:


#avg t/v inc/decreases with dates with each of bae no
plt.figure(figsize= (10,8))
uber_foil.set_index('date').groupby(['dispatching_base_number'])['Trips/Vehicle'].plot()
plt.ylabel('Avg t/v')
plt.title('Demand vs Supply')
plt.legend()

