class Calculator:
    def __init__(self, calc_type):
        self.type = calc_type
        self.f = 0
        self.m = 0
        self.a = 0

    def force_value(self, f: int=0):
        while f == 0 or not f.isnumeric():
            f = input('What is the force? ')
        self.f = int(f)

    def mass_value(self, m: int=0):
        while m == 0 or not m.isnumeric():
            m = input('What is the mass? ')
        self.m = int(m)

    def acceleration_value(self, a: int=0):
        while a == 0 or not a.isnumeric():
            a = input('What is the acceleration? ')
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

if __name__ == '__main__':
    calc_type = 'z'
    calc_option = ['f', 'm', 'a']
    while calc_type not in calc_option:
        calc_type = input('Do you want to calculate Force(f), Mass(m), or Acceleration(a)? ').lower()
        calc = Calculator(calc_type)
        if calc.type == 'f':
            calc.mass_value()
            calc.acceleration_value()
            calc.calc_force()
        elif calc.type == 'm':
            calc.force_value()
            calc.acceleration_value()
            calc.calc_mass()
        elif calc.type == 'a':
            calc.force_value()
            calc.mass_value()
            calc.calc_acceleration()
    calc.calc_answer()
