import random

password_length = int(input('Enter the length of the password you want:  '))
letters= "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

password= ''.join(random.sample(letters,password_length))
print('Your Generated Password is:  ',password)