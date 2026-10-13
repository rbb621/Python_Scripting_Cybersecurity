name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')

# You could have entered not name != " instead of not name, and numOfGuests != 0 
# instead of numOfGuests, 
# but using the truthy and falsey values can make your code easier to read.


'''
Version 2.0 with number of avaiable seats
'''
# name = ''
# availableSeats = 3

# while not name:
#     print("Name of the person: ")
#     name = input()


# while True:
#     print("How many guests are joining?: ")
#     numOfGuests = int(input())
#     if numOfGuests > availableSeats:
#         print('Sorry, there is only room for', availableSeats, 'meaning your group has', numOfGuests - availableSeats)
#     else:
#         print('Be sure to have enough room for all your guests.')
#         break
# print('done')


