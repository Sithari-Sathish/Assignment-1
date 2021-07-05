#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


print('Matplotib version: ', mpl.__version__)


# In[38]:


print(plt.style.available)


# In[ ]:





# In[8]:


from numpy.random import randn, randint, uniform, sample


# In[11]:


# line plot

#displays information as a series of datapoints called markers,connected by straight line
#segments


# In[40]:


##simple examples

x=np.arange(0,10)
y=np.arange(11,21)
print(x)
y


# In[41]:


plt.plot(x,y)


# In[42]:


plt.plot(x,y,'go--', linewidth=1, markersize=7)
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# In[19]:


np.pi


# In[21]:


x = np.arange(0, 4 * np.pi , 0.1)
y= np.sin(x)
plt.title("sine waveform")

#plot the points using matlotlib
plt.plot(x,y,color='b')
plt.show()


# In[22]:


x= np.arange(0,10)
y=x*x
y


# In[23]:


plt.plot(x,y)


# In[29]:


plt.title('square plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()


# In[31]:


#creating subplots

plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y, 'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[33]:


x=np.arange(0,10)
y= 3*x +10
y


# In[35]:


plt.title('Assignment of line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()


# In[36]:


x=[1,2,3,4,5,6,7] 
y=[160,150,140,145,175,165,180]


# In[37]:


plt.title('x-y plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()


# In[ ]:




