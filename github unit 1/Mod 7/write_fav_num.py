#Joy Flowers
#10/14/19

#writing the favorite number

file_name = 'fav_num.txt'
with open(file_name, 'w') as file_object:
       name = input('Enter your favorite number: ')
       file_object.write(name)
    
