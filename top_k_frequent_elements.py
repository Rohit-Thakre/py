# input = [4,1,-1,2,-1,2,3]
# input = [1,1,1,2,2,3]
input = [1]
k = 1


def sol(input , k): 
    hash = dict()
    for x in set(input): 
        hash[x] = input.count(x)


   
    print("origional :", hash)
    ans = list()
    for x in range(k): 
        hash_key = list(hash.keys())
        hash_value = list(hash.values())
        
        mx = max(hash.values())
        idx = hash_value.index(mx)
        key = hash_key[idx]

        ans.append(key)
        # print("idx:", idx)
        # print("key:", key)
        print("apnd :", key)

        del hash[key]
        print(hash)


    return ans 



ans = sol(input, k)
print(ans)



        


# hash = {1: 1, 2:2 , 3:1,4:1, -1:2}
# reverse_hash = {value : key for key, value in hash.items()}
# print(reverse_hash)


