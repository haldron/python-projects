"""
This python script contains one class and one inherited class
with each having its own functions
and testing for the functions
"""

class Dog():
    #Representing a dog

    def __init__(self, name):
        #initialise function for the dog object
        self.name = name

    def sit(self):
        #function to simulate sitting
        print(self.name + ' is sitting.')

my_dog = Dog('Peso')

print(my_dog.name + " is a great dog!")
my_dog.sit()

#inheritance of dog class
class SARDog(Dog):

    def search(self):
        #function to simulate searching
        print(self.name + " is searching.")

my_dog = SARDog('Willie')

print(my_dog.name +  " is a search dog.")
my_dog.search()
my_dog.sit()
