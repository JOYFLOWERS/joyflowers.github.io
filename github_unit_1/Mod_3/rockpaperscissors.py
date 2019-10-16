#Joy Flowers
#09/15/19
#This program plays the game Rock, Paper, Scissors
#The first is input by the user and the second is randomly chosen by computer.

import random
proceed = ' '
while proceed != 'X':
   user_input = input("Enter your choice, rock, paper or scissors, all lowercase: ")
#the program uses a specially sequenced list so that each beats the one preceding it
#note that I have forced scissors to precede paper.
   choices = ['paper','rock','scissors']
   computer_input = random.choice(choices)
   print("I, the great and mighty computer choose ",computer_input)
   user_input_loc = choices.index(user_input)
   computer_input_loc = choices.index(computer_input)
   if user_input_loc == computer_input_loc:
      print("It's a tie - try again")
      continue
   if user_input_loc < computer_input_loc:
#special case wrap around override       
      if (user_input_loc == 0 and computer_input_loc == 2):
         print("I, the great and mighty computer, win")
      else:
         print("You won this one")
   else:
#special case wrap around override       
      if (user_input_loc == 2 and computer_input_loc == 0):
         print("You won this one")
      else:
         print("I, the great and mighty computer, win")
   print(" ")      
   proceed = input("Press X to stop or any other key to continue: ") 
        


