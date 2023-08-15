""" 
3 types of encapsulation
1.public : all data can be accessed from out of the class.
2.private : data can be accessed from same class only
3.protected: data can accessed from same class and inherited classes. 

"""

class student: 
    # public
    def __init__(self,name,age, std): 
        self.name = name #public
        self._age = age # protect 
        self.__std = std # private


    # getter
    def get_std(self): 
        return self.__std

    # setter 
    def set_std(self, std):
        self.__std = std


class boy(student): 
    def __init__(self,name, age, std, sex):
        self._sex = sex
        student.__init__(self, name, age, std)
        

        print("age : ", self._age, "sex :" , self._sex)
    

obj = student("rohit", 20, 12)
print("name :" ,obj.name)

obj2 = boy("Ram",19, 10, "male")

#  direct access to private member using name mangling
print("std :", obj._student__std)

obj.set_std(9)
print("std(using getter) :", obj.get_std())


