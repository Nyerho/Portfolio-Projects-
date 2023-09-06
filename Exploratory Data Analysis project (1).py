#!/usr/bin/env python
# coding: utf-8

# ## EDA in Pandas

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv(r"C:\Users\HP\Documents\pythonaltschool\world_population.csv")


# In[7]:


df


# In[11]:


pd.set_option('display.max.rows', 235)
df


# In[10]:


pd.set_option('display.float_format', lambda x: '%.1f' % x) ## formats decimals numbers to one decimal place 


# In[12]:


df


# In[13]:


df.info()


# In[14]:


df.describe()


# In[16]:


df.isnull().sum()  # this gives us all the columns and the number of values missing in each columns


# In[18]:


df.nunique()


# In[20]:


## to look for top range countries (Top 5 highest population in 2022)
df.sort_values(by = "2022 Population", ascending = False).head()


# In[22]:


## to look for top range countries (Top 5 highest population in 2015)
df.sort_values(by = "2015 Population", ascending = False).head(10)


# In[23]:


df.corr() # to check correlation


# In[30]:


# visualize correlation we use heatmap to visualize correlation
sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.figsize'] =(20,10)

plt.show()


# ## Case : Are there certain continents that have grown faster than others, and which case 

# In[31]:


df


# In[32]:


## group by continents
df.groupby('Continent').mean()


# In[34]:


df[df['Continent'].str.contains('Oceania')]


# In[42]:


## sort by avg population 2022 population
df.groupby('Continent')[df.columns[5:13]].mean().sort_values(by ='2022 Population', ascending = False)


# In[54]:


df2 = df.groupby('Continent')[['1970 Population',
        '1980 Population', '1990 Population', '2000 Population',
        '2010 Population', '2015 Population', '2020 Population',
        '2022 Population']].mean().sort_values(by='2022 Population', ascending = False)

df2


# In[37]:


#df2.plot() #create a visual map for df2 


# In[55]:


#transpose continents to be columns and the columns be the index 
df3 = df2.transpose()
df3


# In[56]:


df3.plot()


# In[49]:


#df.columns


# In[ ]:


## OR  WE CAN USE 
#df2 = df.groupby('Continent')[['1970 Population','19980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population','2020 Population']].mean().sort_values(by ='2022 Population', ascending = False)



# In[57]:


## find outliers by using boxplot 
## outliers help expose the why in the analysis
df.boxplot(figsize=(20,10))


# In[58]:


df 


# In[61]:


df.select_dtypes(include='object')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




