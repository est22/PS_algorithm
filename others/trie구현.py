class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어삽입
    def insert(self, word): #asdf
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.word = True

    def search(self,word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.word
    
t=Trie()
t.insert('apple')
print(t.search('apple'))
t.insert('appear')
print(t.search('aple'))






