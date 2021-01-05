def pb_1 (str,k):
    
    count = 0
    new_list = []
    
    for i in range(0,len(str)):

        new_list.append(str[i])
        count += 1
        #print(new_list)
        if str[i] == '-':
            
            if count > k+1 : 
                # new_list.append(str[0:i])
                del new_list[i-(k+1):i]
                new_list.append("-" * k)
                
            i += count
            count = 0
    
            

    print(''.join(new_list)) 


pb_1("aa-bb-ccc-eef",2)

# def remove_triplicate(str):
#     res = []
#     i = 0
#     while i < len(str):
#         if i < len(str) - 2 and str[i]*3 == str[i:i+3]:
#             i += 3
#         else:
#             res += str[i]
#             i += 1
            
#     if len(res) == len(str):
#         return res
#     else:
#         return remove_triplicate(res)
    

# print (remove_triplicate("aabbbacdddcccdcccdcc"))
