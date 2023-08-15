import os 
os.system("cls")

def roman_to_normal(s):


    s = list(s)
    result = []
    dct = {"I" : 1, "V" :5,  "X" : 10, "L": 50, "C": 100, "D": 500, "M" : 1000}


    for i in range(len(s)):
        result.append(dct[s[i]]) 


        if(result[i]>result[i-1]):
            result[i] = result[i] - result[i-1]
            result[i-1] = 0 
            

            
    
    return sum(result)





# date of birth 
print(roman_to_normal("XXV"))
print(roman_to_normal("XI"))
print(roman_to_normal("MMI"))




