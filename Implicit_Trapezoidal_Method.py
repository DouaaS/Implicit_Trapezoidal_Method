#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def implicit_trapezoisal_method(x0,y0,xf,delta,n):
    num = int((xf-x0)/delta)
    x = np.zeros(num+1) # Numerical grid
    y = np.zeros(num+1)
    y[0]=y0
    x[0]=x0
    for i in range(1,num+1):
        x[i]=x[i-1]+delta
        yi=y[i-1]
        yiplus1=y[i-1]+(delta/2)*(((2.5*(1-y[i-1]))/(1+2.5*x[i-1]))-y[i-1]**2+((2.5*(1-yi))/(1+2.5*x[i])-yi**2))
        diff=abs(yiplus1-yi)
        while diff >10**(-n): 
            yi=yiplus1
            yiplus1=y[i-1]+(delta/2)*(((2.5*(1-y[i-1]))/(1+2.5*x[i-1]))-y[i-1]**2+((2.5*(1-yi))/(1+2.5*x[i])-yi**2))
            diff=abs(yiplus1-yi)
        y[i]=yiplus1
    return [x,y]
y1=implicit_trapezoisal_method(0,0,10,0.5,2)[1]
y2=implicit_trapezoisal_method(0,0,10,0.1,4)[1]
print("for test case 1:") 
print(y1[len(y1)-1])


# In[5]:


print("for test case 2:") 
print((y2[len(y2)-1]))


# In[ ]:





# In[ ]:




