# #  Procedure-Oriented Programming 
# a =  10
# b = 10

# add = a+b
# print(add)

## function programming
# it is used to avoid redundancy and make the code cleaner by using pure functions 

# def add(num1 , num2):
#   print(num1 + num2)

# add(10,20)
# add(30,40)
# add(10,40)
# add(40,40)
# add(60,40)
# add(70,40)


## object oriented programming

# class student:
#     name = "Atharva"
    
# s1 = student()
# print(s1.name)

# s2 = student()
# print(s2.name)

# s3 = student()
# print(s3.name)

# s4 = student()
# print(s4.name)


# class car:
#     color = "blue"
#     brand = "mercendes"
#     tyre = "4"
    
# car1 = car()
# print(car1.color)
# print(car1.brand)
# print(car1.tyre)


#  init function
#  When you create something using a class, Python needs a way to set it up. That’s what __init__() does — it initializes (starts) the object with some values.

# class car:
#   def __init__(self, color, brand, tyres):
#     self.car_color = color
#     self.car_brand = brand
#     self.car_tyres = tyres

# car1 = car("blue","mercedes","4")
# print(car1.car_color)
# print(car1.car_brand)
# print(car1.car_tyres)

# car2 = car("red","tata","3")
# print(car2.car_color)
# print(car2.car_brand)
# print(car2.car_tyres)

# car3 = car("green","BMW","4")
# print(car3.car_color)
# print(car3.car_brand)
# print(car3.car_tyres)


##   __str__() defines what you see when you print an object of a class.

# without using __str__ function

# class student:
#     def __init__(self, firstname):
#         self.firstname = firstname  
    
# s1 = student("Atharva")
# print(s1.firstname)


# # after using __Str__ function

# class student:
#     def __init__(self, firstname, lastname ):
#         self.firstname = firstname  
#         self.lastname = lastname  
    
#     def __str__(self):
#         return f"student name: {self.firstname} {self.lastname}"
    
# s1 = student("Atharva","kesarkar")
# print(s1)




# # What are Object Methods?
# # •	When we create a class, we can also create functions inside that class.
# # •	These functions are called methods.
# # •	They belong to the object (they work with the object’s data).

# class Person:
#     def __init__(self, name):
#         self.name = name  

#     def say_hello(self):  
#         print("Hello! My name is", self.name)
        
# p1 = Person("Atharva")
# p1.say_hello()  


# # Modify Object Properties
# # You can modify properties on objects like this:

# class Person:
#   def __init__(self,  age):
#     self.age = age

# p1 = Person(36)

# p1.age = 40

# print(p1.age)


# Delete Object Properties
# You can delete properties on objects by using the del keyword:

# class Person:
#   def __init__(self,  age):
#     self.age = age

# p1 = Person(36)

# del p1.age

# print(p1.age)


## The pass Statement
## class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Person:



# # Inheritance
# # Inheritance is a feature in Python where one class (child class) can use the code (variables and methods) from another class (parent class) without writing it again.


# class human:
#     def eat(self):
#         print("yes i have eat")
    
#     def work(self):
#         print("yes i have done the work")  


# class male(human):
#     pass
    
# male_1 = male()
# male_1.eat()
# male_1.work()



# class human:
#     def eat(self):
#         print("yes i have eat")
    
#     def work(self):
#         print("yes i have done the work")

# class male(human):
#     def play(self):
#         print("yes i have played the game")
    
# male_1 = male()
# male_1.eat()
# male_1.play()
# male_1.work()



# class human:
#     def eat(self):
#         print("yes i have eat")
    
#     def work(self):
#         print("yes i have done the work")

# class male(human):
#     def play(self):
#         print("yes i have played the game")

# class female(male):
#     pass

# female_1 = female()
# female_1.eat()
    
# male_1 = male()
# male_1.eat()
# male_1.play()
# male_1.work()



# # # overidding

# class human:
#     def eat(self):
#         print("yes i have eat")
    
#     def work(self):
#         print("yes i have done the work")

# class male(human):
#     def work(self):
#         print("i have done the coding")
    
# male_1 = male()
# male_1.eat()
# male_1.work()


## use of super funciton

# class human:
#     def eat(self):
#         print("yes i have eat")
    
#     def work(self):
#         print("yes i have done the work")

# class male(human):
#     def work(self):
#         super().work()
#         print("i can do coding")
    
# male_1 = male()
# male_1.eat()
# male_1.work()





# # use of attributes
# class Human:
#     def __init__(self, eyes, hand):
#         self.eyes = eyes 
#         self.hand = hand   


# class Male(Human):
#     pass

# male_1 = Male(2,2)
# print(male_1.eyes)
# print(male_1.hand)
