# basic caesar cipher
# 11/05/2022

def encrypt(key):
    message = input('Enter message:\n')
    array = list(message)
    for i in range(len(array)):
        array[i] = chr(ord(array[i]) + key)
    print("".join(array))


def decrypt(key):
    array = list(message)
    for i in range(len(array)):
        array[i] = chr(ord(array[i]) - key)
    print("".join(array))

encrypt(3)

message = input('Enter message:\n')
for i in range(26):
    decrypt(i)
