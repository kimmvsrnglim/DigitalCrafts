class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet( self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)

#PROBLEM ONE

self = Person('Sonny',
    'sonny@hotmail.com', '483-485-4948')

print 'name: %s' % self.name
print 'email: %s' % self.email
print 'phone: %s' % self.phone

#PROBLEM TWO

self = Person('Jordan',
    'jordan@aol.com', '495-586-3456')

print 'name: %s' % self.name
print 'email: %s' % self.email
print 'phone: %s' % self.phone

#PROBLEM THREE
class Person(object):
    def __init__(self, name):
        self.name = name
    def greet (self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

sonny = Person('Sonny')
jordan = Person('Jordan')
sonny.greet(jordan)

#PROBLEM FOUR
jordan.greet(sonny)

#MAKE YOUR OWN CLASS

class Vehicle(object):
    def print_info(make, model, year):
        car.make = make
        car.model = model
        car.year = year

car = Vehicle('Nissan',
    'Leaf', 2015)

def print_info (make, model, year):
    print car.make, car.model, car.year
