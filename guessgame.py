import random
random = random.randint(1, 9)
init_num = 0
guess_limit = 3
while init_num < guess_limit:
    guess_count = int(input("Guess your number"))
    if init_num == guess_limit:
        print("sorry you lost the chance")
    elif guess_count < random:
        print("choose greater Number")
    elif guess_count > random:
        print("choose smaller Number")
    elif guess_count == random:
        print("your won the Game")
        break
    init_num += 1