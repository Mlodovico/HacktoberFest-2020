"""
Cesar Cipher System
@author Murilo Lodovico
"""

import sys
import string

print('----------Cesar Cipher System----------')

print('type 1 (one) if you wanna decrypt a message,'
      'type 2 (two) if you wanna encrypt a message,\n')

type = int(input('Type here the service:'))

if type == 1:
  encrypted_message = input("Enter encrypt message:").strip()
  print()
  key = int(input("Enter key:"))
  alphabet = string.ascii_lowercase

  decrypted_message = ""

  for letter in encrypted_message:

    if letter in alphabet:
      position = alphabet.find(letter)
      new_position = (position - key) % 26
      new_char = alphabet[new_position]
      decrypted_message += new_char
    else:
      decrypted_message += letter

elif type == 2:
  doc = open(sys.argv[1], 'r').read().lower()
  rotation = int(sys.argv[2])
  alphabet = string.ascii_lowercase
  result = ''
  
  for letter in doc:
    if letter in alphabet:
      position = alphabet.find(letter)
      position = (position + rotation) % 26
      result += result + alphabet[position]
    print (result)

