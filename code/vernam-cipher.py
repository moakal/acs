# vernam cipher
# 22/05/2022

# broken due to python binary handling

import random
import string

def divideList(l):
    for i in range(0, len(l), 8): 
        yield l[i:i + 8]

def encrypt():
    message = input('Enter message:\n')
    messageBinary = list(''.join(format(ord(i), '08b') for i in message))
    key = ''.join(random.choices(string.ascii_letters, k=len(message)))
    keyBinary = list(''.join(format(ord(i), '08b') for i in key))
    digestBinary = []
    for j in range(len(messageBinary)):
      if int(messageBinary[j]) ^ int(keyBinary[j]):
        digestBinary.append('1')
      else:
        digestBinary.append('0')
    splitDigest = list(divideList(digestBinary))
    digest = []
    for k in range(len(splitDigest)):
      digest.append(chr(int(''.join(splitDigest[k]))))
    digest = ''.join(digest)
    print('Key: '+ key + '\nDigest: ' + digest)

def decrypt():
    digest = input('Enter digest:\n')
    digestBinary = list(''.join(format(ord(i), '08b') for i in digest))
    key = input('Enter key\n')
    keyBinary = list(''.join(format(ord(i), '08b') for i in key))
    messageBinary = []
    for j in range(len(keyBinary)):
      if int(digestBinary[j]) ^ int(keyBinary[j]):
        messageBinary.append('1')
      else:
        messageBinary.append('0')
    splitMessage = list(divideList(messageBinary))
    message = []
    for k in range(len(splitMessage)):
      message.append(chr(int(''.join(splitMessage[k]))))
    message = ''.join(message)
    return 'Keypad:', key
    return 'Message:', message

encrypt()
print('--------')
print(decrypt())
