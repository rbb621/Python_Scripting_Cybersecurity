name = input("Enter a name: ")
print("Welcome,", name)


while True:
    password = input('Enter a password: ')
    if password == 'Animal Crossing':
        print('Logging in...')
        break
    else:
        print("Wrong password. Try again")