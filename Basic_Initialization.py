
class Dog:
    
    def __init__(self, name, breed, sex, age, weight):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.weight = weight

    
    def printDogProfile(self):
        print('Name: ', self.name)
        print('Breed: ', self.breed)
        print('Sex (M/F): ', self.sex)
        print('Age: ', self.age)
        print('Weight: ', self.weight)

        
        
pitbull = Dog('Thor','Pitbull','M','1 month','65 lbs')

pitbull.printDogProfile()
        
    
