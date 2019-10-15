#Joy Flowers
#09/30/19
#Combination of Python Challenge Activities (#1 to #9)

#####################################1 - function_basics.py
#Challenge 1 - Print a pattern
def print_pattern():
   print('*****')
print('#1 - Challenge 1-1 Print a pattern')
print_pattern()
print_pattern()

#Challenge 2 - Print another pattern
def print_shape():
   print('***')
   print('***')
   print('***')   
print('#1 - Challenge 1-2 Print another pattern')
print_shape()

#####################################2 - parameters.py

# Complete the function definition to output the hours given minutes.

# Sample output with input: 210.0
# 3.5

def output_minutes_as_hours(orig_minutes):
     hours = orig_minutes / 60
     return hours
print('Challenge 2-1 Convert minutes to hours')
minutes = float(input("Enter minutes: "))
hours = output_minutes_as_hours(minutes)
print('Hours: ',hours)


#Define a function print_total_inches, with parameters num_feet and num_inches, that prints the total number of inches.
#Note: There are 12 inches in a foot.

#Sample output with inputs: 5 8
#Total inches: 68

def print_total_inches(ft,inch):
    total_inches = ft*12 + inch
    return(total_inches)
print('#2 - Challenge 2-2 Convert feet and inches to inches')
feet = int(input("Feet: "))
inches = int(input("Inches: "))
total_inches = print_total_inches(feet, inches)
print("Total inches are: ", total_inches)

#####################################3 - returns.py
# Complete the program by writing and calling a function that converts a temperature from Celsius into Fahrenheit.
# Challenge 3-1
#Use the formula F = C x 9/5 + 32. Test your program knowing that 50 Celsius is 122 Fahrenheit.

def c_to_f(C):
    temp_f = C * (9/5) + 32
    return  temp_f
print('Challenge 3-1 Convert Celsius to Farenheit')
temp_c = float(input('Enter temperature in Celsius: '))
temp_f = c_to_f(temp_c)

print('Fahrenheit:' , temp_f)

# Challenge 3-2
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
print('Challenge 3-2 Take the sum of the max of 2 numbers and next two numbers')
num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

soln_a = find_max(num_a,num_b)
soln_x = find_max(num_y,num_z)
soln = soln_a + soln_x
print("The sum of the max values of the two pairs of numbers is: ",str(soln))

#####################################4 dynamic.py
# There is no challenge activity for #4, so
# just copy what is here
def add(x, y):
    return x + y
print('#4 Dynamically adds values; integers or strings')	
print('add(5, 7) is', add(5, 7))
print("add('Tora', 'Bora') is", add('Tora', 'Bora'))

####################################5 why_functions.py
# Challenge 1
#Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles().
#Original main program:
print('#5 - Challenge 5-1 Convert miles and minutes to miles per hour - mph')
miles_per_hour = float(input('Enter miles per hour: '))
minutes_traveled = float(input('Enter minutes travelled: '))

def mph_and_minutes_to_miles(miles_per_hour,minutes_traveled):
   hours_traveled = minutes_traveled / 60.0
   miles_traveled = hours_traveled * miles_per_hour
   return miles_traveled
miles_traveled = mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)   

#Sample output with inputs: 70.0 100.0
#Miles: 116.666667

print('Miles: %f' % mph_and_minutes_to_miles(miles_per_hour, minutes_traveled))

####################################6 stub.py
# in steps to calories, the
# Define stubs for the functions get_user_num() and compute_avg(). Each stub should print "FIXME: Finish function_name()"
# followed by a newline, and should return -1. Each stub must also contain the function's parameters.

# Sample output with two calls to get_user_num() and one call to compute_avg():
def get_user_num():
   user_num = int(input('Enter a number: '))
   return user_num

def compute_avg(user_num1,user_num2):
   avg_result = (user_num1 + user_num2)/2
   return avg_result
    
user_num1 = 0
user_num2 = 0
avg_result = 0

print('#6 Challenge 6-1 Compute the average of two numbers')
user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)

####################################7 complex functions.py

# Write a function call using the ebay_fee() function to determine the fee for a selling price of 15.23,
# storing the result in a variable named my_fee.

def ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)
    return fee

print('#7 Challenge 7-1 Compute eBay fee for selling price of $15.23:')
#selling_price = float(input('Enter item selling price (ex: 65.00): '))
#print('Ebay fee: $', ebay_fee(selling_price))
my_fee = ebay_fee(15.23)    #Added to find the fee of $2.48
print('Ebay fee: $'+'{:.2f}'.format(my_fee))

#For any call to ebay_fee(), how many assignment statements will execute? 5
#What does ebay_fee() return if its argument is 0.0? $0.50
#What does ebay_fee() return if its argument is 100.0?  $9.50

print('#7 Challenge 7-2 Enter ounces in a bag of popcorn and output evaluates the size')
#Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small".
#If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by "seconds". End with a newline.

def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
       print("Too large")
    else:
        print(6*bag_ounces,'seconds')
    print('')    
        
user_ounces = int(input('Enter ounces in a bag of popcorn: '))        
print_popcorn_time(user_ounces)

# Write a function shampoo_instructions() with parameter num_cycles. If num_cycles is less than 1, print "Too few.".
# If more than 4, print "Too many.". Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".

# Sample output with input: 2
# 1 : Lather and rinse.
# 2 : Lather and rinse.
# Done.
 
# Hint: Define and use a loop variable.

# ''' Your solution goes here '''
def shampoo_instructions(num_cycles):
   if num_cycles < 1:
      print("Too few")
   elif num_cycles > 4:
      print("Too many")
   else:
      for i in range(user_cycles):
         print(i+1,': Lather and rinse')
print('#7 Challenge 7-3 Number of shampoo cycles')
user_cycles = int(input('Enter number of times you shampoo your hair:'))
shampoo_instructions(user_cycles)

####################################8 objects.py
print('There is no Challenge activity for program 8')
####################################9 scope.py
print('There is no Challenge activity for program 9')

####################################a_lists.py

# Modify short_names by deleting the first element and changing the last element to Joe.

# Sample output with input: 'Gertrude Sam Ann Joseph'
# ['Sam', 'Ann', 'Joe']
print('Challenge a-1 - Lists: Takes a list of names, deletes first one and adds Joe to end')
user_input = input('Enter a list of names separated by a space: ')
short_names = user_input.split()
print('Before: ', short_names)
del short_names[0]
short_names.append('Joe')
print('After: ', short_names)

####################################b_methods.py

# Sort short_names in reverse alphabetic order.

# Sample output with input: 'Jan Sam Ann Joe Tod'
# ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']

print('Challenge b-1 - Methods: Takes a list of names above and sorts it')
short_names.sort()
print(short_names)

####################################c_looping.py

# Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit.
# For the given program, sum_extra is 8 because 1 + 0 + 7 + 0 is 8.

# Sample output for the given program with input: '101 83 107 90'
# Sum extra: 8
print('Challenge c-1 - Looping - This takes test scores and calculates extra credit if over score over 100')
user_input = input('Enter test grades separated by a space: ')
test_grades = list(map(int, user_input.split())) # contains test scores
extra_credit = 0
for i in range(len(test_grades)):            
   if test_grades[i] >= 100:
      extra_credit = extra_credit + (test_grades[i]-100)
print('Sum extra:', extra_credit)

####################################d_nesting.py

# Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

# Sample output with input: '1 2 3,2 4 6,3 6 9':
# 1 | 2 | 3
# 2 | 4 | 6
# 3 | 6 | 9
print('Challenge d-1 Nesting - Enter a 9 digits and they will be displayed into a square')
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


