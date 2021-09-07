class Chaining:
    class Node:
        # 노드 객체 생성자 : key, data, link
        def __init__(self, key, data, link): 
            self.key = key
            self.data = data
            self.next = link  

    # chaining 객체 생성자 : 해시테이블 a
    def __init__(self, size):
        self.M = size # M = 테이블 사이즈
        self.a = [None] * size

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수

    def put(self, key, data):   # 삽입 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                p.data = data
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i])

    def get(self, key):     # 탐색 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:    # 탐색 성공
                return p.data
            p = p.next
        return None         # 탐색 실패

