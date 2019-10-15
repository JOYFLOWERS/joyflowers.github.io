#writing to files
#create a file

file_name = 'programming.txt'

#with open(file_name, 'w') as file_object:
#    file_object.write('Hello, World! and Joy\n')
    #
#    file_object.write('These are multiple lines.\n')

#with open(file_name, 'a') as file_object:
#    file_object.write('more, more\n')
    
#    file_object.write('and more.\n')

file_name = 'guest_book.txt'
with open(file_name, 'w') as file_object:

   name = '1'
   while name != '\n':
       name = input('Enter guest name: ')
       name += '\n'
       file_object.write(name)
    
