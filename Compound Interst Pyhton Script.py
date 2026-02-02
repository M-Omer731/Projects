#!/usr/bin/env python
# coding: utf-8

# In[41]:


p=float(input('what was the principal amount originally deposited: '))
r=float(input('what is the annual interst rate paid by the account: '))
n=int(input('how many times per year is the interest compounded: '))
t=float(input('what is the amount of years that the account will be left to earn interst: '))
a=p*(1+r/n)**(n*t)
print()
print()
print()
print('annual interest rate:',r)
print('specified years:',t)
print('the amount that will be ther after the number of specified years is',format(a,',.2f'))


# In[ ]:




