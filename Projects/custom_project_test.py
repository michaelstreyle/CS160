'''
Testing the module Farm Family
Michael Streyle, 2018
'''

#!/usr/bin/python3


import pytest
from Custom_project import Adults, Children, Pets, Sheep, Horse


class TestFarmFamilyMethods:
    '''Testing module farm family'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.adult1 = Adults('John Doe', 52)
        self.adult2 = Adults('Jane Doe', 49)
        self.child1 = Children('Lil John Doe', 6, None)
        self.child2 = Children('Lil Jane Doe', 8, None)
        self.sheep1 = Sheep('Billy', 3, False, 10.0)
        self.horse1 = Horse("Bubba", 20, True, 3)
        self.horse2 = Horse("Bubba2", 23, False, 5)

    def test_adult(self):
        '''Testing adult properties'''
        assert self.adult1.name == 'John Doe'
        assert self.adult1.age == 52
        assert self.adult2.name == 'Jane Doe'
        assert self.adult2.age == 49

    def test_children(self):
        '''Testing children properties'''
        assert self.child1.child_name == 'Lil John Doe'
        assert self.child2.child_name == 'Lil Jane Doe'
        assert self.child1.child_age == 6

    def test_adult_eq(self):
        '''Testing adult.__eq__ method'''
        assert self.adult1 != self.adult2
        assert self.adult1 is not self.adult2
        assert self.adult1 == self.adult1

    def test_child_status(self):
        '''Testing children properties'''
        assert self.child1.child_name == 'Lil John Doe'
        assert self.child1.child_age == 6
        self.child1.play()
        assert self.child1.child_status == "Playing!!!"

    def test_customer_str(self, capsys):
        '''Testing child.__str__ method'''
        self.child1.play()
        print(self.child1)
        out, err = capsys.readouterr()
        assert out.strip() == ('Lil John Doe is 6, and is currently Playing!!!')


  
    def test_sheep_shearing(self):
        self.sheep1.shear_fur(5.0)
        assert self.sheep1._fur_weight == 5.0

    def test_horse_grooming(self):
        '''Testing horse shearing properties'''
        self.horse1._days_since_groom = 5
        self.horse1.groom_horse()
        assert self.horse1._days_since_groom == 0

        

    def test_horse_nayy(self):
        '''Testing horse.nayy method'''
        assert self.horse2.nayy() == "Nayyyyyy"

    def test_sheep_bahh(self):
        '''Testing sheep.bahh method'''
        assert self.sheep1.bahh() == "Billy says Bahhhhhh"


    def test_pet_is_eating(self):
        assert self.sheep1.eating() == "Pet is eating!"

    def test_pet_is_pottying(self):
        assert self.horse1.potty() == "Pet has gone to the bathroom!"

    def test_adult_reading(self):
        assert self.adult1.reading() == "John Doe is reading"

    def test_adult_working(self):
        assert self.adult2.work() == "Jane Doe is working"

    
if __name__ == '__main__':
    pytest.main(['custom_project_test.py'])