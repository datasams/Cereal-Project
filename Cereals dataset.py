#!/usr/bin/env python
# coding: utf-8

# In[33]:


# Importing libraries

import pandas as pd
import matplotlib.pyplot as plt


# In[34]:


# Read Cereal.csv dataset and store in "df" dataframe

df = pd.read_csv("cereal.csv")
df


# In[35]:


# Check details about the "df" dataframe
df.info()


# In[41]:


# show the first five rows of df dataframe

df.head()


# In[37]:


# Convert "rating" column to integer

df["rating"] = df["rating"].astype(int)


# In[38]:


# Show summary statistics for the dataset

df.describe().round(2)


# In[39]:


# Create histogram for the "calories" column

plt.hist(df["calories"]);
plt.xlabel("Calories per serving")
plt.ylabel("Frequency")
plt.title("Distribution of Cereal Calories Concentration");


# In[40]:


# Create boxplot for the "calories" column

plt.boxplot(df["calories"], vert=False)
plt.xlabel("Calories per serving")
plt.title("Distribution of Cereal Calories Concentration");


# In[ ]:




