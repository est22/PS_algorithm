class Node:
    def __init__ (self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None :
        pre_order(tree[node.left_node])
    if node.right_node != Node :
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != None :
        pre_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != Node :
        pre_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != None :
        pre_order(tree[node.left_node])
    if node.right_node != Node :
        pre_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()

    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
pre_order(tree['B'])
pre_order(tree['C'])
pre_order(tree['D'])
pre_order(tree['E'])
pre_order(tree['F'])
pre_order(tree['G'])
pre_order(tree['H'])
pre_order(tree['I'])
print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])

