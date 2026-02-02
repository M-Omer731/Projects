#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Saving Account Balance

# Constant Varibles
INITAL_DEPOSIT=0
INITAL_WITHDRWAL=0
INITAL_INTEREST=0
MONTHS_PER_YEAR=12
def main():
# Ask the user for annual interest rate, starting balance, and number of months
    annual_interest_rate = float(input('Enter the annual interest rate (as a decimal): '))
    starting_balance = float(input('Enter the starting balance: '))
    num_months = int(input('Enter the number of months: '))
    
    balance = starting_balance 
    total_deposits = INITAL_DEPOSIT
    total_withdrawals = INITAL_WITHDRWAL 
    total_interest =  INITAL_INTEREST
    
# Loop for month
    for month in range(1, num_months + 1):
# Ask for amount deposited and validate input
        deposit = float(input(f'Enter amount deposited in Month {month}: '))
        while deposit < 0:
            print('Error. Please enter a non-negative amount.')
            deposit = float(input(f'Enter amount deposited in Month {month}: '))
        total_deposits += deposit
        
# Ask for amount withdrawn and validate input
        withdrawal = float(input(f'Enter amount withdrawn in Month {month}: '))
        while withdrawal < 0:
            print('Error. Please enter a non-negative amount.')
            withdrawal = float(input(f'Enter amount withdrawn in Month {month}: '))
        total_withdrawals += withdrawal
        
# Calculate monthly interest and update balance
        monthly_interest_rate = annual_interest_rate / MONTHS_PER_YEAR
        monthly_interest = balance * monthly_interest_rate
        total_interest += monthly_interest
        balance += deposit - withdrawal + monthly_interest
    
# Display the results
    print()
    print('Ending balance: $', format(balance,'.2f'))
    print('Total deposits: $',format(total_deposits,'.2f'))
    print('Total withdrawals: $',format(total_withdrawals,'.2f'))
    print('Total interest earned: $',format(total_interest,'.2f'))

main()





