print("Is it raining?")

while True:
    choice = input("(Yes/No): ").lower()

    if choice == "yes":
        break
    if choice == 'no':
        break
    else:
        print("Please enter Yes or No.")

if choice == 'yes':
    while True:        
        umbrella = input("Do you have an umbrella?: ").lower()
        if umbrella == "yes":
            break
        elif umbrella == 'no':
            break
        else:
            print("Please enter Yes or No.")
    if umbrella == "yes":
        print("Go outside.")
    else:
        print("Wait a while.")

else:
    print("Go outside.")