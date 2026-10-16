# перевантаження стандартних операцій
# функції з префіксом 'i' змінюють оригінальний об'єкт. Інші повертають новий об'єкт.

class Fraction:
    numerator: int
    denominator: int
    
    def __init__(self, _numerator, _denominator):
        self.numerator = _numerator
        self.denominator = _denominator
        
    # Fraction(1,2) + Fraction(2,3)
    def __add__(self, other):
        res = Fraction(0, 0)
        res.denominator = self.denominator * other.denominator
        res.numerator = (self.numerator*other.denominator) + (other.numerator * self.denominator)
        return res
    # Fraction(1,2) += Fraction(2,3)
    def __iadd__(self, other):
        # res = Fraction(0, 0)
        denominator = self.denominator * other.denominator
        numerator = (self.numerator*other.denominator) + (other.numerator * self.denominator)
        self.numerator = numerator
        self.denominator = denominator
        return self
    # Fraction(1,2) - Fraction(2,3)
    def __sub__(self, other):
        res = Fraction(0, 0)
        res.denominator = self.denominator * other.denominator
        res.numerator = (self.numerator*other.denominator) - (other.numerator * self.denominator)
        return res
    
    def __isub__(self, other):
        denominator = self.denominator * other.denominator
        numerator = (self.numerator*other.denominator) - (other.numerator * self.denominator)
        self.numerator = numerator
        self.denominator = denominator
        return self
    
    def __mul__(self, other):
        res = Fraction(0,0)
        res.denominator = self.denominator*other.denominator
        res.numerator = self.numerator*other.numerator
        return res
    
    def __imul__(self, other):
        denominator = self.denominator*other.denominator
        numerator = self.numerator*other.numerator
        self.numerator = numerator
        self.denominator = denominator
        return self
    
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    
print(Fraction(1,2) == Fraction(2,3))
