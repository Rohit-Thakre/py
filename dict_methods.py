
""" 
# characteristics of dictionary:

mutable. entries can be added, removed, and changed 
Ordred. do maintain Ordred sequence 
dynamic. They can grow and shrink as needed.
can be nested. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.


 """



import os 
os.system('cls')

dict = {"name" : "rohit", "lname" : "thake", "age": 20}
# print(dict)
# O/P: {'name': 'rohit', 'lname': 'thake', 'age': 20}



# for accessing keys of the dict 
# print(dict.keys())
# O/P : dict_keys(['name', 'lname', 'age'])



# to access values of dict 
# print(dict.values())
# O/P: dict_values(['rohit', 'thake', 20])



# get selective value of dict 
# print("age is : ",dict["age"])
# O/P: age is :  20


# there is also another method for accessing values
# syntax : dict.get(key)



# loop through dict keys and values
# for key, value in dict.items():
#     print(key, ":", value, end= ",\t")
# O/p: name : rohit,   lname : thake,  age : 20,



# adding element in dict 
# dict["job"] = "NA"
# print(dict)
# O/P : {'name': 'rohit', 'lname': 'thake', 'age': 20, 'job': 'NA'}



# adding set of values to single dict key
# dict["hobbies"] = "codding", "cooking", "travel"
# print(dict)
# O/P : {'name': 'rohit', 'lname': 'thake', 'age': 20, 'hobbies': ('codding', 'cooking', 'travel')}




# deleting key value 
# del dict["age"]
# print(dict)
# O/P :{'name': 'rohit', 'lname': 'thake'}


# using pop method  
# v = dict.pop("age")
# print(dict)
# print("poped key value of age :", v)
# O/P : {'name': 'rohit', 'lname': 'thake'}
        #poped key value of age : 20



#  deleting entire dict 
# dict.clear()
# print(dict)
# O/P : {}


