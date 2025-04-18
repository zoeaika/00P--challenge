class pet1:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger -3) #2
        self.happiness = min(10, self.happiness + 1) #6
        
    def sleep(self):
        self.energy = min(10, self.energy + 5) #10
    
    def play(self):
        self.energy =  max(0, self.energy - 2) #8
        self.happiness = min(10,self.happiness + 2) #8
        self.hunger = max(0, self.hunger + 1) #3

    def get_status(self):
        print(f"The pet's name is {self.name} and its hunger level is {self.hunger}, energy level is {self.energy}, and happiness level is {self.happiness}.")
    
    def train(self, trick):
        if  self.tricks.append(trick):
            self.happiness = min(10, self.happiness + 1)
            
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to learn a new trick.")
        
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {self.tricks}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
    
class parrot(pet1):
    def __init__(self, name):
        super().__init__(name)
        self.hunger = 3  # Different initial hunger level
        self.happiness = 7  # Different initial happiness level
        self.energy = 8  # Different initial energy level

    def fly(self):
        if self.energy > 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} is flying high in the sky!")
        else:
            print(f"{self.name} is too tired to fly.")
    
pet1 = pet1("Kifaru")
pet1.get_status()
pet1.eat()
pet1.sleep()
pet1.play()
pet1.get_status()
pet1.train("roll over")
pet1.train("play dead")
pet1.show_tricks()

#pet 2
pet2 = parrot("Laiti")
pet2.eat()
pet2.sleep()
pet2.fly()
pet2.get_status()