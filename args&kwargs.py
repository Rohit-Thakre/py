# normal fucntion
def normal(x ,y ): 
    print(x)
    print(y)

# print(normal(10, 50))
# output:
# 10
# 50


# print(normal(10,23,33))
# output : TypeError: normal() takes 2 positional arguments but 3 were given

# to avoid above error we use *args keyword to give multiple arguments to a function
def arg_func(*args): 
    for x in args: 
        print(x)

# method 1: using multiple arguments
arg_func(1,2,3,5)
# output: 
# 1
# 2
# 3
# 5

# method 2: using list 
arg_func([1,2,3,6]) #o/p: [1, 2, 3, 6]
arg_func(*[1,2,3,6])  # look at * given in next statement and it prints all values if we don't give * then it retun list
# o/p:
# 1
# 2
# 3
# 6



"""  -------------------------------------------------------------------------------------------------------- """
import os 
os.system("cls")

# **kwargs 
# it requires Dictionary

def kwargs(**kwargs): 
    for key, value in kwargs.items(): 
        print(key, value)

# calling using Dictionary
dctnr = {'name' :'rohit', 'lives': 'Nagpur', 'state':'maharastra'}
kwargs(**dctnr)


# calling directly
# kwargs('name' = 'rohit', 'lives' = 'nagpur', 'state' = 'maharastra')




os.system("cls")

def function( name, lst): 
    print(name)
    for x in lst:
        print(x)


lst = [x  for x in range(1,11)]
print(sum(lst))

function("name", lst)
