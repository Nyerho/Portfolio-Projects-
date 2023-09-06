#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load libs
import pandas as pd 


# In[3]:


#import dataset 
df = pd.read_csv(r"C:\Users\HP\Documents\pythonaltschool\weather data.csv")
df


# In[4]:


#display max rows 
pd.set_option('display.max.rows', 8785)
df


# In[5]:


#delete duplicates 
df = df.drop_duplicates()
df


# In[6]:


df.info()


# In[7]:


df.head(20)


# In[9]:


df['Date/Time'] = df['Date/Time'].str.replace('/', '-')
df


# In[11]:


df[['date', 'time']] = df['Date/Time'].str.split(' ', n=1, expand=True)
df


# In[15]:


df.index


# In[16]:


df.columns


# ## Find all the unique windspeed values in the data. 

# In[18]:


## work on windspeed column 
df.nunique()


# In[20]:


df['Wind Speed_km/h'].nunique()


# In[21]:


## to show ALL the unique values in this column 

df['Wind Speed_km/h'].unique() # answer


# ## find the number of times when the weather is exactly clear 

# In[25]:


## working on the weather column 
#using value counts
df.Weather.value_counts()


# In[27]:


## using filter
df[df.Weather == 'Clear'] ## shows all the data associated with the clear weather


# In[28]:


#using groupby 
df.groupby('Weather').get_group('Clear') # get_group returns the particular argument in the column


# ## Find the number of times when the wind speed was exactly 4km/h

# In[29]:


df[df['Wind Speed_km/h'] == 4]


# ## find the null Values in the data 

# In[34]:


df.isnull().sum() ## .sum() returns a count of all the null valies in each column 


# In[35]:


df.notnull().sum() ## not null values 


# ## Rename weather column to Weather Condition 

# In[ ]:


df.rename(columns={'Weather': 'Weather Condition'}, inplace = True)
df


# ## calculate mean of the visibilty 

# In[38]:


visibility_mean = df['Visibility_km'].mean()
print(visibility_mean)


# ## calculate the standard deviation of the pressure
# 

# In[40]:


pressure_std = df['Press_kPa'].std()
print(pressure_std)


# ## Variance for relative humidity 

# In[45]:


variance_relahumid = df['Rel Hum_%'].var()
print(variance_relahumid)


#  ## print all instances where weather condition says snow 

# In[46]:


df[df['Weather Condition'].str.contains('Snow')]


# In[50]:


df['Weather Condition'].value_counts()


# ##  find instances where wind speed  > 24, visibility = 25

# In[52]:


df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] ==25)]


# ## what is the mean value for each column against each weather condition

# In[54]:


#list out column names 
df.columns


# In[55]:


# use groupby function to find mean against the weather codition column 
df.groupby('Weather Condition').mean()


# ## min and max values of each column agaisnst each weather condition 

# In[56]:


# groupby
df.groupby('Weather Condition').min()


# In[57]:


df.groupby('Weather Condition').max()


# ## show where weather condition is fog

# In[59]:


df[df['Weather Condition'] == 'Fog']


# In[61]:


df[(df['Weather Condition']== 'Clear') | (df['Visibility_km']> 40)]


# In[63]:


#weather condition and relative humidity = clear and > 50

df[(df['Weather Condition']== 'Clear') & (df['Rel Hum_%']> 50)]


# In[65]:


#weather condition and relative hum > 40  or  visibility > 50

df[(df['Weather Condition']== 'Clear')  &(df['Rel Hum_%']> 50) |(df['Visibility_km']> 40)]


# In[ ]:




