class Charector:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def attack(self, x):
        x.health = x.health - 1
def rungame():
    x = Charector("Tang", 100)
    z = Charector("Di", 100)
    x.attack(z)
    print(x.name + " is attacking " + z.name)
    print(z.name + " is at " + str(z.health) + " health!")
rungame()