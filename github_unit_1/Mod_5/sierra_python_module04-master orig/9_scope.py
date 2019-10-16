# scope
# A variable or function object is only visible to part of a program, known as the object's scope.

centimeters_per_inch = 2.54
inches_per_foot = 12

def height_US_to_centimeters(feet, inches):
    """ Converts a height in feet/inches to centimeters."""
    total_inches = (feet * inches_per_foot) + inches  # Total inches
    centimeters = total_inches * centimeters_per_inch
    return centimeters

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_centimeters(feet, inches))

# Can you identify which variables a global and which are local?  Check out the definitions below.

# local variables
# Such variables defined inside a function are called local variables.

# global variable
# A variable defined outside of a function is called a global variable.

# global
# A global statement must be used to change the value of a global variable inside of a function.

# Here is an example of how to modify a global variable ...

employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)