n = int(input())

for i in range(n):
    how_many = 0
    scores = list(map(int,input().split())) ### list, map, split()
    avg = sum(scores[1:])/scores[0]
    
    for score in scores[1:]: ### scores index range
        if score > avg:
            how_many += 1
    print("{:.3f}%".format(how_many / scores[0] * 100,3)) ### format 함수 

## split() : 공백 구분이면 괄호 안에 아무것도 넣지말기
## for문 안에 scores 인덱싱 슬라이스 범위를 꼭 명시
## format 함수 잘 알아놓기
## 계속 틀렸습니다 => how_many 를 for문 안에 넣기!