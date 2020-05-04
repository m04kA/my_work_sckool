class Node:
    def __init__(self, num):
        self.right = None
        self.left = None
        self.value = num


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is  None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def find_num(tree, num):
    result = False
    if tree is None:
        return result
    #print(tree.value)
    if tree.value == num:
        result = True
        return result
    else:
        if tree.value > num:
            result = find_num(tree.left, num)

        elif tree.value < num:
            result = find_num(tree.right, num)
            #return result
    return result


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.value)
        print_tree(root.right)

root = Node(8)

insert(root, Node(3))
insert(root, Node(10))
insert(root, Node(1))
insert(root, Node(6))
insert(root, Node(4))
insert(root, Node(7))
insert(root, Node(14))
insert(root, Node(13))
insert(root, Node(13))

print_tree(root)
print('--------------------')
pol = find_num(root, 5)
print(f'Поиск числа 5: {pol}')

