# List iteration
# A programmer commonly wants to access each element of a list. Thus, learning how to iterate through a list using a loop is critical.

# Looping through a sequence such as a list is so common that Python supports a construct called a for loop, specifically for iteration purposes.
# The format of a for loop is shown below.

# for my_var in my_list:
#     # Loop body statements go here

# Each iteration of the loop creates a new variable by binding the next element of the list to the name my_var.
# The loop body statements execute during each iteration and can use the current value of my_var as necessary.

# Programs commonly iterate through lists to determine some quantity about the list's items.

#For example, the following program determines the value of the maximum even number in a list:

# User inputs string w/ numbers: '203 12 5 800 -10'
##user_input = input('Enter numbers:')

##tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
##nums = []
##for token in tokens:
##    nums.append(int(token))

# Print each position and number
##print()  # Print a single newline
##for index in range(len(nums)):
##    value = nums[index]
##    print('%d: %d' % (index, value))

# Determine maximum even number
##max_num = None
##for num in nums:
##    if (max_num == None) and (num % 2 == 0):
##        # First even number found
##        max_num = num
##    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
##        # Larger even number found
##        max_num = num

##print('Max even #:', max_num)

#This is an involved example ... 

# If the user enters the numbers 7, -9, 55, 44, 20, -400, 0, 2, then the program will output Max even #: 44. The code uses three for loops.
# The first loop converts the strings obtained from the split() function into integers. The second loop prints each of the entered numbers.
# Note that the first and second loops could easily be combined into a single loop, but the example uses two loops for clarity.
# The third loop evaluates each of the list elements to find the maximum even number.

# Before entering the first loop, the program creates the list nums as an empty list with the statement nums = [].
# The program then appends items to the list inside the first loop. Omitting the initial empty list creation would cause an error
# when the nums.append() function is called, because nums would not actually exist yet.

# The main idea of the code is to use a variable max_num to maintain the largest value seen so far as the program iterates through the list.
# During each iteration, if the list's current element value is even and larger than max_num so far, then the program assigns max_num with current value.
# Using a variable to track a value while iterating over a list is very common behavior.

#You may want to reference this code later; for now, comment it out by selecting the text and pressing Ctrl + K + C.

###Challenge 1###

# Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit.
# For the given program, sum_extra is 8 because 1 + 0 + 7 + 0 is 8.

# Sample output for the given program with input: '101 83 107 90'
# Sum extra: 8

user_input = input('Enter test grades separated by a space: ')
test_grades = list(map(int, user_input.split())) # contains test scores
extra_credit = 0
for i in range(len(test_grades)):            
   if test_grades[i] >= 100:
      extra_credit = extra_credit + (test_grades[i]-100)
print('Sum extra:', extra_credit)



