import os 
os.system("cls")


nums = [1,2,3,4,5,6,7,8,9,10]
myList = []

# i want n for each n in nums in myList 
# for x in nums: 
#     myList.append(x)
# print(myList)

# -----------------------------------------
myList = [x for x in nums]
print(myList)
# ------------------------------------------



# i want n*n for each n in nums in myList 
# for n in nums: 
#     myList.append(n*n)
# print(myList)

# ------------------------------------------
# myList = [x*x for x in nums]
# print(myList)
# --------------------------------------------



# i want n for each n in nums in myList if n is even 
# for x in nums: 
#     if x%2 ==0:
#         myList.append(x)
# print(myList)

# ------------------------------------------------
# myList = [x for x in nums if x%2==0]
# print(myList)
# ----------------------------------------------------



# i want (letter, num ) pair of each letter of "abcd" and each number of "0123"
# for letter in "abcd": 
#     for number in range(4):
#         myList.append((letter,number))
# print(myList)

# -----------------------------------------------------------------
# myList = [(letter, nums) for letter in "abcd" for nums in range(4)]
# print(myList)
# -------------------------------------------------------------------
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


""" Dictionary Comprehension """

myDict = {}
names = ["Bruce", "Clark", "Peter", "Logon", "Wade"]
heros = ["Batman", "Superman", "Spiderman","Wolverine", "Deadpool"]
# print(zip(names, heros))

# for name, hero in zip(names, heros):
#     myDict[name] = hero
# print(myDict)

#output for both:  {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logon': 'Wolverine', 'Wade': 'Deadpool'}

# -----------------------------------------------------------
# myDict = {name:hero for name, hero in zip(names, heros)}
# print(myDict)
# -------------------------------------------------------------


# --------------------------------------------------------------------------
# escaping keys  # not going to add "Logon" : "Wolverine" key : value pair
# myDict = {name : hero for name , hero in zip(names, heros) if name != "Logon"}
# print(myDict)
# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Wade': 'Deadpool'}
# ------------------------------------------------------------------------------------




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



""" Set Comprehension """

nums = [1,2,4,3,2,4,6,5,4,6,8,7,6,4,8,9,8,6,4,3,1]
mySet = set()
# for x in nums: 
#     mySet.add(x)
# print(mySet)

# -----------------------------------------------------
# mySet = {x for x in nums}
# print(mySet)
# -------------------------------------------------------
#output :  {1, 2, 3, 4, 5, 6, 7, 8, 9}
