'''
Banking classes implementation

Michael Streyle
9/28/18

'''
#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Address:
    '''Address class'''
    def __init__(self, street_init: str, city_init: str, state_init: str, zip_init: str):
        '''__init__'''
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    # TODO: Implement data members as properties
    @property
    def street(self):
        ''' Street property getter'''
        return self._street
    @street.setter
    def street(self, value):
        '''street property setter'''
        self._street = value
    
    @property
    def city(self):
        ''' City property getter'''
        return self._city
    @city.setter
    def city(self, value):
        '''city property setter'''
        self._city = value
    
    @property
    def state(self):
        ''' state property getter'''
        return self._state
    @state.setter
    def state(self, value):
        '''state property setter'''
        self._state = value

    @property
    def zip(self):
        ''' zip_code property getter'''
        return self._zip
    @zip.setter
    def zip(self, value):
        '''zip property setter'''
        self._zip = value




    def __eq__(self, other: object):
        '''Compare 2 addresses'''
        if str(self) == str(other):
            return self, '=', other

    def __str__(self):
        '''__str method'''
        return str(self._street) + '\n' + str(self._city.strip()) + ', ' + str(self._state.strip()) + ' ' + str(self._zip.strip())


class Customer:
    '''Customer class'''
    def __init__(self, name_init: str, dob_init: str, address_init: object):
        '''Constructor'''
        self._name = name_init
        self._dob = dob_init
        self._address = address_init
 # TODO: Implement data members as properties

    @property 
    def name(self):
        ''' name property getter'''
        return self._name
    @name.setter
    def name(self, value):
        '''name property setter'''
        self._name = value

    @property 
    def dob(self):
        ''' dob property getter'''
        return self._dob
    @dob.setter
    def dob(self, value):
        '''dob property setter'''
        self._dob = value

    @property 
    def address(self):
        ''' address property getter'''
        return self._address
    @address.setter
    def address(self, value):
        '''address property setter'''
        self._address = value


    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address

    def __str__(self):
        '''__str'''
        return str(self._name) + ' (' + str(self._dob) + ')\n' + str(self._address)


class Account(ABC):
    '''Account class'''
    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._balance = balance_init
    

    @property 
    def owner(self):
        ''' owner property getter'''
        return self._owner
    @owner.setter
    def owner(self, value):
        '''owner property setter'''
        self._owner = value

    @property 
    def balance(self):
        ''' balance property getter'''
        return self._balance
    @balance.setter
    def balance(self, value):
        '''balance property setter'''
        self._balance = value

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        '''Add money'''
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Must deposit positive amount')

    def close(self):
        '''Close account'''
        self._balance = 0

    def __str__(self):
        '''__str__'''
        return str(self._owner) +  str("{:.2f}".format(self._balance))


class CheckingAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, fee_init: float, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._insufficient_funds_fee = fee_init
        self._balance = balance_init

    def process_check(self, amount: float):
        '''Process a check'''
        if self._balance >= amount:
            self._balance -= amount
        else:
            self._balance -= self._insufficient_funds_fee

    def __str__(self):
        '''__str__'''
        return 'Checking account\n' + 'Owner: ' + str(self._owner) +'\n'+ 'Balance: ' + str("{:.2f}".format(self._balance))


class SavingsAccount(Account):
    '''SavingsAccount class'''
    def __init__(self, owner_init: object, interest_rate_init: float, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._interest_rate = interest_rate_init
        self._balance = balance_init

    @property 
    def interest_rate(self):
        ''' interest rate property getter'''
        return self._interest_rate
    @interest_rate.setter
    def interest_rate(self, value):
        '''interest rate property setter'''
        self._interest_rate = value


    def yield_interest(self):
        '''Yield annual interest'''
        self._balance += (self._balance * (self._interest_rate/100))
        return self._balance

    def __str__(self):
        '''__str__'''
        return 'Savings account\n' + 'Owner: ' + str(self._owner) +'\n'+ 'Balance: ' + str("{:.2f}".format(self._balance))