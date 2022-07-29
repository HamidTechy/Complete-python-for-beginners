car = ""
started = False
while True:
    car = input(">").lower()
    if car == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif car == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped")
    elif car == "help":
        print('''
        star = start car
        stop = stop car
        quite = quite car
        ''')
    elif car == "quite":
        print("Game quite")
        break
    else:
        print("I don't understand that")
