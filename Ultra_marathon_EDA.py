#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df= pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[3]:


df.head(10)


# In[4]:


df.shape


# In[5]:


#cleamn up date
#only want usa races, 50k or 50mi, 2020
#step 1 show 50k or 50mi
#50k
#50mi


# In[6]:


df[df['Event distance/length']== '50mi']


# In[ ]:


#combine 50k/50mi with isin


# In[7]:


df[df['Event distance/length'].isin(['50km', '50mi'])] 


# In[8]:


df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event']==2020)]


# In[9]:


df[df['Event name']== 'Everglades 50 Mile Ultra Run (USA)']


# In[10]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


# In[ ]:


#combine all the filters together


# In[14]:


df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event']==2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]
                                                                                         
                                                                                         


# In[15]:


df2 = df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event']==2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]
                                                                                         
                                                                                         


# In[16]:


df2.head(10)


# In[17]:


df2.shape


# In[ ]:


#remove (USA) from event name


# In[18]:


df2['Event name'].str.split('(').str.get(0)


# In[19]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[20]:


df2.head()


# In[21]:


#clean up athelete age


# In[22]:


df2['athelete_age'] = 2020- df2['Athlete year of birth']


# In[ ]:


#remove h from athelete performance


# In[23]:


df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[24]:


df2.head(10)


# In[ ]:


#drop columns = Athlete club, Athlete Country, Athlete year of birth, Athlete age category.


# In[34]:


df2 = df2.drop (['Athlete club', 'Athlete country', 'Athlete year of birth', 'Athlete age category'] axis = 1)


# In[35]:


df2.head(5)


# In[32]:


df2 = df2.drop (['Athlete club', 'Athlete country', 'Athlete year of birth','Athlete age category'], axis = 1)


# In[33]:


df2.head()


# In[ ]:


#clean up null values


# In[38]:


df2.isna().sum()


# In[43]:


df2[df2['athelete_age'].isna()==1]


# In[44]:


df2 = df2.dropna()


# In[46]:


df2.shape


# In[ ]:


#check for duplicates


# In[48]:


df2[df.duplicated() == True]


# In[ ]:


#reset index


# In[49]:


df2.reset_index(drop = True)


# In[50]:


#fix types


# In[51]:


df2.dtypes


# In[52]:


df2['athelete_age'] = df2['athelete_age'].astype(int)


# In[53]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[54]:


df2.dtypes


# In[55]:


df2.head()


# In[56]:


#rename columns:
#Year of event                  int64
#Event dates                   object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed        float64
#Athlete ID                     int64
#athelete_age                   int64


# In[69]:


df2 = df2.rename(columns = {'Year of event':'year',                                                                                                   
                            'Event dates':'race_day',
                            'Event name':'race_name',
                            'Event distance/length':'race_length',
                            'Event number of finishers':'race_number_of_finishers',
                            'Athlete performance':'athelete_performance',
                            'Athlete gender':'athelete_gender',
                            'Athlete average speed':'athelete_average_speed',
                            'Athlete ID':'athelete_id',    
})


# In[70]:


df2.head()


# In[ ]:


#reorder columns


# In[64]:


df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athelete_id', 'athelete_gender', 'athelete_performance', 'athelete_average_speed','athelete_age' ]]


# In[65]:


df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athelete_id', 'athelete_gender', 'athelete_performance', 'athelete_average_speed','athelete_age' ]]


# In[71]:


df2 = df2.rename(columns = {'Year of event':'year',                                                                                                   
                            'Event dates':'race_day',
                            'Event name':'race_name',
                            'Event distance/length':'race_length',
                            'Event number of finishers':'race_number_of_finishers',
                            'Athlete performance':'athelete_performance',
                            'Athlete gender':'athelete_gender',
                            'athelte_average_speed':'athelete_average_speed',
                            'Athlete ID':'athelete_id',    
})


# In[72]:


df2.head()


# In[73]:


df2 = df2.rename(columns = {'Year of event':'year',                                                                                                   
                            'Event dates':'race_day',
                            'Event name':'race_name',
                            'Event distance/length':'race_length',
                            'Event number of finishers':'race_number_of_finishers',
                            'Athlete performance':'athelete_performance',
                            'Athlete gender':'athelete_gender',
                            'athelte_average_speed':'athelete_average_speed',
                            'Athlete ID':'athelete_id',    
})


# In[74]:


df2.head()


# In[75]:


df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athelete_id', 'athelete_gender', 'athelete_performance', 'athelete_average_speed','athelete_age' ]]


# In[76]:


df2.head()


# In[77]:


df2.head(5)


# In[79]:


sns.histplot(df3['race_length'])


# In[80]:


sns.histplot(df3, x = 'race_length', hue = 'athelete_gender')


# In[82]:


sns.displot(df3[df3['race_length'] == '50mi']['athelete_average_speed']) 


# In[84]:


sns.violinplot(data = df3, x = 'race_length', y = 'athelete_average_speed')


# In[89]:


sns.violinplot(data = df3, x = 'race_length', y = 'athelete_average_speed', hue = 'athelete_gender', split = True, inner = 'quart')


# In[92]:


sns.lmplot(data = df3, x = 'athelete_age', y = 'athelete_average_speed', hue = 'athelete_gender')


# In[ ]:


#questions to find out from the data
#Year of event                 
#Event dates                    
#Event name                     
#Event distance/length          
#Event number of finishers      
#Athlete performance            
#thlete gender                 
#Athlete average speed          
#Athlete ID                     
#athelete_age                 
#dtype: int64


# In[ ]:


#difference in speed for 50k/50mi, male to female


# In[93]:


df3.groupby(['race_length', 'athelete_gender'])['athelete_average_speed'].mean()


# In[94]:


#seasons for the date - slower in summer than winter?


# In[101]:


df3['race_month'] = df3['race_day'].str.split('.').str.get(1).astype(int)


# In[103]:


df3.head(25)


# In[104]:


df3['race_season'] = df3['race_month'].apply(lambda x: 'Winter' if x > 11 else 'Fall' if x > 8 else 'Summer' if x > 5 else 'Spring' if x > 2 else 'Winter')


# In[105]:


df3.head(25)


# In[106]:


df3.groupby('race_season')['athelete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[ ]:


#50 miler only


# In[110]:


df3.query('race_length == "50mi"').groupby('race_season')['athelete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




