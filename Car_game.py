command = ""
speed_initial = 0
started = False

print('''Type "help" to seek the commands''')


while command != "quit":
    command = input("Enter your command: ")
    if command == "help":
        print("Start - Start the car ")
        print("Stop - Stop the car ")
        print("Quit - Quit the game")
        print("Accelerate - To accelerate the car")
        print("Decelerate - To decelerate the car")

    elif command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Starting the car")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Stopping the car")

    elif command == "accelerate":
        if started:
            print("Accelerating the car by 10 km/hr")
            speed_initial += 10
            print(f'Your speed is now {speed_initial}')
        if not started:
            print("First start the car")
    elif command == "decelerate":
        print("Decelerating the car by 10 km/hr")
        speed_initial -= 10
        print(f'Your speed is now {speed_initial}')
    elif command == "quit":
        print("Quitting the program")
        break
    else:
        print("I dont get you, Try another command")
