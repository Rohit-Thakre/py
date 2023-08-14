# swap the cases 
def swap_case(txt):
    txt = txt.swapcase()
    return txt

if __name__ == '__main__' :
    text = str(input("Enter your text here")) 
    # Hello World ---> hELLO wORLD 
    result = swap_case(text)
    print("input text: ", text)
    print("swap  text: ",result)

