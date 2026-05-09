class charactor:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, x):
        x.health = x.health-1

def rungame():
    wizard = charactor("Tang", 100)
    z = charactor("Di", 50)
    wizard.attack(z);
    print(f"{wizard.name} is attacking {z.name}");
    print(f"{z.name} health is now: {z.health}")

rungame();

# how to define a class
# how to define a init function of the class
# how to define attribute/property in the class
# how to define function in the class
# how to create a instance of the class with attributes
# how to use functions with the class instance