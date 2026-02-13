#!/usr/bin/env python
# coding: utf-8

# ## Joining a second dataset
# 
# In this notebook, I’m combining my original Netflix dataset with another dataset that groups countries into larger regions.
# I created the second dataset myself for this assignment so I could clearly show how merging works in pandas. I made sure the country names match the original dataset so the join would work properly and not cause errors.
# 
# 

# ## Importing and Loading

# In[ ]:


import pandas as pd


# In[33]:


df =pd.read_csv("data/netflix_titles.csv")
regions = pd.read_csv("data/country_regions.csv")
regions.columns



# Before merging, I had to check to make sure that both datasets had the same column called "country". This will be the key to combining the datasets. If the country names match in both datasets, each Netflix title will have a region attached to it. 

# ## Merging 

# I used a LEFT join when merging the datasets because I wanted to keep all Netflix titles, even if some countries did not match the region dataset. A LEFT join keeps all rows from the original Netflix dataset. If a country does not exist in the region dataset, the new "region" column will contain a missing value (NaN). These NaN values show which countries did not have a matching region. 
# 

# In[34]:


merged = pd.merge(
    df,
    regions,
    how="left",
    on="country"
)

merged.head()


# ## Analyzing The Region Data

# In[35]:


merged["region"].value_counts(dropna=False)


# This counts how many Netflix titles belong to each region. Value_counts() shows how many times each region appears, and dropna=False ensures that missing values (NaN) are included in the count. Including the missing values helps me see how many titles did not match with a region when I merged the datasets. This helps check if the join worked properly.

# In[36]:


merged["region"].value_counts()


# ^^This shows which region has the most Netflix titles^^

# In[ ]:




