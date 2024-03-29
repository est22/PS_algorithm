# 나는야 포켓몬 마스터 이다솜
# 딕셔너리 두개 만들기
import sys

input = sys.stdin.readline

_dict1, _dict2 = {}, {}
N, M = map(int, input().rstrip().split())

for i in range(N):
    name = input().rstrip()
    _dict1[name] = i + 1
    _dict2[i+1] = name

for i in range(M):
    target = input().rstrip()
    if target.isdigit():
        print(_dict2[int(target)])
    else:
        print(_dict1[target])

# 1. input() 뒤에 다 .rstrip() 붙이는게 나을수도
# 2.
# 3. 함수를 새로 만들어라.. 
'''
def input():
    return sys.stdin.readline().rstrip()
'''