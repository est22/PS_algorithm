import collections
def solution(arr) :
    # 리스트의 순서를 유지하고, 원소의 중복 개수를 카운트하는 딕셔너리 생성
    counter = dict(collections.OrderedDict(collections.Counter(arr)))
    occurencies = list(counter.values())
    filter_number_one(occurencies)
    
def filter_number_one(arr):
    # 중복횟수가 없는 값 제거 (value값이 1인 element를 필터로 거름)
    answer = list(filter(lambda x:x>1, arr))
    # 중복횟수가 하나도 없는 리스트라면(빈 리스트라면)
    if not answer : 
        return [-1]
    else :
        return answer
        


solution([7,3,2,4,4,2,5,2,5,5,6])
solution([1,2,3,4,5])
