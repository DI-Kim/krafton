from sys import stdin as s
import sys
sys.setrecursionlimit(1000000)

s = open('../input.txt', 'rt')

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        
        temp = self.root
        while temp is not None:
            if data > temp.data:
                if temp.right_child:
                    temp = temp.right_child
                else:
                    temp.right_child = new_node
                    return
            else:
                if temp.left_child:
                    temp = temp.left_child
                else:
                    temp.left_child = new_node
                    return
                
def post_order(node):
    if node is not None:
        post_order(node.left_child)
        post_order(node.right_child)
        print(node.data)

tree = Binary_Search_Tree()

while True:
    try:
        data = int(s.readline().strip())
        tree.insert(data)
    except:
        break

post_order(tree.root)
