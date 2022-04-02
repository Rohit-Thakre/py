""" there are 2 types of class decorators 
1. function decorator
2. class decorator """
# check out 
# fucntool.wraps


# 1.function decorator

def check_name(method): 
    def inner(self): 
        if self.name == "Rohit": 
            print("hey my name is also Rohit!")
        else: 
            method()
    return inner


class printing: 
    def __init__(self, name): 
        self.name = name

    @check_name
    def print_name(self): 
        print("The entred name is : ", self.name)


p = printing("Rohit")
p.print_name()


# ----------------------------------------------------------------
print(" _" * 50 , end= "\n\n")





# 2.class decorator
# example 1:
class cls_Decorator: 
    def __init__(self, func): 
        self.func = func

    def __call__(self):
        str1 = self.func()
        return str1.upper()

    # def split_txt(self): 
    #     str2 = self.func()
    #     return str2.split()

@cls_Decorator
def greet(): 
    return "Good Morning !"


print(greet())



# exmaple 2: 
print(" -"*50, end= "\n\n")
print("example 2", end = "\n\n")

class check_div(): 
    def __init__(self, func): 
        self.func = func
    
    def __call__(self, *args, **kwargs):
        lst = []
        lst = args[1:]

        for x in lst: 
            if x <= 0: 
                return "you should not divide any number by 0;"
        else:
            return self.func(*args, **kwargs)
        

@check_div
def div(a,b): 
    return a/b

@check_div
def div1(a,b,c): 
    return a/b/c

@check_div
def div2(a,b,c,d):
    return a/b/c/d


print(div1(1,2,0))