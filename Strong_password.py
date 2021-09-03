import re

password = input('Enter a strong password :  ')
flag = 0

while True:
    if len(password)<8:
        flag = -1
        print('Enter password of length more than 8')

    elif not re.search("[a-z]",password):
        flag = -1
        print('Enter at least one lower alphabet')

    elif not re.search("[A-Z]",password):
        flag = -1
        print('Enter at least one upper alphabet')

    elif not re.search("[0-9]",password):
        flag = -1
        print('Enter at least one digit')

    elif not re.search("[_@$]",password):
        flag = -1
        print('Enter at least one special symbol out of _ $ @')

    else:
        flag = 0
        print("valid")


    if flag==-1:
        print("Not valid password")
        password = input('Enter a strong password :  ')
    else:
        print('Password is strong :  ',password)
        break

