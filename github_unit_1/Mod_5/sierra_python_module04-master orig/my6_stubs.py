# incremental development
    # Programs are typically written using incremental development, meaning a small amount of code is written and tested,
    # then a small amount more (an incremental amount) is written and tested, and so on.
# function stubs
    # To assist with the incremental development process, programmers commonly introduce function stubs, which are function definitions whose statements haven't been written yet.
# pass
    # One approach is to use the pass keyword, which performs no operation except to act as a placeholder for a required statement.

#An example ...

def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    pass  

steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)

#Can you predict what this code will do?  Is there a 'None'?  #Feel free to comment it up!

#A simple print statement can also alert a user or teammate of a stub ...

def steps_to_calories(num_steps):
    print('FIXME: finish steps_to_calories')
    return -1

#Replace this stub in the code above.  Predict and try out!

# NotImplementedError
    # A NotImplementedError can be generated with the statement raise NotImplementedError.

# The example below demonstrates the raise statement stopping the program from running, because there is no user input.

import math

def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError
        
def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter

coordinates = get_points(3)
print('co: ',coordinates)
print('Perimeter of triangle:', get_perimeter_length(coordinates))

###Challenge Activity 1###

# Define stubs for the functions get_user_num() and compute_avg(). Each stub should print "FIXME: Finish function_name()"
# followed by a newline, and should return -1. Each stub must also contain the function's parameters.

# Sample output with two calls to get_user_num() and one call to compute_avg():
# FIXME: Finish get_user_num()
# FIXME: Finish get_user_num()
# FIXME: Finish compute_avg()
# Avg: -1

#Starter Code
# ''' Your solution goes here '''

# user_num1 = 0
# user_num2 = 0
# avg_result = 0

# user_num1 = get_user_num()
# user_num2 = get_user_num()
# avg_result = compute_avg(user_num1, user_num2)

# print('Avg:', avg_result)
