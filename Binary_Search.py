
"""binary search program in python """
import math
lst=[0,1,2,3,4,5,6,7,8,9]
choice = 1

print(lst)
while True: 
    print("\nwhat do you want to do ?\n1. Enter element in list\n2.search element\n3.print list.\n4.Exit\n")
    choice = int(input("\nEnter your choice : "))

    if choice ==1:
        element = int(input("Enter your element here : "))
        lst.append(element)
    
    elif choice ==2:
    # import math 
        lst.sort()
        print("sorted list :", lst)
        find = int(input("\nEnter the element to search in list/ array: "))
        mid = len(lst) /2
        mid = int(math.ceil(mid)) 
        print("first element of lst", lst[0])
        for x in range(len(lst)):
            if lst[mid-1] < find: 
                new_lst = lst[mid:]
                new_mid = len(new_lst)/ 2 
                new_mid = math.ceil(new_mid)
                mid = mid + new_mid +1
                if mid >= len(lst):
                    break
            elif lst[mid -1] > find: 
                new_lst = lst[:mid-1]
                new_mid = len(new_lst) / 2 
                new_mid =math.ceil(new_mid)
                mid = mid - new_mid 
                if mid <= 0:
                    break

            elif find == lst[mid-1] :
                break
            else:
                break
        if lst [mid -1] == find:
            print("\nsearch was done successfully !")
            print("\nThe element you are looking for is found at position :", mid)
        else: 
            print("\nThe search was unsuccessful \n")
            print(f"element {find} not found in the given list/array")

    elif choice == 3:
        lst.sort()
        print("The list is:\n")
        for index , item in enumerate(lst, start = 0):
            print(index, item)
    
    elif choice == 4: 
        exit()


 