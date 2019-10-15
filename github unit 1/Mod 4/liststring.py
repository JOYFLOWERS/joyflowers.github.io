#Joy Flowers
#09/24/19
#This program has a user input elements of a list and takes that list and converts it to a string
#The function named process places list items into the string.
#If there is only one element in the list, it does not add the word 'and'
strng = ''
spam = []
while True:
   inp = (input('You are creating a list. Enter an element or just hit enter to stop: '))
   if inp == '':
       break
   spam.append(inp)                           #append elements to the list, spam
#spam = ['apples', 'bananas', 'tofu', 'cats','dogs','animals','1','2','3','4e','4','3','56']
#spam = ['apples']

def process(spam):                            #this function does the conversion
   global strng
   if len(spam) != 1:
       spam.insert((len(spam)-1),'and')       #adds the word 'and' to the list
   for i in range(len(spam)):
       if i == len(spam) - 1 or i == 0:       #don't add the comma before the first or after the 'and'.
           strng = strng + ' ' + spam[i]
       else:
          strng = strng + ', ' + spam[i]
   strng = strng[1:]
   return strng

print('The list is: ',spam)
strng = process(spam)
print('The string is: ', strng)

  
