#! /usr/bin/env python3
# Joy Flowers
# 10/7/19
# String handling with error handling

# Challenge #1: String Slicing

# Assign sub_lyric by slicing rhyme_lyric from start_index to end_index which are given as inputs.
    # Sample output with inputs: 4 7
    # cow
start_index = 30
end_index = 30
while (start_index > 29) or (end_index < start_index) or (end_index > 29): 
   rhyme_lyric = 'The cow jumped over the moon.'
   try:
      start_index = int(input('Enter starting index from 0 to 29: '))
      end_index = int(input('Enter ending index as a number between starting_index and 29: '))
   except ValueError:
      print("Enter a number between 1 and 29: ")
   except NameError:
      print("Enter a number between 1 and 29: ")
   if start_index > len(rhyme_lyric)-1:
      print('Choose an index less than 30')
   if end_index < start_index or end_index > len(rhyme_lyric)-1:
      print('Choose an index greater than the start_index but less than 30')
sub_lyric = rhyme_lyric[start_index:end_index]
print(sub_lyric)

# Challenge #2: Format Temperature Output

# Print air_temperature with 1 decimal point followed by C.
    # Sample output with input: 36.4158102
    # 36.4C

while True:
   try:
      air_temperature = float(input('Enter air temperature in Celcius ie. 36.4158102: '))
      break
   except ValueError:
       print("Enter a valid number")
   except NameError:
      print("Enter a valid number")
print("The temperature you entered is roughly % 2.1f" % air_temperature)

# Challege #3: Find Abbreviations

# Complete the if-else statement to print 'LOL means laughing out loud' if user_tweet contains 'LOL'.
    # Sample output with input: 'I was LOL during the whole movie!'
    # LOL means laughing out loud.

user_tweet = input('Enter a string with LOL or not: ')

if user_tweet.find('LOL') != -1:
   print('LOL means laughing out loud.')
else:
   print('No abbreviation.')

# Challenge #4: Replace Abbreviations

# Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL' with 'talk to you later'.
    # Sample output with input: 'Gotta go. I will TTYL.'

user_tweet = input('Enter a tweet abbreviation TTYL: ')

decoded_tweet = user_tweet.replace('TTYL','talk to you later')
print(decoded_tweet)

# Challenge 5: Extract Area Code

# Assign number_segments with phone_number split by the hyphens.
    # Sample output with input: '977-555-3221'
    # Area code: 977
while True:
   phone_number = input('Enter a phone number: in the format ###-###-#### ')
   if len(phone_number) >= 3:
      number_segments = phone_number.split('-')
      area_code = number_segments[0]
      print('Area code:', area_code)
      break
   else:
      print('Enter atleast 3 digits: ')

# Challenge 6: Check for integer in string

# Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input,
# and outputs yes if every character is a digit 0-9.

# Ex: If the input is:
    # 1995
    # the output is:
        # yes
# Ex: If the input is:
    # 42,000
    # # or any string with a non-integer character, the output is:
        # no
all_int=True
user_string = input('Enter an integer or not:')
if user_string.isdecimal():
    print('yes')
else:
    print('no')

# Challenge 7: Name Format

# Many documents use a specific format for a person's name. Write a program whose input is: firstName middleName lastName,
# and whose output is: lastName, firstName middleInitial.

# Ex: If the input is:
    # Pat Silly Doe
    # the output is:
        # Doe, Pat S.

# If the input has the form firstName lastName, the output is lastName, firstName.

# Ex: If the input is:
    # Julia Clark
    # the output is:
        # Clark, Julia
while True:
   name = input('Enter a name in the format first name middle name last name separated by a space: ')
   name_split = name.split()
   try:
      if len(name_split) == 2:
         print(str(name_split[1]) + ', ' + str(name_split[0]))
      else:
         print(str(name_split[2]) + ', ' + str(name_split[0]) + ' ' + str(name_split[1])[0:1] + '.')
      break
   except IndexError:
      print('Enter two or three names separated by a space')
   
# Challenge 8: Palindrome

# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# Ex: If the input is:
    # bob
    # the output is:
        # bob is a palindrome
# Ex: If the input is:
    # bobby
    # the output is:
        # bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

pal = input('Enter a string - maybe a pallidrome: ')
str_rev = pal[len(pal)::-1]
print(str_rev)
if (pal) == str_rev:
   print("It's a pallidrome")
else:
   print("It's not a pallidrome")

