#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Rainfall Program

# Constant Varibles 
INITAL_RAINFALL=0
MONTHS_PER_YEAR=12

def main():
# Ask the user for the number of years
    num_years = int(input('Enter the number of years: '))
    
    total_rainfall = INITAL_RAINFALL
    num_months = num_years * MONTHS_PER_YEAR
    
# Outer loop for year
    for year in range(1, num_years + 1):
# Inner loop for month
        for month in range(1, 13):
            rainfall = float(input(f'Enter inches of rainfall for Year {year}, Month {month}: '))
            total_rainfall += rainfall
    
# Calculate average rainfall per month
    average_rainfall = total_rainfall / num_months
    
# Display the results
    print()
    print(f'Number of months: {num_months}')
    print(f'Total inches of rainfall: {total_rainfall}')
    print(f'Average rainfall per month: {average_rainfall:.2f} inches')
main()
