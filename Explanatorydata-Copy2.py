#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


a=pd.read_csv('StudentsPerformance (1) (1).csv')
a.head()


# In[ ]:


a.tail()


# In[ ]:


a.columns.tolist()


# In[ ]:


a.shape


# In[ ]:


#Listing out the unique values 
a.nunique()


# In[ ]:


a.describe()


# In[ ]:


#Checking for null data
a.isnull().sum()


# In[ ]:


#Analysis
corelation = a.corr()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


sns.pairplot(a)


# In[ ]:


sns.relplot(x= 'math score', y='reading score', hue='gender',data=a)


# In[ ]:


sns.relplot(x= 'math score', y='writing score', hue='gender',data=a)


# In[ ]:


sns.relplot(x= 'reading score', y='writing score', hue='gender',data=a)


# In[ ]:


sns.distplot(a['math score'], bins=5)


# In[ ]:


sns.distplot(a['reading score'], bins=5)


# In[ ]:


sns.distplot(a['writing score'], bins=5)


# In[ ]:


#Parameter: Gender


# In[ ]:


sns.violinplot(x='gender',y='math score',data=a)


# In[ ]:


sns.violinplot(x='gender',y='reading score',data=a)


# In[ ]:


sns.violinplot(x='gender',y='writing score',data=a)


# In[ ]:


#Parameter: Test preparation course


# In[ ]:


sns.countplot(x='gender',data=a, hue='test preparation course')


# In[ ]:


sns.violinplot(x='test preparation course',y='math score',data=a)


# In[ ]:


sns.violinplot(x='test preparation course',y='reading score',data=a)


# In[ ]:


sns.violinplot(x='test preparation course',y='writing score',data=a)


# In[ ]:


#Parameter: Parental level of education


# In[ ]:


sns.countplot(x='gender',data=a, hue='parental level of education')


# In[ ]:


sns.violinplot(x='parental level of education',y='math score', data=a)


# In[ ]:


sns.violinplot(x='parental level of education',y='reading score', data=a)


# In[ ]:


sns.violinplot(x='parental level of education',y='writing score', data=a)


# In[ ]:


#parameter: Lunch


# In[ ]:


sns.countplot(x='gender',data=a, hue='lunch')


# In[ ]:


sns.violinplot(x='lunch',y='math score',data=a)


# In[ ]:


sns.violinplot(x='lunch',y='reading score',data=a)


# In[ ]:


sns.violinplot(x='lunch',y='writing score',data=a)


# In[ ]:


#parameter: Race/ethnicity


# In[ ]:


sns.violinplot(x='race/ethnicity',y='math score',data=a)


# In[ ]:


sns.violinplot(x='race/ethnicity',y='reading score',data=a)


# In[ ]:


sns.violinplot(x='race/ethnicity',y='writing score',data=a)

