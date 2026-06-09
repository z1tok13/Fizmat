from Fractions import Fractions

numerator = int(input("Введите значение числителя: "))
denominator = int(input("Введите значение знаменателя: "))
fraction = Fractions(numerator, denominator)

numerator = int(input("Введите значение числителя: "))
denominator = int(input("Введите значение знаменателя: "))
fraction2 = Fractions(numerator, denominator)
print((fraction.add(fraction2)).display())
print((fraction.sub(fraction2)).display())
print((fraction.mult(fraction2)).display())
print((fraction.div(fraction2)).display())