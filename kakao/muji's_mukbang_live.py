def solution(food_times, k):
    food_times = list(map(int, input().split()))
    k = int(input())

    while True:
        for i in range(0, len(food_times)):
            food_times[i] -= 1
            if food_times[i] == 0 :
                i += 1
            elif food_times[i] == food_times[len(food_times)]:
                i == 0
            elif food_times[i] == k :
                print(i+1)
        else:
            return -1
            

solution([3,1,2],5)