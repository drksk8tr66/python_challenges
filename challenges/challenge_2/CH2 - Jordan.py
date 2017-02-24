class Calculator:
    def __init__(self, calc_type):
        self.type = calc_type
        self.f = 0
        self.m = 0
        self.a = 0

    def force_value(self, f: int=0):
        f = input('What is the force? ')
        while str(f) == 0 or not f.isnumeric():
            f = input('Please enter a number for the force: ')
        self.f = int(f)

    def mass_value(self, m: int=0):
        m = input('What is the mass? ')
        while str(m) == 0 or not m.isnumeric():
            m = input('Please enter a number for the mass: ')
        self.m = int(m)

    def acceleration_value(self, a: int=0):
        a = input('What is the acceleration? ')
        while str(a) == '0' or not a.isnumeric():
            a = input('Please enter a number for the acceleration: ')
        self.a = int(a)

    def calc_force(self):
        f = self.m * self.a
        self.f = f

    def calc_mass(self):
        m = self.f/self.a
        self.m = m

    def calc_acceleration(self):
        a = self.f/self.m
        self.a = a

    def calc_answer(self):
        print('Force = {} \nMass = {} \nAcceleration = {}'.format(self.f, self.m, self.a))
        calc.type = None

if __name__ == '__main__':
    calc_type = None
    calc_option = ['f', 'm', 'a', 'e']
    calc = Calculator(calc_type)
    while calc.type not in calc_option:
        print('Do you want to calculate Force(f), Mass(m), Acceleration(a) or Exit(e) the calculator? ')
        calc.type = input("Please enter 'f' for Force, 'm' for Mass, or 'a' for Acceleration or 'e' to Exit: ").lower()
        if calc.type == 'f':
            calc.mass_value()
            calc.acceleration_value()
            calc.calc_force()
            calc.calc_answer()
        elif calc.type == 'm':
            calc.force_value()
            calc.acceleration_value()
            calc.calc_mass()
            calc.calc_answer()
        elif calc.type == 'a':
            calc.force_value()
            calc.mass_value()
            calc.calc_acceleration()
            calc.calc_answer()
        elif calc.type == 'e':
            exit()
