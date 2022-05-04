class Person():
    def __init__(self):
        self.name = ""
        self.money = 0


def main():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    nancy = Person()
    nancy.name = "Nancy"

    print(bob.name, "has", bob.money, "dollars.")
    print(nancy.name, "has", nancy.money, "dollars.")


main()