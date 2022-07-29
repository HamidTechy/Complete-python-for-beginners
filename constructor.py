class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def father(self):
        print("father")

    def mother(self):
        print("mother")


human = Human(10, 20)
human.y = 30
print(human.x)
print(human.y)
