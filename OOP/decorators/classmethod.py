class person:
    # class variable
    counter = 0

    # instance methods
    def __init__(self, name, age):
        # instance variable
        if  person.counter > 1: 
            exit(1)
        self.name = name
        self.age = age
        person.counter = person.counter+1


    def print_all(self):
        print(f"Name:{self.name}, Age:{self.age}, Counter: {person.counter}")


    @classmethod
    def obj_counter(cls): 
        return cls.counter



p1 = person("suresh", 10)
p2 = person("jambo", 21)
p3 = person("temp", 15)
p4 = person("temp2", 17)


# print(person.counter)
# p1.print_all()
# p2.print_all() 
print("Counter :",person.obj_counter())

