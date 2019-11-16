
#inheritance
#superclasses and subclasses - usually dont go deeper than 3 levels..one superclass and two subclasses

class Animal:
    def __init__(self, legs_init_value):
        self._legs = legs_init_value
    def __str__(self):
        return 'Animal has {} legs'.format(self._legs)
    def get_legs(self):
        return self._legs

    def set_legs(self, new_value):
        raise ValueError('Must grow a leg')

    legs = property(get_legs, set_legs)

    def grow_a_limb(self):
        self._legs = self._legs +1


class Deer(Animal):
    def __init__(self):
        super().__init__(4) #super calls the superclass - the one in parentheses --- Animal
    def __str__(self):
        return 'Deer has {} legs'.format(self.legs)





def main():
    # print('Hello deer')
    # a = Animal(4)
    # print(a)
    # a.grow_a_limb()
    # print(a)
    d = Deer()
    print(d)
    d.grow_a_limb()
    print(d)


if __name__ == '__main__':
    main()



