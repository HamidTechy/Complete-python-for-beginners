class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


latif = Person("Hamid Latif")
latif.talk()

naseem = Person("Rana Khuram")
naseem.talk()
