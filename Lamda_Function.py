import os 
os.system("cls") 

def double(a): 
    return a*2

print("regular Function double :",double(5))

# using labda function
Double = lambda x: x*2
print("lambda function Double", Double(5))




def add(a,b ): 
    return a+b 

Add = lambda a,b: a + b
print("Lambda add: ",Add(20,10))

def max(a,b):
    if a > b: 
        return a 
    else: 
        return b 


print("Regular Max  :", max(20, 50))

Max = lambda x , y : x if x > y else y
print("lambda max :",Max(20,50)) 