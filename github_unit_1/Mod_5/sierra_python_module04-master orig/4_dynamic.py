#Dynamic and static typing
    #A programmer can pass any type of object as an argument to a function. Consider a function add(x, y) that adds the two parameters:

    #A programmer can call the add() function using two integer arguments, as in add(5, 7), which returns a value of 12.
    #Alternatively, a programmer can pass in two string arguments, as in add('Tora', 'Bora'), which would concatenate the two strings
    #and return 'ToraBora'.

# An example ...

def add(x, y):
    return x + y
	
print('add(5, 7) is', add(5, 7))
print("add('Tora', 'Bora') is", add('Tora', 'Bora'))

# polymorphism
    #The function's behavior of being able to add together different types is a concept called polymorphism.
# dynamic typing
    #Python uses dynamic typing to determine the type of objects as a program executes.
# static typing
    #In contrast to dynamic typing, many other language like C, C++, and Java use static typing,
    #which requires the programmer to define the type of every variable and every function parameter in a program's source code.