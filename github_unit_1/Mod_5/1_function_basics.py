# Function Basics

# function
    # A function is a named series of statements.
# function definition
    # A function definition consists of the new function's name and a block of statements.
# function call
    # A function call is an invocation of the function's name, causing the function's statements to execute.
# def
    # The def keyword is used to create new functions.

#Here is an example:

def print_cake_area():
    pi_val = 3.14159265
  
    cake_diameter = 12.0
    cake_radius = cake_diameter / 2.0
    cake_area = pi_val * cake_radius * cake_radius
    print(str(cake_diameter) + ' inch cake is ' + str(cake_area) + ' inches squared')


# print_cake_area()

# The function call jumps execution to the function's statements.
# After the last statement, execution returns to the original location.
# Check out the following example and see if you can predict/trace how the function is executed.

# def print_face():
#     face_char = 'o'
#     print('  ', face_char, ' ', face_char)  # Print eyes
#     print('    ', face_char)                # Print nose
#     print('  ', face_char*5)                # Print mouth

# print('Say cheese!')

# print_face()	

# print('Did it turn out ok?')

###Challenge Activity 1###
#    print_pattern() prints 5 characters. Call print_pattern() twice to print 10 characters. Example output:
#    *****
 #   *****

def print_pattern():
   print('*****')

print_pattern()
print_pattern()
''' Your solution goes here '''

###Challenge Activity 2###

# Define print_shape() to print the below shape. Example output:
# ***
# ***
# ***

# ''' Your solution goes here '''
def print_shape():
   print('***')
   print('***')
   print('***')   
print_shape()

    