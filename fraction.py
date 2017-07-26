'''
Python 3 class implementation of a way to display fractions in their exact
form
'''
class Fraction:
    '''
    Class definition of Fraction
    '''
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

def main():
    '''
    Show an example of adding two fractions (here, 4/5 and 2/3)
    '''
    MyFrac = Fraction(4, 5)
    MyFrac.show()
    print(MyFrac)
    OtherFrac = Fraction(2, 3)
    print(MyFrac + OtherFrac)
main()
