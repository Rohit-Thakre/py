
"""binary search program in python """
import os 
import math
lst=[0,1,2,3,4,5,6,7,8,9,10]
choice = 1
os.system('cls')
print(lst)
while True: 
    print("\nwhat do you want to do ?\n1. Enter element in list\n2. remove element from list. \n3. print list.\n4 .search element\n5. Exit\n")
    choice = int(input("\nEnter your choice : "))

    if choice ==1:
        element = int(input("Enter your element here : "))
        lst.append(element)
        print(lst)



    elif choice ==2 : 
        remove = int(input("\nEnter an element to remove from given list: "))
        lst.remove(remove)
        print("now list looks like : ",lst)
    
    elif choice == 3:
        lst.sort()
        print("The list is:")
        print('index\telement')
        for index , item in enumerate(lst, start = 0):
            print(index,"\t", item)

    elif choice ==4:
        lst.sort()
        print("sorted list :", lst)
        find = int(input("\nEnter the element to search in list/ array: "))
        mid = len(lst) /2
        mid = int(math.ceil(mid)) 
        count = mid
        print('mid :',mid)
        for x in lst:
            if find == lst[mid] :
                break
            elif lst[mid] < find: 
                lst = lst[mid:]
                mid = len(lst)/ 2 
                mid = math.ceil(mid)
                count = mid + count
                
                # mid = mid + new_mid 
                if mid >= len(lst):
                    break
            elif lst[mid] > find: 
                lst = lst[:mid]
                mid = len(lst) / 2 
                mid =math.ceil(mid)
                count = count - mid
                # mid = mid - new_mid 
                if mid <= 0:
                    break
            else:
                break


        if lst [mid] == find:
            print("\nsearch was done successfully !")
            print("\nThe element you are looking for is found at position :", count)
        else: 
            print("\nThe search was unsuccessful \n")
            print(f"element {find} not found in the given list/array")

    
    elif choice == 5: 
        exit()
    
    else :
        print('invalid option !')


 
