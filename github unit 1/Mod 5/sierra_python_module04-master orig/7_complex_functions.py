#Functions can include conditionals and loops.  Check out the example of an ebay calculator below.

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

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', ebay_fee(selling_price))
#my_fee = ebay_fee(15.23)
#print('Ebay fee: $', my_fee)

#For any call to ebay_fee(), how many assignment statements will execute?
#What does ebay_fee() return if its argument is 0.0?
#What does ebay_fee() return if its argument is 100.0?

###Challenge 1###

# Write a function call using the ebay_fee() function to determine the fee for a selling price of 15.23,
# storing the result in a variable named my_fee.

###Challenge 2###

#Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small".
#If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by "seconds". End with a newline.

# ''' Your solution goes here '''

# user_ounces = int(input())
# print_popcorn_time(user_ounces)

###Challenge 3####

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

user_cycles = int(input('Enter number of times you shampoo your hair:'))
shampoo_instructions(user_cycles)

