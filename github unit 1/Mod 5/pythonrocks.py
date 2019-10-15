#Joy Flowers
#09/30/19

#xqtoysqgzymooeymondyakqqdxhsycnlym hhyaooysqgy nyihcaaydqn uxd from Franz

#This program steps through several encryption and decryption methods
#Answers retrieved from this code are:
#1  'PYTHONROCKS' with a shift of 14
#2  'xliuymgofvsarjsbnyqtwszivxlipedchsk' with a shift of 4
#3  'minnisotaunitedfootballclub' with a shift of 9
#4  'sbqfzs fqmcpqfzxofqmcpqf mlxcdqumeqsbqgmwwmd fqmcpqyxcdf'
#5  'the sun was shining on the sea shining with all of his might'
#6a 'lqygndqyqdxozaycaysqgymqghlyxcjoydxokylqygndqysqg'
#6b 'do unto others as you would have them do unto you'
#7a 'sjpeywszhpzhzajseoo' with password 'python'
#7b 'iwasblindandnowisee' with password 'python'
#8a 'qjpfavqywpywyzjqfoo' with password 'password'
#8b 'iwasblindandnowisee' with password 'password'

#Set initial keys
key1 = 'abcdefghijklmnopqrstuvwxyz '
key2 = 'mwgp bdzxrylacsokjfhtnueivq'
txt=''
def tough_decryptr2(phrase,keya,keyb):
   global txt
   txt=''
   for i in range(len(phrase)):
      key_ind = keya.index(phrase[i]) 
      j = keyb[(key_ind)]
      txt = txt + j
      print(j,end='')
   print(' ')
   return txt

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
         'O','P','Q','R','S','T','U','V','W','X','Y','Z']

alpha_lc = ['a','b','c','d','e','f','g','h','i','j','k','l',\
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decryptr(phrase,alpha_in):
   for shift in range(len(alpha)):
# Encr = (pᵢ + k) % 26
# Decr = (pᵢ - k) % 26
      for i in range(len(phrase)):
         alpha_ind = alpha_in.index(phrase[i]) 
         j = alpha_in[(alpha_ind+shift)%26]
         print(j,end='')
      print(' Shift',shift)
   
#phrase = input('Enter your code uppercase: ')

print('Part 1: ')      
#Part 1: decrypt the following string:
phrase = list('BKFTAZDAOWE')
#Answer is when shifting 14 where A = O so that the message is 'PYTHONROCKS'
#decryptr(phrase,alpha)

print('Part 2: ')   
#Part 2: encrypt the following string:
plaintext = list(('thequickbrownfoxjumpsoverthelazydog'))
#Answer gives many decryptd options for example, a shift of 4 is 'xliuymgofvsarjsbnyqtwszivxlipedchsk'
#decryptr(plaintext,alpha_lc)

print('Part 3: ')   
#Part 3: decrypt the following string:
ciphertext = list(('dzeevjfkrlezkvuwffksrcctcls'))
#decryptr(ciphertext,alpha_lc)
#Answer for shift 9 is 'minnisotaunitedfootballclub'
#print(phrase)

print('Part 4: ')   
#Part 4: encrypt the following string:
plaintext = list('of shoes and ships and sealing wax of cabbages and kings')
#tough_decryptr2(plaintext,list(key1),list(key2))
ciphertext = txt
print('ciphertext: ',ciphertext)
#Answer is 'sbqfzs fqmcpqfzxofqmcpqf mlxcdqumeqsbqgmwwmd fqmcpqyxcdf'

print('Part 5: ')   
#Part 5: decrypt the following string:
ciphertext = list('hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh')
#tough_decryptr2(ciphertext,list(key2),list(key1))
plaintext = txt
print('plaintext: ',plaintext)
#Answer is 'the sun was shining on the sea shining with all of his might'

print('Part 6a: ')   
#Part 6a: Enter a key and use it to encrypt a string This was done with dictionary
phrase = 'do unto others as you would have them do unto you'
#key2 = input('Enter a scrambled key using all 26 characters once and using the space key: ')
key2 = 'cfilorux behknqtwzadgjmpsvy'
#tough_decryptr2(phrase,list(key1),list(key2))
#Answer is 'lqygndqyqdxozaycaysqgymqghlyxcjoydxokylqygndqysqg'

print('Part 6b: ')   
#Part 6b: Enter a key and use it to decrypt a string
phrase = 'xqtoysqgzymooeymondyakqqdxhsycnlym hhyaooysqgy nyihcaaydqn uxd'
#phrase = 'lqygndqyqdxozaycaysqgymqghlyxcjoydxokylqygndqysqg'
#tough_decryptr2(phrase,list(key2),list(key1))
#Answer is 'do unto others as you would have them do unto you'
#Decrypted answer from Franz is 'hope your week went smoothly and will see you in class tonight'

print('Part 7a: ')   
#Part 7a: encrypt using a key made from a password, the last half of alpha and 1st half of alpha
phrase = 'frantzebaypassword'
key2 = 'pythonqrsuvwxzabcdefgijklm'
tough_decryptr2(phrase,list(key1),list(key2))
#Answer is 'csjpeywszhpzhzajseoo'  

print('Part 7b: ')   
#Part 7b: decrypt using a key made from a password, the last halp of alpha and 1st half of alpha
phrase = 'sjpeywszhpzhzajseoo'
key2 = 'pythonqrsuvwxzabcdefgijklm'
tough_decryptr2(phrase,list(key2),list(key1))
#Answer is 'iwasblindandnowisee'

print('Part 8a: ')   
#Part 8a: encrypt using an entered key and phrase and implement same as 7a
def prep_key(phrase):
   user_pwd = list(input('Enter a lowercase password up to 7 characters, no spaces or punctuation: '))
   pwd = list(dict.fromkeys(user_pwd))
   key_part1 = list('abcdefghijklm')
   key_part2 = list('nopqrstuvwxyz')
   print('pwd kp1 kp2 ',pwd,key_part1,key_part2)
   for i in range(len(pwd)):
      j=0
      while j < len(key_part1):
         if pwd[i] == key_part1[j]:
            del key_part1[j]
            j=j-1
         j=j+1   
   for i in range(len(pwd)):
      j=0
      while j < len(key_part2):
         if pwd[i] == key_part2[j]:
            del key_part2[j]
            j=j-1
         j=j+1  
   ky2 = pwd + key_part2 + key_part1
   key2 = ''.join(ky2)
   print('key2', key2)
   return key2

phrase = input('Enter the phrase to be encrypted: ')
key2 = prep_key(phrase)
tough_decryptr2(phrase,list(key1),list(key2))
#Answer is 'sjpeywszhpzhzajseoo' using pwd python
#Answer is 'qjpfavqywpywyzjqfoo' using pwd password


print('Part 8b: ')   
#Part 8b: decrypt using an entered key and phrase and implement same as 7b

phrase = input('Enter the phrase to be decrypted: ')
key2 = prep_key(phrase)
tough_decryptr2(phrase,list(key2),list(key1))
#Answer is 'iwasblindandnowisee' using pwd python
#Answer is 'iwasblindandnowisee' using pwd password

##End of Program ###########################################################


##########The following was the first implementation
##########and has been replaced by the code above

#The first section was implemented for part 1, but now
#the section below is more flexible so is used instead.

#ncode and dcode were used for the initial implementation and
#then abandon for a better method
##ncode = {'a':'m','b':'w','c':'g','d':'p','e':' ','f':'b',\
##         'g':'d','h':'z','i':'x','j':'r','k':'y','l':'l',\
##         'm':'a','n':'c','o':'s','p':'o','q':'k','r':'j',\
##         's':'f','t':'h','u':'t','v':'n','w':'u','x':'e',\
##         'y':'i','z':'v',' ':'q'}
##dcode = {'m':'a','w':'b','g':'c','p':'d',' ':'e','b':'f',\
##         'd':'g','z':'h','x':'i','r':'j','y':'k','l':'l',\
##         'a':'m','c':'n','s':'o','o':'p','k':'q','j':'r',\
##         'f':'s','h':'t','t':'u','n':'v','u':'w','e':'x',\
##         'i':'y','v':'z','q':' '}

#this function was used for inital implementation and then abandon
##def tough_decryptr(phrase,dcd):
##   for v in range(len(phrase)):
##      ans = dcd.get(phrase[v])
##      print(ans,end='')
##   print(' ')

#This was first used but then chose a better method
##print('Part 4a: ')   
###Part 4a: encrypt the following string:
##phrase = list('of shoes and ships and sealing wax of cabbages and kings')
##tough_decryptr(phrase,ncode)
###Answer is 'sbqfzs fqmcpqfzxofqmcpqf mlxcdqumeqsbqgmwwmd fqmcpqyxcdf'

#This was first used but then chose a better method
##print('Part 5a: ')   
###Part 5a: decrypt the following string: This was done with dictionary
##phrase = list('hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh')
##tough_decryptr(phrase,dcode)
###Answer is 'the sun was shining on the sea shining with all of his might'
