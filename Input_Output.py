# #list comprehesion method to take more than one input in single line. 

# x , y = [ int(x) for x in input("input: x,y (list comprehension method)").split()]
# print("x :" , x ,"y: " , y)




# # using map function 
# a , b ,c = map(int , input("input ,a,b,c(map method)").split())
# print("a:{a:},b:{b:},c:{c:}".format(a = a,b = b,c = c))



# using map function but this time in single variable 
lst = list(map(int , input("list method: input as much as posible: ").split()))
print(lst)

def pprint(start , *args): 
    print(start)
    print(type(args))

    # print(*args,  sep='\n')

    # list(map(print, *args))

    list(map(lambda x:print(x), args))
    # list(map(lambda x:print(x), *args))  #both works fine

    # for x in args:
    #     print(x)

pprint("start", *lst) # this will now work for 1st print statement bcoz value passed by one by one and it accepts iterable
# pprint("start", lst)


