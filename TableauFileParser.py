
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[3]:



path = "Documents\Tableau\Homework\DataSource"
directory = os.path.join(os.getcwd(), path)
print(directory)


# In[3]:


os.chdir(directory)
for root,dirs,files in os.walk(directory):
     combined_csv = pd.concat( [ pd.read_csv(f) for f in files ] )      
  


# In[4]:



combined_csv.to_csv( "citybikedata.csv", index=False )

