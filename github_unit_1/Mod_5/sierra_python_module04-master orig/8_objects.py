#In Python, functions are also objects (they have properties, values, types).
#This allows for us to reuse them in other variable and functions.  The example below creates ASCII art and is called twice.

def print_face():
   # print face statements...
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return


print_face()

func = print_face
func()

#Can you trace the code?

#Functions can also be passed as arguments to other functions ...

def human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(monkey_head)
elif choice == 2:
    print_figure(human_head)

###Challenge 1###