import os 
os.system("cls")
""" def inc(x): 
    return x+1 


def dec(y): 
    return y -1


def operator(func, x): 
    result = func(x)
    return result




print(operator(inc , 5))
print(operator(dec, 5))
 """




# def called(): 
#     def returned(): 
#         # print("hello world")
#         return "Hello world"
    
#     return returned

# cld = called()

# print(cld())



def decorated(func): 
    def inner(): 
        print("I'm Decorated.")
        # func()
        # return "i'm Decorated"
    return inner



@decorated
def origional(): 
    print ("i'm Origional.")



result = decorated(origional)
result()
print("-------------------after using @decorated-------------------------")
origional()