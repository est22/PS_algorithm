# 셀프 넘버
natural = set(range(1,10001))
self_num = set()

for i in range(1,10001): # i = 924
    for j in str(i): # j = "9", "2", "4"
        i += int(j) # i = 924 + 9 + 2 + 4 = 939
    self_num.add(i) # 생성자가 있는 숫자(i)를 넣음.

self_num = sorted(natural - self_num)
for i in self_num:
    print(i)
    
