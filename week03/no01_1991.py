from sys import stdin as s
s = open('../input.txt', 'rt')

node = {}

n = int(s.readline())
for i in range(n):
    data, left_child, right_child = s.readline().split()
    if left_child == '.':
        left_child = None
    if right_child == '.':
        right_child = None
    
    node[data] = [data, left_child, right_child]

def preorder(root):
    if root is not None:
        print(node[root][0], end= '')
        preorder(node[root][1])
        preorder(node[root][2])
def inorder(root):
    if root is not None:
        inorder(node[root][1])
        print(node[root][0], end= '')
        inorder(node[root][2])
def postorder(root):
    if root is not None:
        postorder(node[root][1])
        postorder(node[root][2])
        print(node[root][0], end= '')
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()