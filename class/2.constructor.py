""" 
there are 2 types of constuctors: 
1.default 
2.parameterized 
"""
    
class student: 
    def __init__(self, name:str, age:int):
        assert type(name) == str , "string expecetd"
        assert age > 0, "positive age required."
        self.name = name
        self.age = age



s1 = student("roiht", 20)
print(s1.name) 
print(s1.age) 