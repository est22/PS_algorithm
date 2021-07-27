
# def josephus_sequence(n, k) :
#     #   n명의 사람들을 큐로 표현
#     q = Queue()
    
#     result = []
    
#     for i in range(1, n + 1):
#         q.put(i)
    
#     # 요세푸스 순열 알고리즘에 의해 큐에서 한명씩 사람이 빠진다.
#     # 사람이 다 빠지면 반복문 종료
#     while not q.empty() : # 큐가 비어있지 않다면
    
#         # (0 - k-1)
#         for i in range(k):
#             num = q.get()
            
#             if i == k -1 :
#                 result.append(num)
#             else:
#                 q.put(num)
#     return result