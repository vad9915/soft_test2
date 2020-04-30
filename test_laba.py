class Formulas():
    def __init__(self, x):
        self.x = x

    def calculation_1(self):
        try:
            if self.x <= 1.186  or self.x >= 186.501:
                return self.x**4 * 1.871+ self.x**3 * 2.317-self.x**2 * 4.367 + self.x * 3.851
        except TypeError:
            return "Error"

    def calculation_2(self):
        try:
            if self.x <= 1.186 or self.x >= 186.501:
                return self.x ** 3 * 2.498 - self.x ** 2 * 2.055 + self.x * 5.72
        except TypeError:
            return "Error"

    def calculation_3(self):
        try:
            if self.x <= 1.186 or self.x >= 186.501:
                return self.x ** 2 * 1.948 + self.x * 3.572
        except TypeError:
            return "Error"

    def calculation_4(self):
        try:
            if self.x <= 1.186 or self.x >= 186.501:
                return self.x * 4.314
        except TypeError:
            return "Error"

if __name__ == '__main__':
    F = Formulas(300)
    print(F.calculation_1(), F.calculation_2(), F.calculation_3(), F.calculation_4())