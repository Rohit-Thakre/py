""" property decorator does:
1. class method to attribute
2. repalce getter, setter by property  """


""" 
# 1. class method to attribute
class student: 
    def __init__(self, name , grade): 
        self.name = name 
        self.grade = grade 

    @property
    def msg(self): 
        return self.name + " got grade " + self.grade

s1 = student("Rohit", "A")
print(s1.msg)

 """

""" 
# 2. repalce getter and settter by propery decorator
# example 1:
class student: 
    def __init__(self, name , grade): 
        self.name = name 
        self.grade = grade

    @property
    def msg(self): 
        return self.name +" got grade " + self.grade
    
    @msg.setter
    def msg(self, msg): 
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0] 
        self.grade = sent[-1] 
    

s2 = student("sia", "B")
s2.msg = "Sia got grade B"

print(s2.msg)
print("Name : ", s2.name)
print("Grade : ", s2.grade)

"""

# example 2: 

class student: 
    def __init__(self, marks): 
        self.__marks = marks

    def per(self): 
        return (self.__marks / 600)* 100


    # @property
    # def marks(self): 
    def getter(self): 
        print("getting the marks: ", end = " ")
        return self.__marks
    
    # @marks.setter
    # def marks(self, value):
    def setter(self, value):
        if value < 0 or value >= 600: 
            print("can't set the value, stick with privious one !!!")
        self.__marks = value
        print("setting the marks: ", self.__marks)

    marks = property(getter, setter)


s3 = student(550)
s3.marks = 450
print(s3.marks)
print("Per :",s3.per())