email = input('Enter your email id:   ').strip()

position = email.index('@')
username = email[:position]

domain = email[position+1:]

print('Name in the email is {} and domain used is {}'.format(username,domain))