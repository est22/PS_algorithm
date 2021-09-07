# leetcode 706
# open addressing

import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000 # 기본 사이즈
        self.table = collections.defaultdict(ListNode)
    
    # 삽입
    def put(self, key, value):
        index = key % self.size # size 개수만큼 modulo연산을 한 나머지를 해시값으로 정함
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None: 
            self.table[index] = ListNode(key, value)
            return
        # 인덱스에 노드가 있다면 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)


    # 조회
    def get(self):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1



    
    # 삭제
    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스 첫번째 노드일때 삭제처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next