def split_and_join(line):
    lst_txt = line.split(sep = " ")
    
    jn = "-".join(lst_txt)
    
    return jn
        
        
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)