def pb_1 (str,k):
    str_list = [str]
    times = 0
    for c in str_list:
        times += 1
        if c == "-":
            if times > k:
                c.replace(c,"-")
    print (str_list)

pb_1("aa-bb-ccc-eef",2)