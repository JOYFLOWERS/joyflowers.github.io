# Function parameters

# parameter
    # A parameter is a function input specified in a function definition.
# argument
    # An argument is a value provided to a function's parameter during a function call.

#Here is an example ...

def print_cake_area(cake_diameter):
    pi_val = 3.14159265
  
    cake_radius = cake_diameter / 2.0
    cake_area = pi_val * cake_radius * cake_radius
    print(str(cake_diameter) + ' inch cake is ' + str(cake_area) + ' inches squared')


print_cake_area(12)
print_cake_area(16.0)

#Functions can have multiple parameters.  This example finds the volume of a wedding cake.

def print_cake_volume(cake_diameter, cake_height):
    pi_val = 3.14159265
  
    cake_radius = cake_diameter / 2.0
    cake_area = pi_val * cake_radius * cake_radius
    cake_volume = cake_area * cake_height
    print(str(cake_diameter) + ' x ' + str(cake_height) + ' inch cake is ' + str(cake_volume) + ' inches cubed')


print_cake_volume(12, 2)
print_cake_volume(16.0, .75)

###Challenge Activity 1###

# Complete the function definition to output the hours given minutes.

# Sample output with input: 210.0
# 3.5

#def output_minutes_as_hours(orig_minutes):

#     ''' Your solution goes here '''

# minutes = float(input())
# output_minutes_as_hours(minutes)

###Challenge Activity 2###

# Define a function print_total_inches, with parameters num_feet and num_inches, that prints the total number of inches.
# Note: There are 12 inches in a foot.

# Sample output with inputs: 5 8
# Total inches: 68


# ''' Your solution goes here '''

# feet = int(input())
# inches = int(input())
# print_total_inches(feet, inches)