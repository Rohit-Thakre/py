import os 
os.system("cls")

lst = [1,2,3,4,5,6,7]

def square(lst): 
    lst2 = []
    for x in lst: 
        lst2.append(x**2)
    return lst2
print(square(lst))
# [1, 4, 9, 16, 25, 36, 49]


# using Map function
print(list(map(lambda x : x**2, lst)))
# here list can be also tuple or set
# [1, 4, 9, 16, 25, 36, 49]


