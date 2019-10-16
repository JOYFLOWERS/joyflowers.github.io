# The list object type is one of the most important and often used types in a Python program.
# A list is a container, which is an object that groups related objects together. A list is also a sequence;
# thus, the contained objects maintain a left-to-right positional ordering.
# Elements of the list can be accessed via indexing operations that specify the position of the desired element in the list.
# Each element in a list can be a different type such as strings, integers, floats, or even other lists.

# A list can also be created using the built-in list() function. The list() function accepts a single iterable object argument,
# such as a string, list, or tuple, and returns a new list object. Ex: list('abc') creates a new list with the elements ['a', 'b', 'c'].

#index
    #An index is an integer corresponding to a specific position in the list's sequence of elements.

# mutable
    # Unlike the string sequence type, a list is mutable and is thus able to grow and shrink without the program having to replace the
    # entire list with an updated copy.

# in-place modification 
    # Such growing and shrinking capability is called in-place modification.

# Add print statememts to the code below to see how in-place modification works:

my_list  = [ 'h', 'e', 'l', 'l', 'o' ]
my_list[len(my_list):] = [ ' ', 'w', 'o', 'r', 'l', 'd', '.' ]
my_list[11] = '!'
del my_list[5]

# Another example

my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams  # Create a shared reference to same list
	
my_teams[1] = 'Lakers'  # Modify list element
	
print('My teams are:', my_teams)  # Both variables have changed
print('Your teams are:', your_teams)  # Both variables have changed

# Lists can be copied

my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams[:]  # Assign your_teams to a COPY of my_teams
	
my_teams[1] = 'Lakers'  # Modify list element
	
print('My teams are:', my_teams)  # List element has changed
print('Your teams are:', your_teams)  # List element has not changed

# List items can be changed in place ...

colors = ['red', 'green', 'blue']

colors[1] = 'yellow'  # Change list element
# print colors...

fav_color = colors[2]  # Bind to 'blue'
fav_color = 'turquoise'  # List not altered
# print colors...

###Challenge 1###

# Modify short_names by deleting the first element and changing the last element to Joe.

# Sample output with input: 'Gertrude Sam Ann Joseph'
# ['Sam', 'Ann', 'Joe']

# user_input = input()
# short_names = user_input.split()

# ''' Your solution goes here '''

# print(short_names)



