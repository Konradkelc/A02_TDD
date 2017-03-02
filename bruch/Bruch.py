"""
@author: kkelc

"""


class Bruch(object):

    """ Bruch

    :param int zaehler: numerator
    :param int nenner: denominator
    """

    def __init__(self, zaehler=0, nenner=1):

        """constructor

        :param zaehler: Bruch or int
        :param nenner: int not zero
        :raise TypeError:
        """

        self.zaehler = zaehler
        self.nenner = nenner

        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
        elif type(zaehler) is not int:
            raise TypeError()
        elif type(nenner) is not int:
            raise TypeError()
        if nenner == 0:
            raise ZeroDivisionError


    def __iter__(self):

        """makes the class iterable
        """
        return (self.zaehler, self.nenner).__iter__()


    def __float__(self):

        """float

        :return: float
        """

        return self.zaehler / self.nenner

    def __int__(self):

        """int

        :return: int
        """

        return int(self.__float__())

    def __complex__(self):

        """complex

        :return: complex
        """

        return complex(self.__float__())

    def __invert__(self):

        """invert

        :return: Bruch
        """

        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, n):

        """power

        :param int p: power
        :raise TypeError:
        :return: Bruch
        """

        if type(n) is int:
            return Bruch(self.zaehler**n, self.nenner**n)
        else:
            raise TypeError()

    def __makeBruch(other):

        """makeBruch

        :param other: Bruch or int
        :raise TypeError:
        :return: Bruch
        """

        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError()

    def __abs__(self):

        """absolute

        :return: a positive Bruch
        """

        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):

        """negativ

        :return: a negative Bruch
        """

        return Bruch(-self.zaehler, self.nenner)

    def __eq__(self, other):

        """equal

        :param other: other Bruch
        :return: boolean
        """

        other = Bruch.__makeBruch(other)
        return self.zaehler*other.nenner == other.zaehler*self.nenner

    def __ge__(self, other):

        """greater or equal

        :param other: other Bruch
        :return: boolean
        """

        other = Bruch.__makeBruch(other)
        return self.zaehler*other.nenner >= other.zaehler*self.nenner

    def __le__(self, other):

        """lower or equal

        :param other: other Bruch
        :return: boolean
        """

        other = Bruch.__makeBruch(other)
        return self.zaehler*other.nenner <= other.zaehler*self.nenner

    def __lt__(self, other):

        """lower

        :param other: other Bruch
        :return: boolean
        """

        other = Bruch.__makeBruch(other)
        return self.zaehler*other.nenner < other.zaehler*self.nenner

    def __gt__(self, other):

        """greater

        :param other: other Bruch
        :return: boolean
        """

        other = Bruch.__makeBruch(other)
        return self.zaehler*other.nenner > other.zaehler*self.nenner

    def __str__(self):

        """string

        :return: string
        """

        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1
        str1 = "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

        if self.nenner == 1:
            str1 = "("+str(self.zaehler)+")"

        return str1

    def __add__(self, zaehler):

        """add

        :param zaehler: int or Bruch
        :raise TypeError:
        :return: Bruch
        """

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError()
        nneu = self.nenner * n2
        zneu = z2*self.nenner + n2*self.zaehler
        return Bruch(zneu, nneu)

    def __radd__(self, zaehler):

        """right add

        :param zaehler: int or Bruch
        :raise TypeError:
        :return: Bruch
        """

        return self.__add__(zaehler)

    def __iadd__(self, other):

        """intern add

        :param other: other Bruch
        :return: self
        """

        other = Bruch.__makeBruch(other)
        self = self + other
        return self

    def __sub__(self, zaehler):

        """sub

        :param zaehler: int or Bruch
        :raise TypeError:
        :return: Bruch
        """

        return self.__add__(zaehler*-1)

    def __isub__(self, other):

        """intern sub

         :param other: other Bruch
         :raise TypeError:
         :return: self
         """

        other = Bruch.__makeBruch(other)
        self = self - other
        return self


    def __rsub__(self, left):

        """right sub

         :param zaehler: int or Bruch
         :raise TypeError:
         :return: Bruch
         """

        if type(left) is int:
            z2 = left
            nneu = self.nenner
            rneu = z2 * self.nenner - self.zaehler
            return Bruch(rneu, nneu)
        else:
            raise TypeError()

    def __mul__(self, zaehler):

        """multiply

         :param zaehler: int or Bruch
         :raise TypeError:
         :return: Bruch
         """

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError()
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __imul__(self, other):

        """intern multiply

         :param other: other Bruch
         :return: self
         """

        other = Bruch.__makeBruch(other)
        self = self * other
        return self

    def __rmul__(self, zaehler):

        """right multiply

         :param zaehler: int or Bruch
         :raise TypeError:
         :return: Bruch
         """

        return self.__mul__(zaehler)

    def __truediv__(self, zaehler):

        """division

         :param zaehler: Bruch or int
         :raise TypeError:
         :return: Bruch
         """

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError()
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __rtruediv__(self, left):

        """right division

         :param zaehler: int or Bruch
         :raise TypeError:
         :return: Bruch
         """

        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError()

    def __itruediv__(self, other):

        """intern division

         :param other: other bruch
         :return: self
         """

        other = Bruch.__makeBruch(other)
        self = self / other
        return self















