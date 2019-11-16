'''
Farm Family Project

Michael Streyle
10/7/18

'''
#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Adults():
    '''Adults class'''
    def __init__(self, name: str, age: int):
        '''__init__'''
        self._name = name
        self._age = age
        
    @property
    def name(self):
        ''' Name property getter'''
        return self._name
    @name.setter
    def name(self, value):
        '''name property setter'''
        self._name = value
    
    @property
    def age(self):
        ''' Age property getter'''
        return self._age
    @age.setter
    def age(self, value):
        '''age property setter'''
        self._age = value


    def __eq__(self, other: object):
        '''Compare 2 Adults'''
        if str(self) == str(other):
            return self, '=', other

    def __str__(self):
        '''__str method'''
        return str(self._name) + 'is ' + str(self._age) + 'years old'


class Pets():
    '''Pets class'''
    def __init__(self, name_init: str, pet_age: int):
        '''Constructor'''
        self._pet_name = name_init
        self._pet_age = pet_age

    @property 
    def name(self):
        ''' name property getter'''
        return self._pet_name
    @name.setter
    def name(self, value):
        '''name property setter'''
        self._pet_name = value

    @property 
    def pet_age(self):
        ''' Age of pet property getter'''
        return self._pet_age
    @pet_age.setter
    def pet_age(self, value):
        '''age of pet property setter'''
        self._pet_age = value




    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address

    def __str__(self):
        '''__str'''
        return str(self._pet_name) + 'is a pet and is' + str(self._pet_age) + 'years old.'


class Children(Adults):
    '''Children class'''
    
    def __init__(self, child_name:str, child_age:int, child_status: str):
        '''Constructor'''
        self._child_name = child_name
        self._child_age = child_age
        self._child_status = None
    

    @property 
    def child_name(self):
        ''' child property getter'''
        return self._child_name
    @child_name.setter
    def child_name(self, value):
        '''child name property setter'''
        self._child_name = value

    @property 
    def child_age(self):
        ''' child age property getter'''
        return self._child_age
    @child_age.setter
    def child_age(self, value):
        '''child age property setter'''
        self._child_age = value


    @property 
    def child_status(self):
        ''' child status property getter'''
        return self._child_status
    @child_status.setter
    def child_status(self, value):
        '''child status property setter'''
        self._child_status = value



    def play(self):
        '''Child is playing'''
        self._child_status = 'Playing!!!'

    def cry(self):
        '''Child is crying!!!!'''
        self._child_status = 'Crying!!!!'

    def __str__(self):
        '''__str__'''
        return str(self._child_name) + ' is ' + str(self._child_age) + ', and is currently ' + str(self._child_status)

    def __eq__(self, other):
        if self._child_name == other._child_name:
            if self._child_age == other._child_age:
                return 'This is the same child'
        else:
            return "These are different children"

class Sheep(Pets):
    '''Sheep class'''
    def __init__(self, name: str, age: int, inside: bool, fur_weight: float):
        '''Constructor'''
        self._sheep_name = name
        self._sheep_age = age
        self._inside = inside
        self._fur_weight = fur_weight

    def shear_fur(self, amount: float):
        '''Shear the fur off the sheep'''
        if self._fur_weight >= amount:
            self._fur_weight -= amount
            return "Fur has been sheared"
        else:
            return "Not enough fur to shear"

    def bahh(self):
        return str(self._sheep_name) + " says Bahhhhhh"

    def __str__(self):
        '''__str__'''
        return str(self._sheep_name) + ' is ' + str(self._sheep_age) + ' years old, and has ' + str(self._fur_weight) + ' pounds of fur.'

    def __eq__(self, other: object):
        if self._sheep_name == other._sheep_name:
            return "This is the same sheep!"
        else:
            return "These are different sheep!"

class Horse(Pets):
    '''Horses class'''
    def __init__(self, name: str, age: int, ride: bool, days_since_groom: int):
        '''Constructor'''
        self._horse_name = name
        self._horse_age = age
        self._ride = ride
        self._days_since_groom = days_since_groom

    @property 
    def ride(self):
        ''' ride property getter'''
        return self._ride
    @ride.setter
    def ride(self, value):
        '''ride property setter'''
        self._ride = value

    @property 
    def groom(self):
        ''' _days_since_groom property getter'''
        return self._days_since_groom
    @groom.setter
    def groom(self, value):
        '''_days_since_groom property setter'''
        self._days_since_groom = value


    def nayy(self):
        '''Horse is nayying'''
        return "Nayyyyyy"

    def groom_horse(self):
        self._days_since_groom = 0
        return "Horse has been groomed!"

    def __str__(self):
        '''__str__'''
        return str(self._horse_name) + ' is ' + str(self._horse_age) + ' years old.'
    
    def __eq__(self, other):
        if self._horse_name == other._horse_name:
            return "This is the same horse!"
        else:
            return "These are different horses!"