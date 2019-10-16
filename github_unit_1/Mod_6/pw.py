#! /usr/bin/env python3
# The above line is used for a Mac.
# If running in Windows, replace /usr/bin/env python3 with python3

# pw.py - A Password Locker Systems (PLS) named Phyllis.
# Joy Flowers
# 10/11/19
# This Password Locker System manages passwords for you so you do not have to keep
# track of them. It prompts for URL and password. It encrypts the password and saves it.
# When retrieving the password, it copies it to the clipboard after decrypting and
# launches the website. It also will generate a password upon request.

# Future Enhancements could include: Adding multiple users, more error validation, saving
# the added data to a file, and reading from that file.

#NEW FEATURE: Launches Website after retrieving OR after adding a new password

##### TEST CASE ##############
#Launch the program by running the following command line:
#
#   ./pw.py service 
#   (where service is the service or website you need the password for)
#
#Examples:
#
#./pw.py amazon
#./pw.py expedia
#./pw.py gmail
#
#To see all of the features, try running the program as follows:
#After entering the username as jflowers and the (master) passphrase as ‘GoPhyllisGoPhyllis’,
#
#     At the menu, enter option 3 to generate a password.
# 	        Copy the password
#     At the menu, enter option 1 to add a password.
#		Enter www.amazon.com (as suggested in the prompt)
#		Enter amazon 		(as suggested in the prompt)
#		Paste the generated password when prompted for it.
#           Respond N to not launch the website
#     At the menu, enter option 2 to retrieve the password.
#        Press enter to launch the website.
#        Note: the website will not automatically return you 
#        to the program. 
#     Return to the program and enter option 4 to exit from it.
#
#
##### END TEST CASE ##########

# START PROGRAM
def intro():
   global option, username
# This provides the user with an introduction to the PL system.
   print("""

Hi, I am Phyllis, your Password Locker System (PLS).
I will help you to:
   * Store passwords for websites and other software
   * Retrieve your password when you need it and copy
     it to the clipboard so you don't have to remember it,
     and then launch the associated website
   * Encrypt/decrypt to keep your passwords secure
   * Generate a password for you
   
Once you enter your username and master passphrase,
we can start with whatever you like: """)
   passphrase = 'GoPhyllisGoPhyllis'
#   passphrase = 'Go'
# Enter user name and passphrase
   master=''
   username = input('Username: ')
   while master != passphrase:
      master = input('Enter your passphrase: ')
      if master == passphrase:
         print('\n Great! What would you like to do now? ')
         break
      else:
         print("That's not your passphrase, try again")
         
def menu():
# This function provides a menu of options/features to choose from.
# Depending on the option, the program executes that feature.
   global option, username
   print("""
Menu:
1) Add a password for a service
2) Retrieve a password, copy it to the clipboard and launch website
3) Generate a password for a service 
4) Exit the Program """)  
   option = input('\n Tell me what you want to do by entering 1, 2, 3 or 4: ')
   return option, username

def tough_decryptr2(phrase,keya,keyb):  #Encrypts OR Decrypts depending on parameter order
   global txt
   txt=''
   for i in range(len(phrase)):
      key_ind = keya.index(phrase[i]) 
      j = keyb[(key_ind)]
      txt = txt + j
      print(j,end='')
   print(' ')
   return txt

#This was the code from the book, but I tailored it
#PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
#             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
#             'luggage': '12345'}

#PASSWORDS = {'jflowers': {
#  working      'passphrase': 'Go',
#               'url': 'http://www.gmail.com',
#               'email': 'myemailpassword'}
# Adding a new password for a website

PASSWORDS =   {'jflowers': {
              'passphrase': 'Go',
              'email': {
                 'url': 'http://www.gmail.com',
                 'email': 'xloxpswbpeejadh' }, #myemailpassword
              'expedia': {
                  'url': 'http://www.expedia.com',
                  'expedia': 'xlokbohspbpeejadh'} #myexpediapassword
             }
# This can be a future enhancement to add multiple user names
#             {'frantz': {
#               'passphrase': 'GoFrantz'
#               'email': {
#                  'url': 'http://www.hotmail.com',
#                  'email': 'ndpzfmrafxpswbpeejadh'} #frantzhotmailpassword
#               'ebay': {
#                  'url': 'http://www.ebay.com',
#                  'ebay':'ndpzfmoyplbpeejadh'} #frantzebaypassword
             }
           
#print('jf: ',PASSWORDS['jflowers']['email']['email'])               
                
import sys, pyperclip, webbrowser,json, random
# keys used for encrypting and decrypting
key1 = 'abcdefghijklmnopqrstuvwxyz '
key2 = 'pythonqrsuvwxzabcdefgijklm '
intro()  #Get username and master passphrase
option = '5'
while option != '4':
   menu() #Menu of options/features
   if len(sys.argv) < 2: #Checks to ensure argument was passed from command line
       print('Usage: py pw.py [account] - copy account password')
       print('sys argv: ',sys.argv, len(sys.argv))
       sys.exit()
   if option == '4':    
      print('Thank you. Talk to you later. Goodbye...')
#  TODO add username

   elif option == '2': # Retrieve a password, copy it to the clipboard and launch website
      try:
         account = PASSWORDS[username][sys.argv[1]][sys.argv[1]] #Ensures the service exists
         # first command line arg is the account name
#if account in PASSWORDS:
         tough_decryptr2(account,list(key2),list(key1)) #Decrypt password before saving to clipboard
         pyperclip.copy(txt)
         print('Your password ' + txt + ' has been decrypted and copied to clipboard. \n I will now launch the website for you.')
         xx = input('Press <enter> ')
         print('open website')
         print('ws: ',PASSWORDS[username][sys.argv[1]]['url'])
         webbrowser.open(PASSWORDS[username][sys.argv[1]]['url'])
      except KeyError:    
         print('There is no password for that account. Try using option 1 to add it first.')

   elif option == '3': # Generate a password for a service
        print('Generate password: ')
        word_file = "/usr/share/dict/words"
        WORDS = open(word_file).read().splitlines()
        pwd3 = ''
        for i in range(4):
           one_word = random.choice(WORDS)
           if i == 0:
              one_word = one_word.capitalize()
           pwd3 = pwd3 + one_word
        pwd3 = pwd3.lower()  
        print("Your generated password is ",pwd3)

   elif option == '1': # Add a new password for a website
        print('Add a password for a website: ')
        url = input('Enter the new website url i.e. www.amazon.com: ')
        url = 'http://' + url
        service = input('Enter a name for this website i.e. amazon: ')
        pwd = input('Enter your password for this website: ')
        tough_decryptr2(pwd,list(key1),list(key2))  #Encrypt the password before saving
        PASSWORDS[username][service] = {}
        PASSWORDS[username][service] = {'url':url,service:txt}
#    print('PASSWORDS: ',PASSWORDS)
        print('Your new password for *',service,'* has been encrypted and added')
        launch=input('Do you want to use the password and launch the website now? Y/N ')
        if launch == 'Y':
           print('PWDnew is ',PASSWORDS[username][service][service])
           try:
              account = PASSWORDS[username][service][service]   # first command line arg is the account name
              tough_decryptr2(account,list(key2),list(key1)) # Decrypt password before saving to clipboard
              pyperclip.copy(txt) #Copies to clipboard
              print('Your password ' + txt + ' has been decrypted and copied to clipboard. \n I will now launch the website for you.')
              xx = input('Press <enter> ')
           except KeyError:    
              print('There is no password for that account')
           print('open website')
           print('ws: ',PASSWORDS[username][service]['url'])
           webbrowser.open(PASSWORDS[username][service]['url'])
    
   else:
       print('Error - I did not recognize your entry ')
