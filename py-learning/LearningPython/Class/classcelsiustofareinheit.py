class conversion:
    def __init__(self, ctof, ftoc):
        self.ctof = ctof
        self.ftoc = ftoc

    def ctof(c):
        c = (c * 9/5) + 32
        print(c)

    def ftoc(f):
        f = (f - 32) * 5 / 9
        print(f)
        
conversion.ctof(5)
conversion.ftoc(41)

