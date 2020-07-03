# self is a key word
# method is a function in the class that will work with an object in some way
# class Dog():
#     # Class object attribute. Same for any instance
#     species = 'mammal'

#     # init is for creating an instance of class
#     def __init__(self, mybreed, name, spots):

#         self.breed = mybreed
#         self.name = name
#         self.spots = spots

#     # operations/actions ---->Methods
#     def bark(self, number):
#         print('WOOF My name is {} and the number is {}'.format(self.name, number))
    

# # expect boolean true/false
# my_dog = Dog(mybreed='Lab', name='Korra', spots=False)
# my_dog2 = Dog('Husky', 'Sitka', False)

# print(my_dog.name)

# my_dog.bark(10)

# class Circle():
#     # Class Object Attribute
#     pi = 3.14

#     def __init__(self, radius=1):

#         self.radius = radius

#         # method
#     def get_circumference(self):
#         return self.radius * pi * 2

class Animal():
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am a eating')

myanimal = Animal()
myanimal.who_am_i()


# runs init off of animal, dog can access animal methods
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    # can overwrite other method
    def who_am_i(self):
        print('I am a dog')

mydog = Dog()
mydog.who_am_i()



# Polymophism
class Dogs():
    def __init__(self,name):
        self.name =  name

    def speak(self):
        return self.name + ' says woof'

class Cat():
    def __init__(self,name):
        self.name =  name

    def speak(self):
        return self.name + ' says meow'

niko = Dogs('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

for pet_class in [niko,felix]:
    print(type(pet_class))
    print(type(pet_class.speak()))

# Abstract class
class Animals():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplemented('SubClass must implement absract method')


class Doge(Animal):
    def speak(self):
        return self.name + " says meow"

fido = Dog('Fido')