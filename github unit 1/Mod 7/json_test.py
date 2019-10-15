import json

numbers = [18, 10, 555, 12, 23, 189, 22, 1, 1, 0]
file_name = 'numbers.json'

#with open(file_name,'w') as file_object:
#    json.dump(numbers, file_object)
    



with open(file_name) as file_object:
    numbers = json.load(file_object)
    print(numbers,'numbers')
