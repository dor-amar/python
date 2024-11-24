# class Dog: 
#     number_of_legs = 4 
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed 

#     def bark(self):
#         print(f"{self.name} says Woof")
    
#     def drink():
#         print("The dog is drinking water")
    
# my_dog = Dog("Buddy","Golden")
# my_dog2 = Dog("Rex","German Sheperd")
# print(my_dog.name)
# print(my_dog.breed)
# my_dog.bark()

# Example 2 

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def start_engine(self):
#         print(f" The {self.year} {self.make} {self.model} engine is running !")


# my_car = Car("Tesla", "S", 2024)
# my_car2 = Car("Mazda", "3", 2024)
# my_car2.start_engine()

# Example 3 

# class Circle:
#     pi = 3.141

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return Circle.pi * (self.radius ** 2)    

# my_circle = Circle(5)
# print(my_circle.area())


# Inheritance 
# class Animal: 
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         pass

#     def eat(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof !"
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow !"

# my_dog = Dog("Buddy")
# my_cat = Cat("Mitzi")

# print(my_dog.speak())
# print(my_cat.speak())


# Senario 
class BankAccount: 
    my_string = "hello"
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.__balance = balance # Private 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Your new balance is ", self.__balance)
        else:
            print("Deposit money")
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print("Your new balance is ", self.__balance)
        else:
            print("No money")

my_bank_account = BankAccount("Dor")
my_bank_account.deposit(700)
my_bank_account.deposit(700)
my_bank_account.withdraw(200)


