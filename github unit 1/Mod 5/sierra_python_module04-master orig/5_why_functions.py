#With user-defined functions, the main program is easy to understand.

def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    steps_per_minute = 70.0
    calories_per_minute_walking = 3.5

    minutes = num_steps / steps_per_minute
    calories = minutes * calories_per_minute_walking
    return calories

steps = int(input('Enter number of steps walked: '))
print()

#Albeit shorter, without user-defined functions, the main program is harder to read and understand.

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)

feet_per_step = 3
steps_per_minute = 70.0
calories_per_minute_walking = 3.5

steps = int(input('Enter number of steps walked: '))

feet = steps * feet_per_step
print('Feet:', feet)

minutes = steps / steps_per_minute
calories = minutes * calories_per_minute_walking
print('Calories:', calories)
print()

# Modular development
    # Modular development is the process of dividing a program into separate modules that can be developed
    # and tested separately and then integrated into a single program.

###Challenge Activity 1###

#Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles().
#Original main program:

miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print('Miles: %f' % miles_traveled)

#Sample output with inputs: 70.0 100.0
#Miles: 116.666667

# ''' Your solution goes here '''

# miles_per_hour = float(input())
# minutes_traveled = float(input())

# print('Miles: %f' % mph_and_minutes_to_miles(miles_per_hour, minutes_traveled))