#Joy Flowers
#09/16/19
#This is a 4 part algorithm

#Part 1 generates a random 8-byte password with the first character
#as uppercase, the last byte as a number, and the rest as lowercase characters.

#Part 2 concatenates four randomly-generated words and uses this as a password.
#A dash was put between the words to distiguish them.

#Part 3 takes the password from Part 2 and substitutes to make the password harder to hack.
#For example, a '3' is substituted for 'e', a '0' is substituted for 'o, and '1' is substituted for 'l'

#Part 4 has the user enter a four-letter word (lowercase only) and determines what the word is. It lists the
#word it found and tells how many tries it took to find the password.

import random

#Part 1 - 8-byte password with uppercase, lowercase and number
pwd1 = ''
lc_choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uc_choices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nm_choices = ['0','1','2','3','4','5','6','7','8','9']
for i in range(8):
   if i == 0:    #first position is a capital
      one_byte = random.choice(uc_choices)
   elif i == 7:  #last position is a number
      one_byte = random.choice(nm_choices)
   else:
       one_byte = random.choice(lc_choices) #all others are lowercase
   pwd1 = pwd1 + one_byte
print("Part 1: Password is ",pwd1)

#Part 2 - four words concatenated together
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
pwd2 = ''
for i in range(4):
   one_word = random.choice(WORDS)
   if i == 0:
       one_word = one_word.capitalize()
   pwd2 = pwd2 + '-' + one_word
print("Part 2: Password is ",pwd2)

#Part 3 - substituted password making the password more difficult to guess
pwd3 = pwd2.replace('o','0')
pwd3 = pwd3.replace('e','3')
pwd3 = pwd3.replace('l','1')
print("Part 3: Password is ",pwd3)

#Part 4 - guess a four-letter lowercase password and tell how many tries it took
pwd4 = ''
cnt=4 
the_word = input("Enter a four-letter word, all lowercase, no profanity, please: ")
#lc_choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while pwd4 != the_word:
   for j in range(4):
      for i in range(26):
         if lc_choices[i] == the_word[j]:
            pwd4 = pwd4 + lc_choices[i]
            break
         else:
            cnt = cnt + 1
print("Part 4: Your word ",pwd4," was found after ",str(cnt)," tries")
