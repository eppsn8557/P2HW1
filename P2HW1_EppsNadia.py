# This program calculates and displays travel expenses
# 15 October 2023
# CTI-110 P2HW1-Travel
# Nadia Epps
#
print('This program calculates and displays travel expenses')
print()
budget = float(input('Enter Budget:'))
print()
print('Enter your travel destination:', end=' ')
location = input()
print()
fuel = float(input('How much do you think you will spend on gas?'))
print()
acc = float(input('Approximately, how much will you need for accomodation/hotel?'))
print()
food = float(input('Last, how much do you need for food?'))
print()
print('------------Travel Expenses------------')
print(f'Location:           {location}')
print(f'Initial Budget:     ${budget}')
print(f'Fuel:               ${fuel}')
print(f'Accomodation:       ${acc}')
print(f'Food:               ${food}')
print('----------------------------------------')
rem_bal = budget - fuel - acc - food
print(f'Remaining Balance:  ${rem_bal:.1f}')



