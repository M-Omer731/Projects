#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    location = input("Where would you be going for summer vacation?: ")
    if location == 'Hawaii' or location == 'Bahamas':
        print(f"Chosen vacation destination: {location}")
        carrier(location)
    else:
        print('Please enter a valid location (Hawaii or Bahamas).')

def calculation(airline, airfare, num_passengers, num_underage):
    num_adults= num_passengers-num_underage
    total_adult_fare = airfare * num_adults
    total_underage_fare = airfare * num_underage * 0.75  # 25% discount for underage travelers
    total_cost = total_adult_fare + total_underage_fare
    print("\nVacation Details:")
    print(f"Round trip price for adult: ${airfare}")
    print(f"Airfare for person(s) under the age of 18: ${total_underage_fare:.2f}")
    print(f"Airline for flight: {airline}")
    print(f"Total cost of vacation: ${total_cost:.2f}")

def passenger(location, airline, airfare):
    num_passengers = int(input("Enter the number of passengers (1-3): "))
    if num_passengers not in [1, 2, 3]:
        print("Invalid number of passengers.")
    else:
        num_underage = int(input("Enter the number of passengers under 18: "))
        calculation(airline, airfare, num_passengers, num_underage)

def carrier(location):
    if location == 'Hawaii':
        airline_choice = input("Choose an airline (1 for US Air, 2 for Delta): ")
        if airline_choice == '1':
            airline = 'US Air'
            airfare = float(input('How much is the round trip airfare for this flight?: '))
            passenger(location, airline, airfare)
        elif airline_choice == '2':
            airline = 'Delta'
            airfare = float(input('How much is the round trip airfare for this flight?: '))
            passenger(location, airline, airfare)
        else:
            print("Invalid choice.")
    elif location == 'Bahamas':
        airline_choice = input("Choose an airline (1 for US Air, 2 for Delta): ")
        if airline_choice == '1':
            airline = 'US Air'
            airfare = float(input('How much is the round trip airfare for this flight?: '))
            passenger(location, airline, airfare)
        elif airline_choice == '2':
            airline = 'Delta'
            airfare = float(input('How much is the round trip airfare for this flight?: '))
            passenger(location, airline, airfare)
        else:
            print("Invalid choice.")
    else:
        print('Please enter a valid location (Hawaii or Bahamas).')

main()


# In[ ]:




