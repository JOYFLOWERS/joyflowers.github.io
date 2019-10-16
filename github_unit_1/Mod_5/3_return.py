#Returning a value from a function

# return statement
    # A function may return one value using a return statement.

# None
    # None is a special keyword that indicates no value.

#An example ...

def compute_square(num_to_square):
    return num_to_square * num_to_square


num_squared = compute_square(7)

print('7 squared is', num_squared)
print()

# Step 1 - call compute_square and pass in the value 7.
# Step 2 - compute the square of num_to_square and return the result.
# Step 3 - num_squared is assigned the return value of compute_square(7).
# Step 4 - 49 is printed.

#Another example of return in action

CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * INCHES_PER_FOOT + inches
    cm = total_inches * CM_PER_INCH
    return cm

feet = 6
inches = 4
	
centimeters = height_US_to_cm(feet, inches)
print('Centimeters:', centimeters)
print()

###Challenge Activity 1###

# Complete the program by writing and calling a function that converts a temperature from Celsius into Fahrenheit.
# Use the formula F = C x 9/5 + 32. Test your program knowing that 50 Celsius is 122 Fahrenheit.

def c_to_f(C):
    temp_f = C * (9/5) + 32
    return  temp_f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = c_to_f(temp_c)
# FIXME: Call conversion function
#temp_f = ??

#FIXME: Print result
print('Fahrenheit:' , temp_f)
#hierarchical function calls
    #A function's statements may include function calls, known as hierarchical function calls or nested function calls.
#nested function calls
    #A function's statements may include function calls, known as hierarchical function calls or nested function calls.

#An example ...

def calc_circle_area(circle_diameter):
    pi_val = 3.14159265
   
    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area
	
def cake_calories(cake_diameter):
    calories_per_square_inch = 16.7    # Chocolate cake
   
    total_calories = calc_circle_area(cake_diameter) * calories_per_square_inch
    return total_calories
	
	
#print('12 inch cake has %.2f calories.'% cake_calories(12.0))
#print('14 inch cake has %.2f calories.'% cake_calories(14.0))

###Challenge Activity 2###

# Assign max_sum with the greater of num_a and num_b, PLUS the greater of num_y and num_z. Use just one statement.
# Hint: Call find_max() twice in an expression.

# Sample output with inputs: 5.0 10.0 3.0 7.0
# max_sum is: 17.0

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

soln_a = find_max(num_a,num_b)
soln_x = find_max(num_y,num_z)
soln = soln_a + soln_x
print("The sum of the max values of the two pairs of numbers is: ",str(soln))
''' Your solution goes here '''

#print('max_sum is:', max_sum)

###Challenge Activity 3 - Volume of a Pyramid###

# Define a function pyramid_volume with parameters base_length, base_width, and pyramid_height, that returns the volume of a pyramid with a rectangular base.

# Sample output with inputs: 4.5 2.1 3.0
# Volume for 4.5, 2.1, 3.0 is: 9.45
# Relevant geometry equations:
# Volume = base area x height x 1/3
# Base area = base length x base width.

# ''' Your solution goes here '''

# length = float(input())
# width = float(input())
# height = float(input())
# print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))