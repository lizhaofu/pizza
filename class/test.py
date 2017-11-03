from dog import Dog
import pygame

my_dog = Dog("willie", 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " year old.")

my_dog.sit()
my_dog.roll_over()