#!/usr/bin/env python
# coding: utf-8

# In[2]:


BROKERCOMMISSIONRATE= 0.03
numberofshares=int(input('please enter # of stock shares joe purchased? '))
pricepershares=float(input('How much did he pay per share? '))
boughtstockprice=numberofshares*pricepershares
stockbrokecommission=boughtstockprice*BROKERCOMMISSIONRATE
print('Joe initally paid', format(boughtstockprice, ',.2f') ,'for the stock')
print('After joes inital purchase of the stock, his stockbroker made:', format(stockbrokecommission, ',.2f'))
print()
print()
sharessold=int(input('how many of the shares did joe sell? '))
joeshareprice=float(input('how much did joe charge per share? '))
soldstockprice=sharessold*joeshareprice
commissionafterstocksold=soldstockprice*BROKERCOMMISSIONRATE
print('Joe sold the stock for,', format(soldstockprice, ',.2f'))
print('After joe sold the stock, his stockbroker made:', format(commissionafterstocksold,',.2f'))
print()
print()
profit=soldstockprice-boughtstockprice-stockbrokecommission-commissionafterstocksold
print('After selling the stock and paying his stockbroker, joe was left wit:', format(profit,',.2f'))
if profit > 0:
    print('joe made a proft of:', format(profit,',.2f') ,'dollars')
else:
    print('joe didnt make any money on this investment, he lost:', format(profit,',.2f') ,'dollars')


# In[ ]:





# In[ ]:




