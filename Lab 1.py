
# coding: utf-8

# # Lab 1

# In[6]:


print ("hello world")
1+2

a = 3


# ## demo of writing

# In[7]:


print (1)
print (a)


# ## demo of print and solving

# In[8]:


a = 4
b = 3
a+b


# ## demo of addition

# 1. item 1
# 2. item 2
# 
# JMU [website](http://www.jmu.edu)

# ## demo of list and link

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()

