n = [1,2,3,4,5,6]
# regular simple fucntion
def over_two(lst): 
    lst = [x for x in lst if x >2] # list comprehension
    return lst

print(over_two(n))


# using filter 
print(list(filter(lambda x: x > 2 , n)))


