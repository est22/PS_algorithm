n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
largest = data[-1]
sec_largest = data[-2]

ans = 0

while True:
    for i in range(k):
        if m == 0 : break
        ans += largest
        m -= 1
    if m == 0: break
    ans += sec_largest
    m -= 1

print(ans)