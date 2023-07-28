class Vehicle:
    '''
        Task 1: Create a class Vehicle with the attributes: name, speed, and mileage.
        Implement the methods: __init__, a method to change the speed, and a method to get speed.
    '''
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage


    def change_speed(self, new_speed):
        self.speed = new_speed
       

    def get_speed(self):
        return self.speed
        


class Animal:
    '''
        Task 2: Create a class Animal with the attributes: name, age, and type.
        Implement the methods: __init__, a method to change the age, and a method to get age.
    '''
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
        

    def change_age(self, new_age):
        self.age = new_age
        

    def get_age(self):
        return self.age
        


class Plant:
    '''
        Task 3: Create a class Plant with the attributes: name, height and type.
        Implement the methods: __init__, a method to change the height, and a method to get height.
    '''
    def __init__(self, name, height, type):
        self.name = name
        self.height = height
        self.type = type
        

    def change_height(self, new_height):
        self.height = new_height
        

    def get_height(self):
        return self.height
        


class Tree(Plant):
    '''
        Task 4: Create a class Tree which inherits from the Plant class.
        Add a new attribute: age. Also add a new method to change the age, and a method to get age.
    '''
    def __init__(self, name, height, type, age):
        self.name = name
        self.height = height
        self.type = type
        self.age = age
        

    def change_age(self, new_age):
        self.age = new_age
        

    def get_age(self):
        return self.age
        
