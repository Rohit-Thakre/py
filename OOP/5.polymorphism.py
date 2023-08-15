import os 
os.system("cls")
os.system("color a")

class person(object): 
    def __init__(self, name: str, age: int,sex:str): 
        self.name = name 
        self.age = age 
        self.sex = sex 


    def show_all(self):  # base function
        print(self.name, self.age, self.sex)





class men(person):
    def __init__(self, name, age, sex, height: int, skill:str): 
        self.height = height
        self.skill = skill
        person.__init__(self, name, age, sex)



    def show_all(self):  # funciton overriding
        print(self.name, self.age, self.sex, self.height, self.skill)



class female(person):
    def __init__(self,name, age, sex, isBeautiful):
        self.isBeautiful = isBeautiful
        person.__init__(self, name, age, sex)


    def show_all(self):  # function overriding 
        print(self.name, self.age, self.sex, self.isBeautiful)




p1 = person("pravin", 20, "male")
p1.show_all()


p2 = men("pravin", 20 , "male", 163,"java dev" )
p2.show_all()

p3 = female("jasica", 21, "female", "yes")
p3.show_all()