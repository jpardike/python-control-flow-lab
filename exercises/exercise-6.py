# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month_input = input('Enter the month of the year (Jan - Dec): ')

day_input = input('Enter the day of the month: ')

convert_to_num = int(day_input)

winter_months = ['Jan', 'Feb']
spring_months = ['Apr', 'May']
summer_months = ['Jul', 'Aug']
fall_months = ['Oct', 'Nov']

winter_message = f'{month_input} {day_input} is in Winter'
spring_message = f'{month_input} {day_input} is in Spring'
summer_message = f'{month_input} {day_input} is in Summer'
fall_message = f'{month_input} {day_input} is in Fall'

if month_input in winter_months:
    print(winter_message)
elif month_input in spring_months:
    print(spring_message)
elif month_input in summer_months:
    print(fall_message)
elif month_input in fall_months:
    print(fall_message)
else:
    if month_input == 'Mar':
        if convert_to_num <= 19:
            print(winter_message)
        else:
            print(spring_message)
    elif month_input == 'Jun':
        if convert_to_num <= 20:
            print(spring_message)
        else:
            print(summer_message)
    elif month_input == 'Sep':
        if convert_to_num <= 21:
            print(summer_message)
        else:
            print(fall_message)
    elif month_input == 'Dec':
        if convert_to_num <= 20:
            print(fall_message)
        else:
            print(winter_message)