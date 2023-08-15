"""
Types of inheritance:
1. single inheritance : child class derived from only one parent class
2. multiple inheritance : child class derived from two or more parent class 
3.multilevel inheritance : child class is derived from parent of parent class
"""



class base1(object) : 
    def __init__(self, name , age):
        self.name = name
        self.age = age

        print(self.name, self.age)




class base2(object):
    def __init__(self, sex):
        self.sex = sex

        print(self.sex)



# single inheritance 
class sub(base1):
    def __init__(self, name, age, post, sallary):
        self.post = post
        self.sallary = sallary
        base1.__init__(self, name, age)

        print(self.name, self.age, self.post, self.sallary)


class sub2(base1, base2): 
    def __init__(self, name, age, sex, std):
        self.std = std 

        base1.__init__(self, name, age)
        base2.__init__(self, sex)

        print(self.name, self.age, self.sex, self.std)






print("base")
b = base1("rohit", 20)

print("\n\nsub:single inheritance")
s = sub("rohit", 20, "dev", "50k")


print("\n\nsub 2 : multiple inheritance")
s2 = sub2("nitu", 19, "female", 12)


