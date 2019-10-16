# Joy Flowers
# 09/24/19
# This program shows the Collatz sequence. If the number is even,
# divide it by 2 (no remainder) and if it is odd, multiply by 3 and add 1.
# Also, make sure that only an integer is entered.

while True:
    try:
        number = int(input('Enter number: '))
        break
    except ValueError:             #Make sure it is an integer
        print('Enter an integer, try again')
        
def collatz():                     #function is collatz
    global number                  #number is passed out of the function
    if (number % 2) == 0:          #if the number is even
        number = number // 2
    else:                          #if the number is odd 
        number = number * 3 + 1
    print(number)
    return number

while number != 1:
    number = collatz()

