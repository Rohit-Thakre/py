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







def decorated(func): 
    def inner(): 
        print("start")
        func()
        print("end")
       
    return inner



@decorated
def origional(): 
    print ("i'm Origional.")



result = decorated(origional)
result()
print("-------------------after using @decorated-------------------------")
origional()
