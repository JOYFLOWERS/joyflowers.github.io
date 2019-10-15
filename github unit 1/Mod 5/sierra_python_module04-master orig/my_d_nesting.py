# List Nesting

# Since a list can contain any type of object as an element, and a list is itself an object, a list can contain another list as an element.
# Such embedding of a list inside another list is known as list nesting.Ex: The code my_list = [[5, 13], [50, 75, 100]] creates a list with two elements
# that are each another list.

my_list = [[10, 20], [30, 40]]
print('First nested list:', my_list[0])
print('Second nested list:', my_list[1])
print('Element 0 of first nested list:', my_list[0][0])

# A list is a single-dimensional sequence of items, like a series of times, data samples, daily temperatures, etc.
# List nesting allows for a programmer to also create a multi-dimensional data structure, the simplest being a two-dimensional table,
# like a spreadsheet or tic-tac-toe board. The following code defines a two-dimensional table using nested lists:

tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])

# The example above creates a variable tic_tac_toe that represents a 2-dimensional table with 3 rows and 3 columns, for 3*3=9 total table entries.
# Each row in the table is a nested list. Table entries can be accessed by specifying the desired row and column: tic_tac_toe [1][1] accesses the middle square
# in row 1, column 1 (starting from 0), which has a value of 'X'. The following code illustrates:

currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

###Challenge 1###

# Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

# Sample output with input: '1 2 3,2 4 6,3 6 9':
# 1 | 2 | 3
# 2 | 4 | 6
# 3 | 6 | 9

user_input= input('Enter nine numbers in the following format 1 2 3,2 4 6,3 6 9 ')
lines = user_input.split(',')

# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]
for i in range(len(mult_table)):
   for j in range(len(mult_table)):
      print(mult_table[i][j],'|',end=' ')
   print('')  


