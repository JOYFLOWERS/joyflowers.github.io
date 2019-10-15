#! /usr/bin/env python3
# The above line is used for a Mac.
# If running in Windows, replace /usr/bin/env python3 with python3
# pw.py - An insecure password locker program.

def menu:
   print("""Hi, I am Phyllis, your Password Locker System (PLS).
I will help you to store passwords for websites and other software,
retrieve your password when you need it and copy it to the clipboard so you
don't have to remember it, and
encrypt/decrypt it to keep your passwords secure.
You can also have me generate a password for you.
When you enter a master passphrase, we can start with whatever you like:""")
   passphrase = 'GoPhyllisGoPhyllis'
   master=''
   while master != passphrase:
      master = input('Enter your passphrase: ')
      if master == passphrase:
         print('Great! What would you like to do now? ')
         break
      else:
         print("That's not your passphrase, try again")

   print("""Menu:
1) Add a password for a service
2) Retrieve a password and copy it to the clipboard
3) Generate a password for a service """)
   option = input('Tell me what you want to do by entering 1, 2, or 3')
   

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
print("I'm here")
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    print('sys argv: ',sys.argv, len(sys.argv))
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name
print('account: ', account)
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
