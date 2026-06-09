class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def set_numerator(self, numerator):
        self.numerator = numerator
    def set_denominator(self, denominator):
        self.denominator = denominator

    def add(self, new_fraction):
        new_numerator = self.numerator * new_fraction.denominator + new_fraction.numerator * self.denominator
        new_denominator = self.denominator * new_fraction.denominator
        return Fractions(new_numerator, new_denominator)

    def sub(self, new_fraction):
        new_numerator = self.numerator * new_fraction.denominator - new_fraction.numerator * self.denominator
        new_denominator = self.denominator * new_fraction.denominator
        return Fractions(new_numerator, new_denominator)

    def mult(self, new_fraction):
        new_numerator = self.numerator * new_fraction.numerator
        new_denominator = self.denominator * new_fraction.denominator
        return Fractions(new_numerator, new_denominator)

    def div(self, new_fraction):
        new_numerator = self.numerator * new_fraction.denominator
        new_denominator = self.denominator * new_fraction.numerator
        return Fractions(new_numerator, new_denominator)

    def display(self):
        print(f'{self.numerator}/{self.denominator}')