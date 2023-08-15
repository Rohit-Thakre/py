import os 

""" 
there are 2 types of constuctors: 
1.default 
2.parameterized 
"""
    
class student: 
    def __init__(self, name:str, age:int):
        assert type(name) == str , "string expecetd"
        assert age > 0, "positive age required."
        self.name = name
        self.age = age



# s1 = student("rohit", 20)
# print(s1.name) 
# print(s1.age) 


class Item: 
    # class attributes
    payRate = 0.8 #after applying 20% discount 

    all =[] 

    def __init__(self, name: str ,price: int , quantity : int):

        # validation
        assert type(name) ==str, "string value required."
        assert price > 0, f"price cannot be {price} or negative."
        assert quantity >0, f"quantity must be positive value, but given {quantity}."

        #assigning to self(object)
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)






    def calculate_price(self): 
        return self.price * self.quantity


    def after_discount(self): 
        return (self.price * self.payRate)  # this will first look for instace level parRate if not found then class level attribute
        # self.price * Item.payRate   # this will always clss level.



    def __repr__(self): 
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# itemL = Item("laptop", 40000, 10)
# itemL.payRate = 0.5 # 50% discount 
# print(itemL.calculate_price())
# print("After discount price(class level payRate):",itemL.after_discount()) # self.price * Item.payRate
# print("After discount price(instance level payRate):",itemL.after_discount()) #self.price*self.payRate



# itemM = Item("mobile", 15000, 50)
# print(itemM.calculate_price())


    
# # accessing class attributes
# print("from class Item payRate", Item.payRate)
# print("from instance of class Item payRate ", itemL.payRate)



# # checking class all attributes 
# print("class level attribute",Item.__dict__) 
# print("\n\ninstance level attribute",itemL.__dict__) 

os.system("cls")

item1 = Item("Phone", 1000,1)
item1 = Item("Laptop", 100,3)
item1 = Item("Cable", 10,5)
item1 = Item("Mouse", 50,5)
item1 = Item("Keybord", 75,5)


# print(Item.all)
# output :
#  [<__main__.Item object at 0x0000022CECCA68C8>,
#  <__main__.Item object at 0x0000022CECCA6908>,
#  <__main__.Item object at 0x0000022CECCA6948>, 
# <__main__.Item object at 0x0000022CECCA6988>,
# <__main__.Item object at 0x0000022CECCA69C8>]

print(Item.all)
# to make above code look good we have magic method __repr__()


# for x in Item.all:
#    print(x.name,x.price,x.quantity)