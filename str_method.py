import os 
os.system("cls")
os.system("color a")
name = "Pravindflkjakdlfjlkdjfirefjoifjoidoiejfoijoier\tjfoijf\tio\tefii"

print(name.capitalize())
print(name.casefold())
print(name.center(50,  "_")) 
print(name.count("i"))
print(len(name))
print(name.encode())
print(name.endswith("ii"))
print(name.expandtabs(10))
print(name.find("fire"))
print(name[name.find("fire"):name.find("fire")+len("fire")])


txt = "two apples for {price:.2f} only!"
print(txt.format(price =50))

print(txt.index("y"))