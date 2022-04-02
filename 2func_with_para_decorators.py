def dec_txt(func): 
    def inner(): 
        string = func()
        return string.upper()
    return inner

    


@dec_txt
def txt(): 
    return "hello world"


print(txt())







# if function is taking parameters
def div_dec(func): 
    def inner(a,b): 
        if b <= 0 :
            return "divisior must be greater than zero, else it will generate an error."
    
        return func(a,b) 
    return inner



@div_dec
def div(a, b ): 
    return a/b 


print(div(4, 0))