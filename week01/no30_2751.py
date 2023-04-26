import sys
# 힙정렬 사용
def swap(tree, index1, index2):
    temp = tree[index1]
    tree[index1] = tree[index2]
    tree[index2] = temp

def heapify(tree, index, tree_size):
    left_index = 2 * index
    right_index = 2 * index + 1

    largest = index

    if 0 < left_index < tree_size and tree[largest] < tree[left_index]:
        largest = left_index
    if 0 < right_index < tree_size and tree[largest] < tree[right_index]:
        largest = right_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)

def heapsort(tree):
    tree_size = len(tree)
    for i in range(tree_size - 1, -1, -1):
        heapify(tree, i, tree_size)
    
    for i in range(tree_size -1, -1, -1):
        swap(tree, 0, i)
        heapify(tree, 0, i)


# N
test_num = int(sys.stdin.readline())
# 새로운 리스트에 입력값 받음
new_list = []
for _ in range(test_num):
    new_list.append(int(sys.stdin.readline()))
# 정렬
# 리스트의 길이가 길지 않으면 sort 사용
# if len(new_list) < 10:
new_list.sort()
# else:
#     heapsort(new_list)

# 정렬된 list 출력
for i in new_list:
    print(i)