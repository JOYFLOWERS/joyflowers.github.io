#Lesson 1 Python Basics Practice
#Joy Flowers
#Aug 31, 2019

#part 1 change string value and print
name='My name is Joy...'
print(name)
name="...but my dad calls me JoJo."
print(name)

#part 2 famous quote and author
quote='Jesus said, "Do unto others as you would have them do unto you."'
print(quote)

#part 3 Favorite number
mynum=23
print('My favorite number is ' + str(mynum)+'.')

#part 4 Length of rv sentence
#character counting includes all characters in a sentence,
#and not just letters.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
'Tis some visitor, I muttered, tapping at my chamber door;
Only this and nothing more."""
num_chars=len(rv)
print('The number of characters in the variable rv is',str(num_chars)+'.')
