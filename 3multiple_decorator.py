# multiple decorator
def split(func): 
    def inner(): 
        string = func()
        return string.split()

    return inner


def upper(func): 
    def inner(): 
        string = func()
        return string.upper() 

    return inner


@split
@upper
def ordinary(): 
    return "hello world"



print("\nMultiple Decorator: \n", ordinary())

#----------------------------------------------------------------------------

# parameterised decorator 

def add_name(name): 
    def outter(func): 
        def inner(): 
            string = func()
            return  func() + name
        return inner
    return outter


@add_name("Rohit")
def normal(): 
    return "Hello, Good Morning "

print("\nParameterised Decorator :\n", normal())


#---------------------------------------------------------------------------------



# General Decorator 

def general(func): 
    def inner(*args): 
        list1 = []
        list1 = args[1:]
        for x in list1: 
            if x <= 0: 
                return "Give proper input !"
            else :
                return func(*args)
    return inner 



@general
def div(a,b): 
    return a/b

@general
def div1(a,b,c): 
    return a/b/c



print("\nGeneral Decorator : \n", div1(1,2,9))
