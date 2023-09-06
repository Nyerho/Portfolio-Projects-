#!/usr/bin/env python
# coding: utf-8

# In[1]:


## import libs
import pandas as pd 
import numpy as np


# In[4]:


## read in dataset 
df = pd.read_csv(r"C:\Users\HP\Documents\pythonaltschool\fifa21 raw data v2.csv")
df


# In[12]:


df.info()


# In[6]:


df.columns


# In[7]:


df.head(10)


# ## data cleaning 

# In[14]:


## create a copy of the data 
df2 = df.copy()
df2


# In[ ]:


# first column 'ID' = CURRENT OWNER OF CLUB


# ## CLUB COLUMN 

# In[16]:


df2['Club'].dtype


# In[18]:


df2['Club'].unique() # check unique values in clu column 


# In[21]:


## remove white spaces from Club column 

df2['Club'] = df2['Club'].str.strip()
df2['Club'].unique()


# ## CONTRACT column 

# In[26]:


pd.set_option('display.max_columns', 78)


# In[22]:


df2['Contract'].dtype


# In[24]:


df2.columns


# In[25]:


df2.shape


# In[27]:


## check for unique values in contract column 
df['Contract'].unique()


# In[30]:


## make formatting consistent
for index, row in df2.iterrows(): # iterrows allows to iterate thru each row in that column
    if 'On Loan' in row['Contract'] or 'Free' in row['Contract']:
        print(row['Contract'])


# In[32]:


## extract the 3 different unique infos from the contract column and put each in a separate column to make the formatting consistent

def extract_contract_info(contract):
    if contract == 'Free' or 'On Loan' in contract:
        start_date = np.nan
        end_date = np.nan
        contract_length = 0 
    else:
        start_date, end_date = contract.split(' ~ ')
        start_year = int(start_date[:4])
        end_year = int(end_date[:4])
        contract_length = end_year - start_year
    return start_date, end_date, contract_length 

## create new columns from this info above and add to the data set "df2"
new_cols = ['Contract_start', 'Contract_End', 'Contract_Length(years)']

## define data to be put in the new columns 
new_data = df2['Contract'].apply(lambda x: pd.Series(extract_contract_info(x))) #pd.series method converts the object returned by the extract_contratct info function above into a pd series object which is a dimensional array-like object used to store and manipulate data 

#create a for loop that would loop through the column names and insert the info we have extracted
for i in range(len(new_cols)):
    df2.insert(loc=df2.columns.get_loc('Contract')+1+i, column = new_cols[i], value=new_data[i]) #this finds the index position of the 'Contract' column and inserts the new columns next to it
    


# In[33]:


df2.head(5)


# In[38]:


df2[['Contract', 'Contract_start', 'Contract_End', 'Contract_Length(years)']].sample(5)


# In[40]:


# define contratct categories 
def contract_status(contract):
    if contract == 'Free':
        return 'Free'
    elif 'On Loan' in contract:
        return 'On Loan'
    else:
        return 'Contract'

## add contract_status column  to df2
df2.insert(df2.columns.get_loc('Contract_Length(years)')+1, 'contract_status', df2['Contract'].apply(contract_status))
df2.sample(5)
    


# In[41]:


df2[['Contract', 'Contract_start', 'Contract_End', 'Contract_Length(years)','contract_status']].sample(5)


# ## HEIGHT COLUMN 

# In[42]:


#DATA TYPE height is supposed to be integer 
df2["Height"].dtype


# In[43]:


#check why its a string 
df2["Height"].unique()


# In[46]:


# convert from inches to cm and then to int from strings
def convert_height(height):
    if "cm" in height:
        return int(height.strip("cm"))
    else:
        feet, inches = height.split("'")
        total_inches = int(feet)*12 + int(inches.strip('"'))
        return round(total_inches * 2.54)
    
#apply to height column
df2['Height'] = df2['Height'].apply(convert_height)
df2['Height'].unique()


# In[47]:


## rename height column to be more descriptive 
df2 = df2.rename(columns = {'Height':"Height(cm)"})
df2.head(5)


# ## WEIGHT COLUMNS 

# In[51]:


# check data type 
df2['Weight'].dtype


# In[52]:


#check unique values 
df2['Weight'].unique()


# In[56]:


# convert from lbs to kg to keep format consistent. 
def convert_weight(weight):
    if "kg" in weight:
        return int(weight.strip("kg")) # strips the kg
    else:
        weight_lbs = int(weight.strip("lbs")) # strips the lbs
        return round(weight_lbs/2.205) # converts the number from "O" to "int" and then from lbs to kg by *2.205
    
# apply to weight column 
df2['Weight'] = df2['Weight'].apply(convert_weight)
df2['Weight'].unique()


# In[58]:


# rename weight column
df2 = df2.rename(columns={"Weight": "Weight(kg)"})
df2.head()


# In[60]:


df2.info()


# In[ ]:


## LOAN DATE COLUMN 


# In[61]:


# check dtype
df2['Loan Date End'].dtype


# In[63]:


#check for unique values to be able to know if  formating is  consistent 
df2['Loan Date End'].unique()


# In[64]:


on_loan = df2[df2['contract_status']== 'On Loan']
on_loan[['Contract', 'contract_status', 'Loan Date End']]

## this returns the values in the contract status column that shows null in the loan date end columns. the null values are because those players are on loan and as such loan date end will record null


# In[ ]:


## W/F COLUMN 


# In[65]:


## check dtype
df2['W/F'].dtype


# In[66]:


# check unique values to aid consistent formating
df2['W/F'].unique()


# In[67]:


## to remove the stars -- for future refrence 
df2['W/F']= df2['W/F'].str.replace('★', '')
df2['W/F'].unique()     # this is used if the values are needed for calculation


# In[ ]:


## HITS COLUMN


# In[68]:


#check dtype
df2['Hits'].dtype


# In[69]:


#check unique values 
df2['Hits'].unique()


# In[78]:


# convert to int
import numpy as np
df['Hits'] = df['Hits'].astype(int)
df['Hits'] = df['Hits'].apply(lambda x: np.log10(x) * 1024)
df2


# In[ ]:





# In[ ]:





# In[ ]:




