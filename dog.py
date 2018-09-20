# dogs = list()
# dogs.append("German Shepherd")
# dogs.append("Poodle")
# print(dogs)

# creating class Dog that has object named bark. However, you cant just call method bark()
#  because it is equal to try to make ALL dogs to bark>>> not gonna work.
# Instead you can use this class for SPECIFIC dog >>> created instance.


# class Dog:
#     def bark(self):
#         print("Woof!")


# created instance my_dog that can relate to Dog class
# my_dog = Dog()
# asking ONE dog to bark
# my_dog.bark()

# when dog.py is imported the name of this file is printed in the 
# terminal when the other file is run, in this case, when my-dog.py is run

# print(__name__)


# class Dog:
#     def bark(self):
#         print("Woof!")
        # the following line checks if the method is run modular
# if __name__ == "__main__":
#     my_dog = Dog()
#     my_dog.bark()


class Dog:
    greeting = "Woof!"

    # using init to set initial value at the time our object is created
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)

# using constructor to specify unique name for our dog
my_first_dog = Dog("Spot")
print(my_first_dog.name)

# creating new dog 
my_second_dog = Dog("Annie")
print(my_second_dog.name)

my_first_dog.bark()
my_second_dog.bark()
